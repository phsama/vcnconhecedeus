<script setup lang="ts">
import { onMounted, onUnmounted, ref } from 'vue'
import EmailForm from './EmailForm.vue'

const section = ref<HTMLElement | null>(null)
const visible = ref(false)
const activeTab = ref<'newsletter' | 'waitlist'>('newsletter')

let observer: IntersectionObserver | null = null

onMounted(() => {
  observer = new IntersectionObserver(
    ([entry]) => { if (entry.isIntersecting) visible.value = true },
    { threshold: 0.1 }
  )
  if (section.value) observer.observe(section.value)
})

onUnmounted(() => observer?.disconnect())
</script>

<template>
  <section class="subscribe" ref="section" id="lista">
    <div class="container">
      <p class="subscribe__label reveal" :class="{ 'in-view': visible }">
        Junte-se
      </p>

      <h2 class="subscribe__heading reveal" :class="{ 'in-view': visible }">
        Escolha como começar.
      </h2>

      <!-- Tab toggles -->
      <div class="subscribe__tabs reveal" :class="{ 'in-view': visible }" role="tablist" aria-label="Tipo de inscrição">
        <button
          class="subscribe__tab"
          :class="{ active: activeTab === 'newsletter' }"
          role="tab"
          :aria-selected="activeTab === 'newsletter'"
          aria-controls="panel-newsletter"
          @click="activeTab = 'newsletter'"
        >
          Newsletter gratuita
        </button>
        <button
          class="subscribe__tab"
          :class="{ active: activeTab === 'waitlist' }"
          role="tab"
          :aria-selected="activeTab === 'waitlist'"
          aria-controls="panel-waitlist"
          @click="activeTab = 'waitlist'"
        >
          Quero a assinatura
        </button>
      </div>

      <!-- Newsletter panel -->
      <transition name="fade" mode="out-in">
        <div
          v-if="activeTab === 'newsletter'"
          id="panel-newsletter"
          class="subscribe__panel reveal"
          :class="{ 'in-view': visible }"
          role="tabpanel"
          aria-labelledby="tab-newsletter"
        >
          <p class="subscribe__desc">
            Receba um conteúdo por semana — texto, prática e pergunta-guia.<br />
            <strong>Grátis.</strong> Sempre.
          </p>
          <EmailForm source="newsletter" cta-label="Entrar na lista" />
        </div>

        <div
          v-else
          id="panel-waitlist"
          class="subscribe__panel reveal"
          :class="{ 'in-view': visible }"
          role="tabpanel"
          aria-labelledby="tab-waitlist"
        >
          <p class="subscribe__desc">
            A assinatura inclui práticas em áudio, acervo completo e encontros mensais ao vivo.<br />
            <strong>Avise-me quando abrir.</strong>
          </p>
          <EmailForm source="waitlist" cta-label="Quero ser avisado" />
        </div>
      </transition>

      <!-- Offer breakdown -->
      <div class="subscribe__tiers reveal" :class="{ 'in-view': visible }">
        <div class="subscribe__tier">
          <span class="subscribe__tier-label">Gratuito</span>
          <ul>
            <li>Texto semanal</li>
            <li>Prática (10–20 min)</li>
            <li>Pergunta-guia</li>
          </ul>
        </div>
        <div class="subscribe__tier-divider"></div>
        <div class="subscribe__tier subscribe__tier--muted">
          <span class="subscribe__tier-label">Assinatura <em>em breve</em></span>
          <ul>
            <li>Tudo do gratuito</li>
            <li>Áudio / meditação</li>
            <li>Acervo completo</li>
            <li>Encontro mensal ao vivo</li>
          </ul>
        </div>
      </div>
    </div>
  </section>
</template>

<style scoped>
.subscribe {
  padding-block: var(--space-16);
  border-bottom: 1px solid var(--gray-200);
}

.subscribe__label {
  font-size: var(--size-xs);
  font-weight: 500;
  letter-spacing: 0.15em;
  text-transform: uppercase;
  color: var(--gray-400);
  margin-bottom: var(--space-4);
}

.subscribe__heading {
  margin-bottom: var(--space-6);
}

/* Tabs */
.subscribe__tabs {
  display: flex;
  gap: 0;
  border-bottom: 1px solid var(--gray-200);
  margin-bottom: var(--space-6);
}

.subscribe__tab {
  background: none;
  border: none;
  padding: var(--space-2) 0;
  margin-right: var(--space-6);
  font-family: var(--font-sans);
  font-size: var(--size-sm);
  font-weight: 400;
  color: var(--gray-400);
  cursor: pointer;
  position: relative;
  transition: color var(--transition);
  letter-spacing: 0.03em;
}

.subscribe__tab::after {
  content: '';
  position: absolute;
  bottom: -1px;
  left: 0;
  right: 0;
  height: 1.5px;
  background: var(--black);
  transform: scaleX(0);
  transition: transform var(--transition);
}

.subscribe__tab.active {
  color: var(--black);
  font-weight: 500;
}

.subscribe__tab.active::after {
  transform: scaleX(1);
}

.subscribe__tab:focus-visible {
  outline: 2px solid var(--black);
  outline-offset: 4px;
}

/* Panel */
.subscribe__panel {
  display: flex;
  flex-direction: column;
  gap: var(--space-3);
  max-width: 480px;
  margin-bottom: var(--space-8);
}

.subscribe__desc {
  font-size: var(--size-base);
  font-weight: 300;
  color: var(--gray-700);
  line-height: 1.65;
}

/* Tiers */
.subscribe__tiers {
  display: flex;
  gap: var(--space-6);
  flex-wrap: wrap;
  padding-top: var(--space-6);
  border-top: 1px solid var(--gray-200);
}

.subscribe__tier {
  display: flex;
  flex-direction: column;
  gap: var(--space-2);
}

.subscribe__tier ul {
  list-style: none;
  display: flex;
  flex-direction: column;
  gap: var(--space-1);
}

.subscribe__tier ul li {
  font-size: var(--size-sm);
  font-weight: 300;
  color: var(--gray-700);
  padding-left: var(--space-2);
  border-left: 1px solid var(--gray-200);
}

.subscribe__tier--muted .subscribe__tier-label,
.subscribe__tier--muted ul li {
  color: var(--gray-400);
}

.subscribe__tier-label {
  font-size: var(--size-xs);
  font-weight: 500;
  letter-spacing: 0.1em;
  text-transform: uppercase;
  color: var(--black);
}

.subscribe__tier-label em {
  font-style: normal;
  font-weight: 300;
  font-size: var(--size-xs);
  color: var(--gray-400);
  text-transform: none;
  letter-spacing: 0;
}

.subscribe__tier-divider {
  width: 1px;
  background: var(--gray-200);
  align-self: stretch;
}

/* Reveal animations */
.reveal {
  opacity: 0;
  transform: translateY(20px);
  transition: opacity 600ms ease, transform 600ms ease;
}

.reveal.in-view {
  opacity: 1;
  transform: none;
}
</style>
