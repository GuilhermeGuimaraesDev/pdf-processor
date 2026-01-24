📄 Processador de PDF Assíncrono com OCR e API

🎯 Objetivo
Construir um pipeline assíncrono e escalável para processamento de PDFs,
com extração de texto via OCR, utilizando arquitetura baseada em eventos.

🚀 Tecnologias
- **Backend**: Python 3.10+, FastAPI, Uvicorn
- **Mensageria**: Kafka, Zookeeper
- **Banco de Dados**: PostgreSQL, SQLAlchemy
- **OCR & PDF**: pdf2image, Poppler, Tesseract OCR
- **Infraestrutura**: Docker, Docker Compose
- **Versionamento**: Git

🧱 Arquitetura

1. API recebe o upload do PDF
2. Metadados do arquivo são publicados no Kafka
3. Consumer processa o PDF de forma assíncrona
4. Texto extraído via OCR é salvo no PostgreSQL
5. API permite consultar status e resultado do processamento


🔑 Funcionalidades (em desenvolvimento)
- [X] Upload de PDFs via API (FastAPI)
- [X] Publicação de metadados no Kafka
- [X] Consumo de mensagens Kafka (consumer conectado)
- [ ] Conversão PDF → imagens (pdf2image)
- [ ] Extração de texto via Tesseract OCR
- [ ] Persistência do texto no PostgreSQL
- [ ] Endpoint de consulta de status e resultado 

⚙️ Como rodar (Em desenvolvimento)
git clone https://github.com/seu-usuario/pdf-processor.git
cd pdf-processor
docker compose up --build

📌 Status
🚧 Projeto em desenvolvimento 🚧
Pipeline Kafka funcional, ajustes finais no consumer e OCR em andamento.

✍️ Autor
Guilherme Guimarães Paiva  
[LinkedIn](https://www.linkedin.com/in/guilherme-guimarães-paiva-82633b20a) | 
[GitHub](https://github.com/GuilhermeGuimaraesDev)

