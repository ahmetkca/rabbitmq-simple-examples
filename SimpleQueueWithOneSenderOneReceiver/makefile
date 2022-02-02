build:
	docker build -t rabbitmq-tutorial1-python-sender:latest sender
	docker build -t rabbitmq-tutorial1-python-receiver:latest receiver

up:
	docker compose up -d --build

down:
	docker compose down

logs:
	docker compose logs -f

recompose: down up

recompose-build: down build up