# rabbitmq-simple-examples


> RabbitMQ is a message-queueing software also known as a message broker or queue manager. Simply said; it is software where queues are defined, to which applications connect in order to transfer a message or messages.
> --- <cite> www.cloudamqp.com </cite>

This repository will contain examples and demos for RabbitMQ. It will cover some fundamental topics such as simple message queues with one producer and one consumer, and then more advance work queues where you'll have multiple consumers which consumes work queue one at a time, so that no consumer will be assigned with more than one message before it acknowledges that it finished the currently processed message.
Additionally, it will cover Publisher/Subscriber pattern where you can send messages to more than one consumer (subscriber) at once as opposed to work queues where message is only consumed by one consumer at a time.


The tools that have been used in this repository are;
- Docker (Docker version 20.10.12, build e91ed57)
- Docker Compose (Docker Compose V2)
- Python (Python 3.9.9)
- RabbitMQ

##### Examples and Demos
- [Simple Queues Example with One Producer and One Consumer](SimpleQueueWithOneSenderOneReceiver)
- [Work (Task) Queues with Multiple Consumers](WorkQueuesWithMultipleConsumers)
- [Publisher/Subscriber](PublishAndSubscribe)
