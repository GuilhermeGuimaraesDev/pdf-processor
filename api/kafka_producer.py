import os, json
from kafka import KafkaProducer

import time
from kafka import KafkaProducer, errors

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
