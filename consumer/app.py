import os, json
import time
from kafka import KafkaConsumer, KafkaProducer, errors
import pytesseract
from pdf2image import convert_from_path
from sqlalchemy import create_engine, Table, Column, String, MetaData, Text

# Conexão DB
engine = create_engine(os.getenv("DATABASE_URL", "postgresql://postgres:postgres@postgres:5432/pdfdb"))
metadata = MetaData()
jobs = Table("jobs", metadata,
             Column("id", String, primary_key=True),
             Column("filename", String),
             Column("text", Text))
metadata.create_all(engine)

# Kafka
for i in range(10):
    try:
        consumer = KafkaConsumer(
            "pdf_incoming",
            bootstrap_servers="kafka:9092",
            group_id="pdf_group"
        )
        print("Conectado ao Kafka!")
        break
    except errors.NoBrokersAvailable:
        print("Kafka não disponível, tentando novamente...")
        time.sleep(5)
else:
    raise Exception("Não foi possível conectar ao Kafka após várias tentativas.")
producer_dlq = KafkaProducer(
    bootstrap_servers=os.getenv("KAFKA_BOOTSTRAP_SERVERS", "kafka:9092"),
    value_serializer=lambda v: json.dumps(v).encode("utf-8")
)

for message in consumer:
    try:
        data = message.value
        pdf_path = data["path"]
        pages = convert_from_path(pdf_path, dpi=300)
        text = ""
        for page in pages:
            text += pytesseract.image_to_string(page, lang="por+eng")
        # Salva no DB
        with engine.connect() as conn:
            conn.execute(jobs.insert().values(id=data["id"], filename=pdf_path, text=text))
        print(f"Processado: {data['id']}")
    except Exception as e:
        print(f"Erro ao processar {data['id']}: {e}")
        producer_dlq.send("pdf_dead_letter", value={"id": data.get("id"), "path": data.get("path"), "error": str(e)})

