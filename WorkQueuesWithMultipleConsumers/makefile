build:
	docker build -t rabbitmq-work-queues-python-producer:latest producer
	docker build -t rabbitmq-work-queues-python-consumer:latest consumer

up:
	docker compose up -d --build

down:
	docker compose down

recompose: down up

recompose-build: down build up