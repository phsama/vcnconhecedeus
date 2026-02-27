<script setup lang="ts">
import EmailForm from './EmailForm.vue'
import { onMounted, onUnmounted, ref } from 'vue'

const hero = ref<HTMLElement | null>(null)
const visible = ref(false)

let observer: IntersectionObserver | null = null

onMounted(() => {
  observer = new IntersectionObserver(
    ([entry]) => { if (entry.isIntersecting) visible.value = true },
    { threshold: 0.1 }
  )
  if (hero.value) observer.observe(hero.value)
})

onUnmounted(() => observer?.disconnect())
</script>

<template>
  <section class="hero" ref="hero">
    <div class="hero__container container">
      <!-- Label / eyebrow -->
      <p class="hero__label" :class="{ 'in-view': visible }">
        Um clube de espiritualidade real
      </p>

      <!-- Main question -->
      <h1 class="hero__question" :class="{ 'in-view': visible }">
        Aprimoramos nossa<br />
        evolução espiritual sem religião,<br />
        conectando-se direto com Deus.
      </h1>

      <!-- Subline -->
      <p class="hero__sub" :class="{ 'in-view': visible }">
        Um conteúdo por semana. Uma prática. Uma pergunta que fica.
      </p>

      <!-- Form -->
      <div class="hero__form" :class="{ 'in-view': visible }">
        <EmailForm source="newsletter" cta-label="Quero receber os conteúdos" />
        <p class="hero__microcopy">
          Sem spam. 1 e-mail por semana. Cancelamento em 1 clique.
        </p>
      </div>
    </div>

    <!-- Decorative horizontal rule -->
    <div class="hero__rule"></div>
  </section>
</template>

<style scoped>
.hero {
  min-height: 100svh;
  display: flex;
  flex-direction: column;
  justify-content: center;
  padding-top: var(--space-16);
  padding-bottom: var(--space-12);
  position: relative;
}

.hero__container {
  display: flex;
  flex-direction: column;
  gap: var(--space-6);
}

/* Staggered reveal animations */
.hero__label,
.hero__question,
.hero__sub,
.hero__form {
  opacity: 0;
  transform: translateY(24px);
  transition: opacity 700ms ease, transform 700ms ease;
}

.hero__label.in-view    { opacity: 1; transform: none; transition-delay: 0ms; }
.hero__question.in-view { opacity: 1; transform: none; transition-delay: 80ms; }
.hero__sub.in-view      { opacity: 1; transform: none; transition-delay: 180ms; }
.hero__form.in-view     { opacity: 1; transform: none; transition-delay: 280ms; }

.hero__label {
  font-family: var(--font-sans);
  font-size: var(--size-xs);
  font-weight: 500;
  letter-spacing: 0.15em;
  text-transform: uppercase;
  color: var(--gray-400);
}

.hero__question {
  font-family: var(--font-serif);
  font-size: clamp(2rem, 5vw, 3.75rem);
  font-weight: 400;
  font-style: italic;
  line-height: 1.1;
  letter-spacing: -0.02em;
  max-width: 18ch;
}

.hero__sub {
  font-family: var(--font-sans);
  font-size: var(--size-lg);
  font-weight: 300;
  color: var(--gray-700);
  max-width: 50ch;
}

.hero__form {
  display: flex;
  flex-direction: column;
  gap: var(--space-2);
  max-width: 480px;
}

.hero__microcopy {
  font-size: var(--size-xs);
  color: var(--gray-400);
  font-weight: 300;
  max-width: none;
}

.hero__rule {
  position: absolute;
  bottom: 0;
  left: 0;
  right: 0;
  height: 1px;
  background: var(--gray-200);
}
</style>
