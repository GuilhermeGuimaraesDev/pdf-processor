# 📄 Processador de PDF Assíncrono com OCR e API

![Python](https://img.shields.io/badge/Python-3.10+-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-Async-green)
![Kafka](https://img.shields.io/badge/Kafka-Event%20Driven-black)
![Docker](https://img.shields.io/badge/Docker-Containerized-blue)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-Database-blue)

Sistema distribuído e assíncrono para processamento de PDFs com OCR, utilizando arquitetura orientada a eventos, mensageria com Kafka e infraestrutura containerizada.

---

## 🎯 Objetivo

Construir um pipeline distribuído capaz de:

- Receber PDFs via API REST
- Processar arquivos de forma assíncrona e escalável
- Converter PDF em imagens
- Extrair texto com OCR (Tesseract)
- Persistir dados estruturados em PostgreSQL
- Desacoplar serviços usando Kafka
- Garantir tolerância a falhas com Dead Letter Queue (DLQ)

---

## 🧱 Arquitetura do Sistema

```text
                ┌──────────────┐
                │   Cliente    │
                └──────┬───────┘
                       │
                       ▼
            ┌────────────────────┐
            │   FastAPI API      │
            │ (Upload de PDF)    │
            └────────┬───────────┘
                     │
                     ▼
            ┌────────────────────┐
            │ Kafka (topic)      │
            │ pdf_incoming       │
            └────────┬───────────┘
                     │
                     ▼
            ┌────────────────────┐
            │ Consumer Worker    │
            │ (Assíncrono)       │
            └────────┬───────────┘
                     │
     ┌───────────────┼────────────────┐
     ▼               ▼                ▼
PDF → Images     OCR Engine     DLQ (Falhas)
(pdf2image)      (Tesseract)

                     │
                     ▼
            ┌────────────────────┐
            │ PostgreSQL         │
            │ Persistência       │
            └────────────────────┘



🔄 Fluxo de Processamento
Upload do PDF via API
API salva arquivo localmente
Publicação de metadados no Kafka
Consumer consome mensagem de forma assíncrona
PDF convertido em imagens (pdf2image + Poppler)
OCR executado página por página (Tesseract)
Texto estruturado salvo no PostgreSQL
Falhas são enviadas para DLQ
📡 Endpoints da API
📤 Upload de PDF

POST /upload

📊 Status do processamento (em desenvolvimento)

GET /status/{job_id}

📄 Resultado do processamento (em desenvolvimento)

GET /result/{job_id}

🚀 Tecnologias Utilizadas
Backend
Python 3.10+
FastAPI
Uvicorn
Mensageria
Apache Kafka
Zookeeper
Banco de Dados
PostgreSQL
SQLAlchemy
OCR & Processamento
pdf2image
Poppler
Tesseract OCR
Pillow
Infraestrutura
Docker
Docker Compose
🔑 Funcionalidades
✅ Implementadas
Upload de PDFs via API
Pipeline Kafka funcional
Consumer assíncrono
Conversão PDF → imagem
OCR automático
Persistência no PostgreSQL
DLQ (tratamento de falhas)
Ambiente completo via Docker
🚧 Em desenvolvimento
Job ID único por processamento
Consulta de status
Consulta de resultado
Monitoramento e métricas
Testes automatizados
🧠 Decisões de Arquitetura
🔹 Kafka como mensageria

Escolhido para desacoplar API e processamento, permitindo escalabilidade horizontal.

🔹 Processamento assíncrono

Evita bloqueio da API e permite processamento de múltiplos PDFs simultaneamente.

🔹 OCR via Tesseract

Solução open-source robusta para extração de texto de imagens.

🔹 Docker Compose

Permite replicação do ambiente completo localmente com um comando.

🔹 DLQ (Dead Letter Queue)

Garante resiliência e rastreabilidade de falhas no pipeline.

⚙️ Como executar o projeto
git clone https://github.com/seu-usuario/pdf-processor.git
cd pdf-processor
docker compose up --build
📦 Serviços
Serviço	Porta
FastAPI	8000
Kafka	9092
PostgreSQL	5432
Zookeeper	2181
📂 Estrutura do Projeto
pdf-processor/
│
├── api/
├── producer/
├── consumer/
├── infra/
├── data/
│   ├── incoming/
│   └── processed/
│
├── docker-compose.yml
└── README.md
📌 Status do Projeto

🚧 Pipeline funcional ponta a ponta

O sistema já executa:

Recebimento de PDFs
Processamento assíncrono via Kafka
OCR automático
Persistência no banco de dados
✍️ Autor

Guilherme Guimarães Paiva

GitHub: GuilhermeGuimaraesDev
LinkedIn: Perfil LinkedIn
