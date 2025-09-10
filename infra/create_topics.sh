#!/bin/bash
# Script para criar tópicos no Kafka

docker exec -it pdf-processor-kafka-1 kafka-topics --create --topic pdf_incoming --bootstrap-server localhost:9092 --partitions 1 --replication-factor 1
docker exec -it pdf-processor-kafka-1 kafka-topics --create --topic pdf_text --bootstrap-server localhost:9092 --partitions 1 --replication-factor 1
