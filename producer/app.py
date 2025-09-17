import os
import json
from kafka import KafkaProducer

# Função para publicar metadados do PDF
def publish_pdf_metadata(pdf_path):
    producer = KafkaProducer(
        bootstrap_servers=os.getenv("KAFKA_BOOTSTRAP_SERVERS", "kafka:9092"),
        value_serializer=lambda v: json.dumps(v).encode('utf-8')
    )
    msg = {"id": os.path.basename(pdf_path), "path": pdf_path}
    producer.send("pdf_incoming", value=msg)
    producer.flush()
    print(f"Publicado: {msg}")

def main():
    print("Consumer iniciado - pronto para ler mensagens do Kafka e salvar no banco")

if __name__ == "__main__":
    main()

