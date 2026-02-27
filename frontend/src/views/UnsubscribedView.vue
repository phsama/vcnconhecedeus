<script setup lang="ts">
import { RouterLink } from 'vue-router'
</script>

<template>
  <main class="simple-page">
    <div class="container simple-page__inner">
      <h1 class="simple-page__heading">Descadastrado.</h1>
      <p class="simple-page__body">
        Tudo bem. O caminho é seu.
      </p>
      <p class="simple-page__sub">
        Se mudar de ideia, a porta está aberta.
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
