import pika
import enum
import os

class RabbitMQ:
    class ExchangeTypes(enum.Enum):
        FANOUT = 'fanout'

def main():
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(
            host=os.environ.get("RABBITMQ_HOST", 'rabbitmq_srv'),
            credentials=pika.PlainCredentials(
                username=os.environ.get('RABBITMQ_USER', 'dev_user'),
                password=os.environ.get('RABBITMQ_PASSWORD', 'pa55w0rd'),
            ),
            connection_attempts=10,
            retry_delay=5,
        )
    )
    channel = connection.channel()

    exchange_name = 'logs'
    # Declare exchange with fanout type which will basically broadcast
    # all the messages it receives to all the queues it knows
    channel.exchange_declare(
        exchange=exchange_name,
        exchange_type=RabbitMQ.ExchangeTypes.FANOUT
    )

    # We will have to create a temporary queue for this subcriber.
    # Since we want our subscribers to get the same messages,
    # it is going to be a fresh, empty queue everytime we connect to rabbitmq
    create_random_queue_result = channel.queue_declare(queue='')
    # empty queue name indicates that rabbitmq will auto-generate a queue name for us.
    queue_name = create_random_queue_result.method.queue

    # After we created the queue we are going to need to bind the queue 
    # to the exchange we created earlier 'logs'
    channel.queue_bind(exchange='logs', queue=queue_name)
    # this is important because this is how the exchange knows about queues.

    print(" [*] Waiting for logs. To exit press CTRL+C ")

    def callback(ch, method, properties, body):
        print(f" [x] Received {body}")
        print(f" [x] Sorted message body {sorted(body.decode())}\n{'-'*15}\n")

    channel.basic_consume(
        queue=queue_name,
        on_message_callback=callback,
        auto_ack=True
    )

    channel.start_consuming()



if __name__ == "__main__":
    main()

                    