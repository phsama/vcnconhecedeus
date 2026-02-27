const BASE = import.meta.env.VITE_API_BASE ?? '/api'

export interface SubscribePayload {
    email: string
    source: 'newsletter' | 'waitlist'
    website?: string
}

export interface SubscribeResult {
    ok: boolean
    message: string
}

export async function subscribeEmail(payload: SubscribePayload): Promise<SubscribeResult> {
    try {
        const res = await fetch(`${BASE}/subscribe`, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(payload),
        })

        const data = await res.json()

        if (!res.ok) {
            return { ok: false, message: data.detail ?? 'Algo deu errado. Tente novamente.' }
        }

        return { ok: true, message: data.message ?? 'Cadastro realizado.' }
    } catch {
        return { ok: false, message: 'Sem conexão com o servidor. Tente mais tarde.' }
    }
}
