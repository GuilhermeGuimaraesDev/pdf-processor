import os
import json
import time
from kafka import KafkaProducer, errors

BOOTSTRAP = os.getenv("KAFKA_BOOTSTRAP_SERVERS", "kafka:9092")
TOPIC = os.getenv("KAFKA_TOPIC_INCOMING", "pdf_incoming")

producer = None


def get_producer():
    global producer
    if producer:
        return producer

    for i in range(10):
        try:
            producer = KafkaProducer(
                bootstrap_servers=BOOTSTRAP,
                value_serializer=lambda v: json.dumps(v).encode("utf-8"),
            )
            print("✅ Conectado ao Kafka")
            return producer
        except errors.NoBrokersAvailable:
            print("⏳ Kafka não disponível, tentando novamente...")
            time.sleep(5)

    raise RuntimeError("❌ Não foi possível conectar ao Kafka")


def publish_pdf_metadata(pdf_path: str):
    prod = get_producer()

    msg = {
        "id": os.path.basename(pdf_path),
        "path": pdf_path,
    }

    prod.send(TOPIC, value=msg)
    prod.flush()
    print(f"[API] Publicado no Kafka: {msg}")
