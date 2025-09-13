from fastapi import FastAPI, UploadFile
import shutil, os
from producer.app import publish_pdf_metadata

app = FastAPI()

UPLOAD_DIR = "/data/incoming"

@app.post("/upload")
async def upload_pdf(file: UploadFile):
    file_path = os.path.join(UPLOAD_DIR, file.filename)
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    publish_pdf_metadata(file_path)
    return {"filename": file.filename, "status": "enviado"}

@app.get("/status/{job_id}")
def get_status(job_id: str):
    return {"job_id": job_id, "status": "processing/done"}  # Conectar ao DB para status real

@app.get("/result/{job_id}")
def get_result(job_id: str):
    return {"job_id": job_id, "text": "texto extraído"}  # Conectar ao DB para resultado real
