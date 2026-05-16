import json
import os
from kafka import KafkaConsumer, KafkaProducer
from sqlalchemy import create_engine, text
from pdf2image import convert_from_path
import pytesseract
from PIL import Image

# =========================
# CONFIGURAÇÕES
# =========================

KAFKA_BROKER = "kafka:9092"
TOPIC_NAME = "pdf_incoming"
DEAD_LETTER_TOPIC = "pdf_dead_letter"

POSTGRES_URL = os.getenv(
    "DATABASE_URL",
    "postgresql://postgres:postgres@postgres:5432/pdf_processor"
)

PDF_INPUT_DIR = "/data/incoming"

# =========================
# CONEXÃO POSTGRES
# =========================

engine = create_engine(POSTGRES_URL)

# =========================
# CRIA TABELA AUTOMATICAMENTE
# =========================

with engine.begin() as conn:
    conn.execute(text("""
        CREATE TABLE IF NOT EXISTS documentos (
            id SERIAL PRIMARY KEY,
            filename TEXT NOT NULL,
            texto_extraido TEXT NOT NULL,
            criado_em TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """))

print("✅ Tabela verificada/criada com sucesso")

# =========================
# CONSUMER KAFKA
# =========================

consumer = KafkaConsumer(
    TOPIC_NAME,
    bootstrap_servers=KAFKA_BROKER,
    auto_offset_reset="earliest",
    enable_auto_commit=True,
    group_id="pdf_group_v3",
    value_deserializer=lambda x: json.loads(x.decode("utf-8"))
)

# =========================
# PRODUCER PARA DEAD LETTER
# =========================

producer = KafkaProducer(
    bootstrap_servers=KAFKA_BROKER,
    value_serializer=lambda v: json.dumps(v).encode("utf-8")
)

print("🚀 Consumer iniciado e aguardando mensagens...")

# =========================
# PROCESSAMENTO
# =========================

for message in consumer:
    try:
        data = message.value

        filename = data["id"]
        filepath = data["path"]

        print(f"📄 Processando PDF: {filename}")

        # =========================
        # VERIFICA SE O PDF EXISTE
        # =========================

        if not os.path.exists(filepath):
            raise FileNotFoundError(f"Arquivo não encontrado: {filepath}")

        # =========================
        # CONVERTE PDF EM IMAGENS
        # =========================

        pages = convert_from_path(filepath)

        texto_final = ""

        # =========================
        # OCR EM CADA PÁGINA
        # =========================

        for i, page in enumerate(pages):
            print(f"🔍 OCR página {i + 1}")

            texto = pytesseract.image_to_string(page, lang="por")
            texto_final += texto + "\n"

        # =========================
        # SALVA NO BANCO
        # =========================

        with engine.begin() as conn:
            conn.execute(
                text("""
                    INSERT INTO documentos (filename, texto_extraido)
                    VALUES (:filename, :texto)
                """),
                {
                    "filename": filename,
                    "texto": texto_final
                }
            )

        print(f"✅ PDF processado com sucesso: {filename}")

    except Exception as e:
        print(f"❌ Erro ao processar arquivo: {e}")

        producer.send(
            DEAD_LETTER_TOPIC,
            {
                "erro": str(e),
                "mensagem_original": message.value
            }
        )

        producer.flush()