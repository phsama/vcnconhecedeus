<script setup lang="ts">
import { onMounted, onUnmounted, ref } from 'vue'

const section = ref<HTMLElement | null>(null)
const visible = ref(false)

let observer: IntersectionObserver | null = null

onMounted(() => {
  observer = new IntersectionObserver(
    ([entry]) => { if (entry.isIntersecting) visible.value = true },
    { threshold: 0.1 }
  )
  if (section.value) observer.observe(section.value)
})

onUnmounted(() => observer?.disconnect())

const steps = [
  {
    num: '01',
    title: 'Um texto',
    desc: 'Curto. Sem rodeios. Vai direto ao ponto.',
  },
  {
    num: '02',
    title: 'Uma prática',
    desc: 'De 10 a 20 minutos. Silêncio, escrita, atenção — o que couber no seu dia.',
  },
  {
    num: '03',
    title: 'Uma pergunta',
    desc: 'Que fica. Que incomoda. Que abre algo.',
  },
]

const topics = [
  'Símbolo e linguagem sagrada',
  'Autoconsciência',
  'Silêncio e contemplação',
  'Disciplina espiritual',
  'Ética e sombra',
  'Encontro com o Absoluto',
  'Misticismo comparado',
  'Presença e atenção',
]
</script>

<template>
  <section class="how" ref="section" id="como-funciona">
    <div class="container">
      <!-- Eyebrow -->
      <p class="how__label reveal" :class="{ 'in-view': visible }">
        Como funciona
      </p>

      <h2 class="how__heading reveal" :class="{ 'in-view': visible }">
        Simples como deve ser.
      </h2>

      <!-- 3 steps -->
      <div class="how__steps">
        <div
          v-for="(step, i) in steps"
          :key="step.num"
          class="how__step reveal"
          :class="{ 'in-view': visible }"
          :style="{ transitionDelay: `${100 + i * 80}ms` }"
        >
          <span class="how__step-num">{{ step.num }}</span>
          <div class="how__step-body">
            <strong class="how__step-title">{{ step.title }}</strong>
            <p class="how__step-desc">{{ step.desc }}</p>
          </div>
        </div>
      </div>

      <hr class="hr" />

      <!-- Topics -->
      <p class="how__topics-label reveal" :class="{ 'in-view': visible }">
        O que você vai encontrar
      </p>
      <ul class="how__topics reveal" :class="{ 'in-view': visible }">
        <li v-for="topic in topics" :key="topic">{{ topic }}</li>
      </ul>
    </div>
  </section>
</template>

<style scoped>
.how {
  padding-block: var(--space-16);
  border-bottom: 1px solid var(--gray-200);
}

.how__label {
  font-size: var(--size-xs);
  font-weight: 500;
  letter-spacing: 0.15em;
  text-transform: uppercase;
  color: var(--gray-400);
  margin-bottom: var(--space-4);
}

.how__heading {
  margin-bottom: var(--space-8);
}

/* Steps */
.how__steps {
  display: flex;
  flex-direction: column;
  gap: 0;
}

.how__step {
  display: flex;
  align-items: baseline;
  gap: var(--space-4);
  padding-block: var(--space-4);
  border-top: 1px solid var(--gray-200);
}

.how__step:last-child {
  border-bottom: 1px solid var(--gray-200);
}

.how__step-num {
  font-family: var(--font-serif);
  font-size: var(--size-3xl);
  font-weight: 400;
  color: var(--gray-200);
  min-width: 3.5rem;
  line-height: 1;
}

.how__step-body {
  display: flex;
  flex-direction: column;
  gap: var(--space-1);
}

.how__step-title {
  font-family: var(--font-serif);
  font-size: var(--size-xl);
  font-weight: 400;
  color: var(--black);
}

.how__step-desc {
  font-weight: 300;
  font-size: var(--size-base);
  color: var(--gray-700);
  max-width: 50ch;
}

/* Topics */
.how__topics-label {
  font-size: var(--size-xs);
  font-weight: 500;
  letter-spacing: 0.15em;
  text-transform: uppercase;
  color: var(--gray-400);
  margin-bottom: var(--space-3);
  max-width: none;
}

.how__topics {
  list-style: none;
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
  gap: var(--space-2) var(--space-4);
}

.how__topics li {
  font-size: var(--size-base);
  font-weight: 300;
  color: var(--gray-700);
  padding-left: var(--space-3);
  border-left: 1px solid var(--gray-200);
  line-height: 1.4;
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
