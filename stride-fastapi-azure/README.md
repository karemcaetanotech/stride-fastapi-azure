# STRIDE API (FastAPI)

Protótipo simples para análise STRIDE via FastAPI.

## Como rodar
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
python -m uvicorn app.main:app --reload --port 8000

## Endpoints
GET  /health
POST /analyze-text  { "description": "API com login, S3, gateway..." }

## Notas
Versão de entrega focada em estrutura do projeto e stub da análise STRIDE.
