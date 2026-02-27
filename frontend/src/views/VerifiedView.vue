<script setup lang="ts">
import { RouterLink } from 'vue-router'
</script>

<template>
  <main class="simple-page">
    <div class="container simple-page__inner">
      <span class="simple-page__symbol" aria-hidden="true">✓</span>
      <h1 class="simple-page__heading">E-mail confirmado.</h1>
      <p class="simple-page__body">
        Bem-vindo.<br />
        Seu primeiro conteúdo chega na semana que vem.
      </p>
      <p class="simple-page__sub">
        Enquanto isso — observe o que aparece.
      </p>
      <RouterLink to="/" class="btn btn--ghost">Voltar ao início</RouterLink>
    </div>
  </main>
</template>

<style scoped>
.simple-page {
  min-height: 100svh;
  display: flex;
  align-items: center;
}

.simple-page__inner {
  display: flex;
  flex-direction: column;
  gap: var(--space-4);
  padding-block: var(--space-16);
}

.simple-page__symbol {
  font-size: var(--size-2xl);
  color: var(--gray-400);
}

.simple-page__heading {
  font-style: italic;
}

.simple-page__body {
  font-size: var(--size-lg);
  font-weight: 300;
  line-height: 1.8;
}

.simple-page__sub {
  font-size: var(--size-sm);
  color: var(--gray-400);
  font-style: italic;
  max-width: none;
}
</style>
