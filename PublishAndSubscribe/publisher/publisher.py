import time
import random
import pika, os, sys
import enum
from utils import get_random_message

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

    interval = lambda : random.random()
    
    i = os.environ.get('from_num', 0)
    while i <= os.environ.get('to_num', 500):
        slp_tm = interval()
        message = f"[message-{i}] : " + get_random_message(16)
        
        print(f" [x] created a random message {message}")
        channel.basic_publish(
            exchange=exchange_name,
            routing_key='',
            body=message
        )
        print(f" [x] Sent {message}")
        print(f" [*] Waiting for {slp_tm}s")
        time.sleep(interval())
        i+=1

if __name__ == "__main__":
    main()
    print(" PUBLISHER EXITED WITH 0 ")
    sys.exit(0)