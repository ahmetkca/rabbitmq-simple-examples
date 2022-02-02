import pika, os, logging, time, random

from utils import produce_blocking_message

FROM_TASK_ID = int(os.environ.get("FROM_TASK_ID", 0))
TO_TASK_ID = int(os.environ.get("TO_TASK_ID", 50))

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
console_handler = logging.StreamHandler()
logger.addHandler(console_handler)

logger.info(" ... PRODUCER ... ")
logger.info(" - Connecting to the RabbitMQ Server... - ")
connection = pika.BlockingConnection(
    pika.ConnectionParameters(
        host='rabbitmq-srv',
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


queue_name = 'task_queue'
logger.info(f" - Declaring queue in channel with name '{queue_name}' - ")
channel.queue_declare(queue=queue_name, durable=True)

interval = lambda : random.randint(1, 2)

task_id = FROM_TASK_ID
while task_id <= TO_TASK_ID:
    logger.info(f" [*] Publising message to the queue '{queue_name}' ")
    blocking_message_body = produce_blocking_message(str(task_id))
    channel.basic_publish(
        exchange='',
        routing_key=queue_name,
        body=blocking_message_body,
        properties=pika.BasicProperties(
            delivery_mode= pika.spec.PERSISTENT_DELIVERY_MODE
        )
    )
    logger.info(f" [x] Sent '{blocking_message_body}' ")
    logger.info(f" [*] Waiting {interval()} seconds before sending another message to the queue '{queue_name}' \n")
    time.sleep(interval())
    task_id += 1

connection.close()
    



