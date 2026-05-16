FROM python:3.10-slim

# =========================
# DEPENDÊNCIAS DO SISTEMA
# =========================
RUN apt-get update && apt-get install -y \
    tesseract-ocr \
    tesseract-ocr-por \
    poppler-utils \
    wget \
    netcat-openbsd \
    && rm -rf /var/lib/apt/lists/*

# =========================
# DIRETÓRIO DA APLICAÇÃO
# =========================
WORKDIR /app

# =========================
# INSTALA DEPENDÊNCIAS PYTHON
# =========================
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# =========================
# COPIA OS ARQUIVOS
# =========================
COPY . .

# =========================
# INSTALA DOCKERIZE
# =========================
RUN wget https://github.com/jwilder/dockerize/releases/download/v0.6.1/dockerize-linux-amd64-v0.6.1.tar.gz \
    && tar -C /usr/local/bin -xzvf dockerize-linux-amd64-v0.6.1.tar.gz \
    && rm dockerize-linux-amd64-v0.6.1.tar.gz

# =========================
# INICIALIZAÇÃO
# =========================
CMD ["dockerize", \
     "-wait", "tcp://kafka:9092", \
     "-wait", "tcp://postgres:5432", \
     "-timeout", "60s", \
     "--", \
     "python", "-u", "app.py"]