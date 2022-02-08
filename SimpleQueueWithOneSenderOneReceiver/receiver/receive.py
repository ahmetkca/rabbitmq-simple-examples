import pika, sys, os, logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
console_handler = logging.StreamHandler()
logger.addHandler(console_handler)

def main():
    logger.info(" - Connecting to the RabbitMQ Server... - ")
    connecion = pika.BlockingConnection(
        pika.ConnectionParameters(
            host=os.environ.get('RABBITMQ_HOST', 'rabbitmq-srv'),
            connection_attempts=5,
            retry_delay=5,
            credentials=pika.PlainCredentials(
                username=os.environ.get('RABBITMQ_USER'), 
                password=os.environ.get('RABBITMQ_PASSWORD')
            )
        )
    )
    logger.info(" - Creating channel... - ")
    channel = connecion.channel()

    logger.info(" - Declaring queue in channel with name 'hello' - ")
    channel.queue_declare(queue='hello')

    def callback(ch , method, properties, body):
        logger.info(properties)
        logger.info(f" [x] Received {body}")
        ch.basic_ack(delivery_tag=method.delivery_tag)

    logger.info(" - Consume messages from queue 'hello' - ")
    channel.basic_consume(
        queue='hello',
        on_message_callback=callback)
    
    logger.info(" [*] Waiting for messages. To exit press CTRL+C")
    channel.start_consuming()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        logger.info("Interrupted")
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)