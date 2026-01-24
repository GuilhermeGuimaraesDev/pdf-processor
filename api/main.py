from fastapi import FastAPI, UploadFile
import shutil
import os

from kafka_producer import publish_pdf_metadata  # 👈 USA O PRODUCER CERTO

app = FastAPI()

UPLOAD_DIR = "/data/incoming"


@app.post("/upload")
async def upload_pdf(file: UploadFile):
    file_path = os.path.join(UPLOAD_DIR, file.filename)

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    publish_pdf_metadata(file_path)

    return {
        "filename": file.filename,
        "status": "enviado"
    }


@app.get("/status/{job_id}")
def get_status(job_id: str):
    return {"job_id": job_id, "status": "processing/done"}


@app.get("/result/{job_id}")
def get_result(job_id: str):
    return {"job_id": job_id, "text": "texto extraído"}
