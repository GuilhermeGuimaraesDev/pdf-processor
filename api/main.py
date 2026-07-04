from fastapi import FastAPI, UploadFile, HTTPException
import shutil
import os

from kafka_producer import publish_pdf_metadata
from security import analisar_pdf

app = FastAPI()

UPLOAD_DIR = "/data/incoming"


@app.post("/upload")
async def upload_pdf(file: UploadFile):

    # Verifica se é PDF
    if not file.filename.lower().endswith(".pdf"):
        raise HTTPException(
            status_code=400,
            detail="Somente arquivos PDF são permitidos."
        )

    file_path = os.path.join(UPLOAD_DIR, file.filename)

    # Salva o arquivo
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    # Analisa o PDF
    relatorio = analisar_pdf(file_path)

    # Se reprovado, remove o arquivo
    if not relatorio["approved"]:
        os.remove(file_path)

        raise HTTPException(
            status_code=400,
            detail=relatorio
        )

    # Publica no Kafka
    publish_pdf_metadata(file_path)

    return {
        "filename": file.filename,
        "status": "enviado",
        "security": relatorio
    }


@app.get("/status/{job_id}")
def get_status(job_id: str):
    return {
        "job_id": job_id,
        "status": "processing/done"
    }


@app.get("/result/{job_id}")
def get_result(job_id: str):
    return {
        "job_id": job_id,
        "text": "texto extraído"
    }