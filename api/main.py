from fastapi import FastAPI, UploadFile
import shutil
import os
import json
import time
from kafka import KafkaProducer, errors

app = FastAPI()

UPLOAD_DIR = "/data/incoming"

# Configura producer Kafka interno da API
for i in range(10):  # tenta 10 vezes
    try:
        producer = KafkaProducer(bootstrap_servers="kafka:9092")
        print("Conectado ao Kafka!")
        break
    except errors.NoBrokersAvailable:
        print("Kafka não disponível, tentando novamente...")
        time.sleep(5)
else:
    raise Exception("Não foi possível conectar ao Kafka após várias tentativas.")

def publish_pdf_metadata(pdf_path: str):
    msg = {"id": os.path.basename(pdf_path), "path": pdf_path}
    producer.send("pdf_incoming", value=msg)
    producer.flush()
    print(f"[API] Publicado: {msg}")

@app.post("/upload")
async def upload_pdf(file: UploadFile):
    file_path = os.path.join(UPLOAD_DIR, file.filename)
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    publish_pdf_metadata(file_path)
    return {"filename": file.filename, "status": "enviado"}

@app.get("/status/{job_id}")
def get_status(job_id: str):
    return {"job_id": job_id, "status": "processing/done"}  # depois conecta no DB

@app.get("/result/{job_id}")
def get_result(job_id: str):
    return {"job_id": job_id, "text": "texto extraído"}  # depois conecta no DB
