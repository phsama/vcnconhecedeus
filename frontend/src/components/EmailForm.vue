<script setup lang="ts">
import { ref, computed } from 'vue'
import { subscribeEmail } from '@/api/subscribe'

const props = defineProps<{
  source: 'newsletter' | 'waitlist'
  ctaLabel?: string
}>()

const email = ref('')
const honeypot = ref('')
const loading = ref(false)
const status = ref<'idle' | 'success' | 'error'>('idle')
const message = ref('')

const cta = computed(() => props.ctaLabel ?? 'Quero receber')

async function submit() {
  if (!email.value.trim() || loading.value) return

  loading.value = true
  status.value = 'idle'
  message.value = ''

  const result = await subscribeEmail({
    email: email.value.trim(),
    source: props.source,
    website: honeypot.value,
  })

  loading.value = false
  status.value = result.ok ? 'success' : 'error'
  message.value = result.message

  if (result.ok) {
    email.value = ''
  }
}
</script>

<template>
  <form class="email-form" @submit.prevent="submit" novalidate>
    <!-- Honeypot — hidden from real users -->
    <div class="honeypot" aria-hidden="true">
      <label for="hp-website">Deixe em branco</label>
      <input id="hp-website" v-model="honeypot" type="text" name="website" tabindex="-1" autocomplete="off" />
    </div>

    <div class="email-form__row">
      <label for="email-input" class="visually-hidden">Seu e-mail</label>
      <input
        id="email-input"
        v-model="email"
        type="email"
        name="email"
        placeholder="seu@email.com"
        autocomplete="email"
        :disabled="loading || status === 'success'"
        required
        aria-label="Endereço de e-mail"
      />
      <button
        type="submit"
        class="btn"
        :disabled="loading || status === 'success' || !email.trim()"
        :aria-label="cta"
      >
        <span v-if="loading" class="spinner" aria-hidden="true"></span>
        <span>{{ loading ? 'Enviando…' : cta }}</span>
      </button>
    </div>

    <transition name="fade">
      <p
        v-if="message"
        class="email-form__msg"
        :class="status === 'success' ? 'email-form__msg--success' : 'email-form__msg--error'"
        role="alert"
        aria-live="polite"
      >
        {{ message }}
      </p>
    </transition>
  </form>
</template>

<style scoped>
.visually-hidden {
  position: absolute;
  width: 1px;
  height: 1px;
  padding: 0;
  margin: -1px;
  overflow: hidden;
  clip: rect(0, 0, 0, 0);
  white-space: nowrap;
  border: 0;
}

.email-form {
  display: flex;
  flex-direction: column;
  gap: var(--space-2);
}

.email-form__row {
  display: flex;
  align-items: flex-end;
  gap: var(--space-3);
}

.email-form__row input[type="email"] {
  flex: 1;
  min-width: 0;
}

.email-form__msg {
  font-size: var(--size-sm);
  font-family: var(--font-sans);
  font-weight: 300;
}

.email-form__msg--success { color: var(--black); }
.email-form__msg--error   { color: #b00020; }

.spinner {
  display: inline-block;
  width: 12px;
  height: 12px;
  border: 1.5px solid currentColor;
  border-top-color: transparent;
  border-radius: 50%;
  animation: spin 0.7s linear infinite;
}

@keyframes spin {
  to { transform: rotate(360deg); }
}

@media (max-width: 480px) {
  .email-form__row {
    flex-direction: column;
    align-items: stretch;
  }
  .email-form__row .btn {
    width: 100%;
    justify-content: center;
  }
}
</style>
