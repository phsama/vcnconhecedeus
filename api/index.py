import sys
import os

# Adiciona o diretório backend ao path para importar o app
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'backend'))

from app.main import app  # noqa: F401 — Vercel detecta automaticamente
