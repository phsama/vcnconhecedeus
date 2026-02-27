# Você não conhece Deus

> Aprimoramos nossa evolução espiritual sem religião, conectando-se direto com Deus.

Um clube de conteúdo semanal sobre espiritualidade — sem dogmas, sem promessas vazias.

---

## Estrutura

```
voce-nao-conhece-deus/
├── backend/           # FastAPI + SQLAlchemy + SQLite
│   ├── app/
│   │   ├── main.py
│   │   ├── config.py
│   │   ├── database.py
│   │   ├── models.py
│   │   ├── schemas.py
│   │   ├── email_service.py
│   │   └── routers/
│   │       ├── subscribe.py
│   │       ├── verify.py
│   │       ├── unsubscribe.py
│   │       ├── health.py
│   │       └── admin.py
│   ├── requirements.txt
│   ├── Dockerfile
│   └── .env.example
├── frontend/          # Vue 3 + Vite + TypeScript
│   ├── src/
│   │   ├── api/
│   │   ├── components/
│   │   ├── views/
│   │   └── router/
│   ├── nginx.conf
│   └── Dockerfile
└── docker-compose.yml
```

---

## Rodando localmente (dev)

### Pré-requisitos
- Python 3.12+
- Node 20+

### Backend

```bash
cd backend
cp .env.example .env   # edite conforme necessário
pip install -r requirements.txt
uvicorn app.main:app --reload
# API em http://localhost:8000
# Docs em http://localhost:8000/api/docs
```

### Frontend

```bash
cd frontend
npm install
npm run dev
# App em http://localhost:3000
# Proxy automático: /api/* → http://localhost:8000
```

---

## Rodando via Docker

```bash
# 1. Configure o ambiente
cp backend/.env.example backend/.env
# Edite backend/.env com suas configurações

# 2. Suba tudo
docker-compose up --build

# App:  http://localhost:3000
# API:  http://localhost:8000/api/docs
```

---

## Configurar SMTP

Edite `backend/.env`:

```env
SMTP_HOST=smtp.gmail.com
SMTP_PORT=587
SMTP_USER=seu@gmail.com
SMTP_PASS=sua_senha_de_app
FROM_EMAIL=seu@gmail.com
PUBLIC_BASE_URL=http://localhost:3000
```

Se as variáveis SMTP estiverem **vazias**, o backend roda em **modo dev**:  
o link de verificação é logado no console (não envia e-mail de verdade).

---

## Fluxo de double opt-in

1. Usuário preenche e-mail no site
2. Backend cria `Subscriber` com `status=PENDING` + token único
3. E-mail de verificação é enviado (ou logado em dev)
4. Usuário clica no link: `GET /api/verify?token=...`
5. Status muda para `ACTIVE`, e-mail de boas-vindas é enviado
6. Link de cancelamento: `GET /api/unsubscribe?token=...` → `UNSUBSCRIBED`

---

## Exportar CSV de inscritos (admin)

```bash
# Com curl
curl -u admin:changeme \
  "http://localhost:8000/api/admin/subscribers?format=csv" \
  -o subscribers.csv

# Via browser
# GET http://localhost:8000/api/admin/subscribers?format=csv
# Username: admin | Password: changeme (definido em .env)
```

Colunas: `email, status, source, created_at, verified_at`

Altere as credenciais em `backend/.env`:
```env
ADMIN_USER=admin
ADMIN_PASS=uma_senha_segura
```

---

## Endpoints da API

| Método | Rota | Descrição |
|--------|-----|-----------|
| `GET` | `/api/health` | Status da API |
| `POST` | `/api/subscribe` | Inscrever e-mail |
| `GET` | `/api/verify?token=` | Confirmar e-mail |
| `GET` | `/api/unsubscribe?token=` | Cancelar inscrição |
| `GET` | `/api/admin/subscribers` | Export CSV (Basic Auth) |

---

## Variáveis de ambiente

| Variável | Padrão | Descrição |
|----------|--------|-----------|
| `SMTP_HOST` | `""` | Host SMTP (vazio = modo dev) |
| `SMTP_PORT` | `587` | Porta SMTP |
| `SMTP_USER` | `""` | Usuário SMTP |
| `SMTP_PASS` | `""` | Senha SMTP |
| `FROM_EMAIL` | `noreply@...` | E-mail remetente |
| `PUBLIC_BASE_URL` | `http://localhost:3000` | URL do frontend |
| `ADMIN_USER` | `admin` | Usuário do admin |
| `ADMIN_PASS` | `changeme` | Senha do admin |
| `DATABASE_URL` | `sqlite:///./data/subscribers.db` | URL do banco |

---

## Monetização futura

- **Newsletter gratuita** — topo do funil (implementado)
- **Lista de espera** — pré-venda da assinatura (implementado)
- **Assinatura mensal/anual** — conteúdo completo + áudio + acervo
- **Círculo / mentoria** — encontro mensal ao vivo em grupo
