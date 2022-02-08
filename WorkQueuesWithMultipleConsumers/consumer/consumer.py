import pika, sys, os, logging, time

MY_CONSUMER_ID = os.environ.get("MY_CONSUMER_ID")

logger = logging.getLogger(__name__ + f" MY_CONSUMER_ID={MY_CONSUMER_ID}")
logger.setLevel(logging.INFO)
console_handler = logging.StreamHandler()
logger.addHandler(console_handler)

def main():
    logger.info(f" ... CONSUMER-{MY_CONSUMER_ID} ... ")
    logger.info(" - Connecting to the RabbitMQ Server... - ")
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(
            host=os.environ.get('RABBITMQ_HOST', 'rabbitmq-srv'),
            connection_attempts=5,
            retry_delay=5,
            credentials=pika.PlainCredentials(
                username=os.environ.get('RABBITMQ_USER', 'dev_user'), 
                password=os.environ.get('RABBITMQ_PASSWORD', 'pa55w0rd')
            )
        )
    )
    logger.info(" - Creating channel... - ")
    channel = connection.channel()

    queue_name = "task_queue"
    logger.info(f" - Declaring queue in channel with name '{queue_name}' - ")
    channel.queue_declare(queue=queue_name, durable=True)


    def callback(ch , method, properties, body):
        logger.info(f"\n [x] Received {body.decode()}, will sleep for {body.count(b'.')}s")
        time.sleep(body.count(b'.'))
        logger.info(f" [x] Done, slept for {body.count(b'.')}s \n")
        ch.basic_ack(delivery_tag = method.delivery_tag)

    # the rabbitmq will not give more than one message to a worker at a time.
    # basically the rabbitmq will not dispatch a new message to a worker until it has processed and acknowledged
    # the previous one. Instead, it will dispatch the next message in the queue to the next worker that is not busy.
    # So that the workers (consumers) will not be overwhelmed with more than one message
    # at a time. 
    channel.basic_qos(prefetch_count=1)

    logger.info(f" - Consume messages from queue '{queue_name}' - ")
    channel.basic_consume(
        queue=queue_name,
        on_message_callback=callback
    )
    
    logger.info(" [*] Waiting for messages. To exit press CTRL+C")
    channel.start_consuming()

def debug_messages():
    pass

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        logger.info("Interrupted")
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)


    