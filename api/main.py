from fastapi import FastAPI, UploadFile, File
import uuid

app = FastAPI(title="PDF Processor API", version="1.0.0")

# Endpoint inicial
@app.get("/")
def home():
    return {"status": "API rodando 🚀"}

# Endpoint para verificar a saúde do sistema
@app.get("/health")
def health_check():
    return {"status": "ok"}

# Endpoint para upload de PDF
@app.post("/upload")
async def upload_pdf(file: UploadFile = File(...)):
    # Gera um ID único para o job
    job_id = str(uuid.uuid4())
    
    # Aqui você vai salvar o arquivo em uma pasta (ex.: data/incoming/)
    # e publicar uma mensagem no Kafka
    return {"job_id": job_id, "filename": file.filename, "status": "enviado"}

# Endpoint para consultar o status de um job
@app.get("/status/{job_id}")
def check_status(job_id: str):
    # Aqui no futuro vamos consultar no Postgres
    return {"job_id": job_id, "status": "processing"}

# Endpoint para buscar o resultado de um job
@app.get("/result/{job_id}")
def get_result(job_id: str):
    # Aqui no futuro vamos trazer o texto processado do Postgres
    return {"job_id": job_id, "result": "Texto extraído será mostrado aqui"}


