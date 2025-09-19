from fastapi import FastAPI, UploadFile, File
from pydantic import BaseModel
from typing import Dict, List
from dotenv import load_dotenv

load_dotenv()
app = FastAPI(title="STRIDE API")

@app.get("/health")
def health():
    return {"status": "ok"}

class ArchText(BaseModel):
    description: str

def simple_stride(text: str) -> Dict[str, List[str]]:
    """Heurística bem simples só para demo/entrega."""
    t = text.lower()
    out = {
        "Spoofing": [],
        "Tampering": [],
        "Repudiation": [],
        "InformationDisclosure": [],
        "DenialOfService": [],
        "ElevationOfPrivilege": [],
    }
    if "login" in t or "auth" in t:
        out["Spoofing"].append("Fortalecer autenticação (MFA, lockout, senha forte).")
        out["Repudiation"].append("Auditar logins, guardar logs imutáveis.")
    if "s3" in t or "blob" in t or "bucket" in t or "storage" in t:
        out["InformationDisclosure"].append("Criptografar em repouso e em trânsito; políticas de acesso mínimas.")
    if "api" in t or "gateway" in t:
        out["DenialOfService"].append("Rate limiting, circuit breaker e WAF no gateway.")
        out["Tampering"].append("Assinar/validar payloads; validação de entrada.")
    if "admin" in t or "root" in t:
        out["ElevationOfPrivilege"].append("Separação de papéis, MFA reforçado e acesso just-in-time.")

    return out

@app.post("/analyze-text")
def analyze_text(body: ArchText):
    """Recebe descrição textual da arquitetura e devolve uma análise STRIDE de exemplo."""
    return {"stride": simple_stride(body.description)}

@app.post("/analyze-image")
async def analyze_image(file: UploadFile = File(...)):
    """Stub para imagem (demo)."""
    return {
        "note": "Protótipo: para a entrega, envie texto em /analyze-text. "
                "A versão com Azure OpenAI extrairia entidades do diagrama."
    }
