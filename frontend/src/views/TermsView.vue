<script setup lang="ts">
import { RouterLink } from 'vue-router'
</script>

<template>
  <main class="doc-page">
    <div class="container doc-page__inner">
      <RouterLink to="/" class="doc-page__back">← Início</RouterLink>

      <h1>Termos de Uso</h1>
      <p class="doc-page__date">Última atualização: fevereiro de 2026</p>

      <section>
        <h3>O que é este espaço</h3>
        <p>Um clube de conteúdo sobre espiritualidade. Não é terapia, aconselhamento religioso ou promessa de resultado espiritual.</p>
      </section>

      <section>
        <h3>Responsabilidade</h3>
        <p>O conteúdo é para reflexão pessoal. Você é responsável por como o aplica na sua vida.</p>
      </section>

      <section>
        <h3>Direitos</h3>
        <p>Todo o conteúdo é de autoria do clube. Não reproduza sem autorização.</p>
      </section>

      <section>
        <h3>Cancelamento</h3>
        <p>Você pode sair quando quiser, pelo link em qualquer e-mail. Simples assim.</p>
      </section>

      <section>
        <h3>Alterações</h3>
        <p>Podemos atualizar estes termos. Comunicaremos por e-mail em caso de mudanças relevantes.</p>
      </section>

      <section>
        <h3>Contato</h3>
        <p><a href="mailto:contato@vocenahconhecedeus.com.br">contato@vocenahconhecedeus.com.br</a></p>
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
  font-size: var(--size-xs);
  font-family: var(--font-sans);
  font-weight: 500;
  letter-spacing: 0.05em;
  text-transform: uppercase;
  color: var(--gray-400);
}
</style>
