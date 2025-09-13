FROM python:3.10-slim

RUN apt-get update && apt-get install -y tesseract-ocr poppler-utils

WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .

CMD ["python", "app.py"]
producer/app.py (exemplo inicial)
import os, json
from kafka import KafkaProducer

producer = KafkaProducer(
    bootstrap_servers=os.getenv("KAFKA_BOOTSTRAP_SERVERS", "kafka:9092"),
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

def publish_pdf_metadata(pdf_path):
    msg = {"id": os.path.basename(pdf_path), "path": pdf_path}
    producer.send("pdf_incoming", value=msg)
    producer.flush()
    print(f"Publicado: {msg}")

if __name__ == "__main__":
    publish_pdf_metadata("/data/incoming/exemplo.pdf")
