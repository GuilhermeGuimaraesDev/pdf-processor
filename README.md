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
