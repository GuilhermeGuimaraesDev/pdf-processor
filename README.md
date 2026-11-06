# 📄 Processador de PDF Assíncrono com OCR e API

![Python](https://img.shields.io/badge/Python-3.10+-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-Async-green)
![Kafka](https://img.shields.io/badge/Kafka-Event%20Driven-black)
![Docker](https://img.shields.io/badge/Docker-Containerized-blue)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-Database-blue)

Sistema distribuído e assíncrono para processamento de PDFs com OCR, utilizando arquitetura orientada a eventos, mensageria com Kafka, validação de segurança dos arquivos e infraestrutura containerizada.

---

## 🎯 Objetivo

Desenvolver um sistema capaz de processar arquivos PDF de forma assíncrona, garantindo validações de segurança antes do processamento e permitindo a extração e armazenamento de informações.

O sistema realiza:

- Upload de arquivos via API.

- Validação de segurança dos arquivos recebidos.

- Processamento em background.

- Conversão de PDFs em imagens.

- Extração de texto utilizando OCR (Tesseract).

- Comunicação assíncrona através do Kafka.

- Armazenamento dos dados extraídos no PostgreSQL.

---

## 🚀 Tecnologias

- Python 3.10+ – Linguagem principal.

- FastAPI – Desenvolvimento da API REST.

- Kafka – Mensageria e processamento orientado a eventos.

- Zookeeper – Gerenciamento do Kafka.

- PostgreSQL – Banco de dados relacional.

- SQLAlchemy – ORM para interação com o banco.

- pdf2image – Conversão de PDFs em imagens.

- Poppler – Suporte à conversão de documentos PDF.

- Tesseract OCR – Extração de texto das imagens.

- Pillow – Manipulação de imagens.

- Docker / Docker Compose – Containerização e gerenciamento dos serviços.

---
Zookeeper – Gerenciamento do Kafka.

PostgreSQL – Banco de dados relacional.

SQLAlchemy – ORM para interação com o banco.

pdf2image – Conversão de PDFs em imagens.

Poppler – Suporte à conversão de documentos PDF.

Tesseract OCR – Extração de texto das imagens.

Pillow – Manipulação de imagens.

Docker / Docker Compose – Containerização e gerenciamento dos serviços.

---

🔐 Segurança e Validação de Arquivos

Verificações implementadas

- Hash SHA-256: geração de hash para identificação e integridade do arquivo.

- Tamanho do arquivo: limite máximo de 20 MB para evitar o recebimento de arquivos excessivamente grandes.

- Quantidade de páginas: análise do número de páginas para identificar documentos que possam exigir processamento elevado.

- PDF criptografado: identificação de documentos protegidos por senha ou criptografados.

- Metadados: análise das informações internas disponíveis no documento.

- Pontuação de risco: avaliação dos resultados das verificações para determinar se o arquivo pode ser aprovado ou rejeitado.

Processo de validação

O cliente envia um arquivo PDF através da API.

O sistema realiza as verificações de segurança.

Uma pontuação é calculada com base nas características identificadas.

Arquivos aprovados seguem para o Kafka.

Arquivos considerados suspeitos são rejeitados antes de entrar na fila de processamento.

A API também retorna informações sobre a análise realizada, incluindo aprovação, pontuação, motivo da decisão e verificações executadas.






## 🧱 Fluxo do Sistema

Cliente → API (FastAPI) → Validação de Segurança → Kafka → Consumer → Conversão PDF/Imagem → OCR → PostgreSQL
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
