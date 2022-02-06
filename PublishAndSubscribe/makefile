build:
	docker build -t rabbitmq-pub-sub-python-publisher:latest publisher
	docker build -t rabbitmq-pub-sub-python-subscriber:latest subscriber

up:
	docker compose up -d --build

down:
	docker compose down

recompose: down up

recompose-build: down build up