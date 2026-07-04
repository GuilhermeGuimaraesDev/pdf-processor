# 📄 Processador de PDF Assíncrono com OCR e API

![Python](https://img.shields.io/badge/Python-3.10+-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-Async-green)
![Kafka](https://img.shields.io/badge/Kafka-Event%20Driven-black)
![Docker](https://img.shields.io/badge/Docker-Containerized-blue)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-Database-blue)

Sistema distribuído e assíncrono para processamento de PDFs com OCR, utilizando arquitetura orientada a eventos, mensageria com Kafka e infraestrutura containerizada.

---

## 🎯 Objetivo

Processar arquivos PDF de forma assíncrona, realizando:

- Upload via API
- Processamento em background
- Conversão de PDF em imagens
- Extração de texto com OCR (Tesseract)
- Salvamento dos dados em banco de dados

---

## 🚀 Tecnologias

- Python 3.10+
- FastAPI
- Kafka
- Zookeeper
- PostgreSQL
- SQLAlchemy
- pdf2image
- Tesseract OCR
- Docker / Docker Compose

---

## 🧱 Fluxo do Sistema

Cliente → API (FastAPI) → Kafka → Consumer → OCR → PostgreSQL

---

## ⚙️ Como executar

```bash
git clone https://github.com/seu-usuario/pdf-processor.git
cd pdf-processor
docker compose up --build
```

👤 Autor

Guilherme Guimarães Paiva

GitHub: https://github.com/GuilhermeGuimaraesDev

LinkedIn: https://www.linkedin.com/in/guilherme-guimaraes-paiva
