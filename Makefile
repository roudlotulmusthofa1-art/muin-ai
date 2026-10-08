.PHONY: help up down restart shell logs ps build

help:
	@echo "Muin AI - Docker Management Commands"
	@echo "-------------------------------------"
	@echo "make up        : Menjalankan semua container (backend, 9router, qdrant) di background"
	@echo "make down      : Menghentikan dan menghapus semua container"
	@echo "make restart   : Restart semua container"
	@echo "make shell     : Masuk ke dalam interactive shell container backend"
	@echo "make logs      : Melihat streaming log semua container"
	@echo "make ps        : Memeriksa status container yang sedang berjalan"
	@echo "make build     : Melakukan build ulang image container backend"

up:
	docker compose up -d

down:
	docker compose down

restart:
	docker compose restart

shell:
	docker compose exec backend /bin/bash || docker compose exec backend /bin/sh

logs:
	docker compose logs -f

ps:
	docker compose ps

build:
	docker compose build
