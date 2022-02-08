import pika, os, logging, time, random, string

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
console_handler = logging.StreamHandler()
logger.addHandler(console_handler)

logger.info(" - Connecting to the RabbitMQ Server... - ")
connection = pika.BlockingConnection(
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
channel = connection.channel()

logger.info(" - Declaring queue in channel with name 'hello' - ")
channel.queue_declare(queue='hello')


def get_random_message_body(length):
    letters_and_digits = string.ascii_letters + string.digits
    return ''.join((random.choice(letters_and_digits) for _ in range(length)))

interval = lambda : random.randint(1, 3)
logger.info(f" - Publish message to the queue 'hello' every {interval()} seconds - ")

while True:
    logger.info(" [*] Publising message to the queue 'hello' ")
    random_message_body = get_random_message_body(256)
    channel.basic_publish(
        exchange='',
        routing_key='hello',
        body=random_message_body)
    logger.info(f" [x] Sent '{random_message_body}' ")
    logger.info(f" [*] Waiting {interval()} seconds before sending another message to the queue 'hello' ")
    time.sleep(interval())
    



