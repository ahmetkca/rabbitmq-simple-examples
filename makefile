build:
	docker build -t rabbitmq-tutorial1-python-sender:latest tutorial1/sender
	docker build -t rabbitmq-tutorial1-python-receiver:latest tutorial1/receiver

up:
	docker compose up -d --build

down:
	docker compose down

recompose: down up

recompose-build: down build up