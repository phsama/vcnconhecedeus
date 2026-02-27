<script setup lang="ts">
import { RouterLink } from 'vue-router'
</script>

<template>
  <main class="doc-page">
    <div class="container doc-page__inner">
      <RouterLink to="/" class="doc-page__back">← Início</RouterLink>

      <h1>Política de Privacidade</h1>
      <p class="doc-page__date">Última atualização: fevereiro de 2026</p>

      <section>
        <h3>O que coletamos</h3>
        <p>Somente seu endereço de e-mail, fornecido voluntariamente ao se inscrever.</p>
      </section>

      <section>
        <h3>Como usamos</h3>
        <p>Seu e-mail é usado exclusivamente para enviar os conteúdos semanais e comunicações relacionadas ao clube. Não vendemos, compartilhamos ou cedemos seus dados a terceiros.</p>
      </section>

      <section>
        <h3>Cancelamento</h3>
        <p>Todo e-mail enviado contém um link de cancelamento. Um clique, e pronto. Sem perguntas.</p>
      </section>

      <section>
        <h3>Armazenamento</h3>
        <p>Seus dados ficam em servidores seguros. Guardamos apenas o mínimo necessário.</p>
      </section>

      <section>
        <h3>Contato</h3>
        <p>Dúvidas? <a href="mailto:contato@vocenahconhecedeus.com.br">contato@vocenahconhecedeus.com.br</a></p>
      </section>
    </div>
  </main>
</template>

<style scoped>
.doc-page {
  padding-block: var(--space-16);
  min-height: 100svh;
}

.doc-page__inner {
  display: flex;
  flex-direction: column;
  gap: var(--space-6);
}

.doc-page__back {
  font-size: var(--size-sm);
  color: var(--gray-400);
  text-decoration: none;
  letter-spacing: 0.05em;
  transition: color var(--transition);
}

.doc-page__back:hover { color: var(--black); }

h1 { margin-bottom: 0; }

.doc-page__date {
  font-size: var(--size-xs);
  color: var(--gray-400);
  max-width: none;
}

section {
  display: flex;
  flex-direction: column;
  gap: var(--space-2);
  padding-top: var(--space-4);
  border-top: 1px solid var(--gray-200);
}

h3 {
  font-size: var(--size-base);
  font-family: var(--font-sans);
  font-weight: 500;
  letter-spacing: 0.05em;
  text-transform: uppercase;
  font-size: var(--size-xs);
  color: var(--gray-400);
}
</style>
