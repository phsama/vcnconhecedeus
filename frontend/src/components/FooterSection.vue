<script setup lang="ts">
import { RouterLink } from 'vue-router'
</script>

<template>
  <footer class="footer">
    <div class="container footer__inner">
      <p class="footer__brand">Você não conhece Deus</p>

      <nav class="footer__nav" aria-label="Links do rodapé">
        <RouterLink to="/terms">Termos</RouterLink>
        <RouterLink to="/privacy">Privacidade</RouterLink>
        <a href="mailto:contato@vocenahconhecedeus.com.br">Contato</a>
      </nav>

      <p class="footer__copy">
        © {{ new Date().getFullYear() }} · Um exercício de honestidade.
      </p>
    </div>
  </footer>
</template>

<style scoped>
.footer {
  padding-block: var(--space-8);
  border-top: 1px solid var(--gray-200);
}

.footer__inner {
  display: flex;
  flex-direction: column;
  gap: var(--space-3);
}

.footer__brand {
  font-family: var(--font-serif);
  font-size: var(--size-lg);
  font-style: italic;
  color: var(--black);
  max-width: none;
}

.footer__nav {
  display: flex;
  gap: var(--space-4);
  flex-wrap: wrap;
}

.footer__nav a {
  font-size: var(--size-sm);
  font-weight: 300;
  color: var(--gray-700);
  text-decoration: none;
  transition: color var(--transition);
}

.footer__nav a:hover { color: var(--black); }

.footer__copy {
  font-size: var(--size-xs);
  color: var(--gray-400);
  font-weight: 300;
  max-width: none;
}
</style>
