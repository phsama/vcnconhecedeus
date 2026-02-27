import { createRouter, createWebHistory } from 'vue-router'

const router = createRouter({
    history: createWebHistory(import.meta.env.BASE_URL),
    routes: [
        { path: '/', component: () => import('@/views/HomeView.vue'), meta: { title: 'Você não conhece Deus' } },
        { path: '/verified', component: () => import('@/views/VerifiedView.vue'), meta: { title: 'E-mail confirmado' } },
        { path: '/unsubscribed', component: () => import('@/views/UnsubscribedView.vue'), meta: { title: 'Descadastrado' } },
        { path: '/privacy', component: () => import('@/views/PrivacyView.vue'), meta: { title: 'Privacidade' } },
        { path: '/terms', component: () => import('@/views/TermsView.vue'), meta: { title: 'Termos de Uso' } },
    ],
    scrollBehavior() {
        return { top: 0 }
    },
})

router.afterEach((to) => {
    const title = to.meta.title as string | undefined
    document.title = title ? `${title} · Você não conhece Deus` : 'Você não conhece Deus'
})

export default router
