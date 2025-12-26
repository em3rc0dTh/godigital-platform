from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional
from extractor import UltraReceiptExtractor, adapt_to_transaction_schema

app = FastAPI(
    title="Ultra Receipt Extractor API",
    version="1.0.0"
)

extractor = UltraReceiptExtractor()

# =========================
# MODELOS
# =========================
class ExtractRequest(BaseModel):
    html: str
    formato: Optional[str] = "dict"   # dict | json
    detalles: Optional[bool] = False

class BatchRequest(BaseModel):
    html_list: List[str]

# =========================
# ENDPOINTS
# =========================
@app.post("/extract")
def extract_receipt(req: ExtractRequest):
    if len(req.html.strip()) < 50:
        raise HTTPException(status_code=400, detail="HTML insuficiente")

    raw = extractor.analyze(req.html)
    adapted = adapt_to_transaction_schema(raw)

    return adapted


@app.post("/extract/batch")
def extract_batch(req: BatchRequest):
    if not req.html_list:
        raise HTTPException(status_code=400, detail="Lista vacía")

    df = extractor.analyze_batch(req.html_list)
    return df.to_dict(orient="records")


@app.get("/health")
def health():
    return {
        "status": "ok",
        "ai_available": extractor.ai_available
    }
