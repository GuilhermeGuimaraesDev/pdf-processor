#!/bin/bash
# Script para criar tópicos no Kafka

docker exec kafka kafka-topics.sh --create --topic pdf_incoming --bootstrap-server kafka:9092 --partitions 1 --replication-factor 1
docker exec kafka kafka-topics.sh --create --topic pdf_text --bootstrap-server kafka:9092 --partitions 1 --replication-factor 1
docker exec kafka kafka-topics.sh --create --topic pdf_dead_letter --bootstrap-server kafka:9092 --partitions 1 --replication-factor 1
