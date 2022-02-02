## Work Queues with Multiple Consumers

This folder's content demonstrates work queues with multiple consumers.

Basically you have one producer who produce a message with random amount of dots at the end.

The message content is TASK-{task_id}{random amount of dots} 
ex. TASK-139.... which indicates sleep time of 4 seconds.

The consumers who are listening on queue named task_queue will process messages one at a time.

In order to fake long tasks, consumers will sleep for an amount of dot that has been counted in the message content.

No consumer will receive more than one message at a time. So if one consumer processed a message with 10 dots, it will sleep for 10 seconds. In the mean time, the other consumer can process other messages in the queue with 2, 3, 4, 1 dots respectively which means the consumer B will be finished processing four messages in total while consumer A was processing one message.

In this demo producer will produce the messages in random intervals. Two consumers will process each messages from queue one at a time.
The queue in this example is persistance, so any unprocessed message in the queue will not be lost if the rabbitmq unexpectadly shutsdown.
And the connected workers (consumers) will receive unprocessed old messages while producer will be publishing new messages to the queue.
The consumers will eventually get to new messages in the queue.

## How to run this example

The environment variables you can change in the docker-compose.yml files are;
    - FROM_TASK_ID      (start of the task id range ex. 150)
    - TO_TASK_ID        (end of the task id range ex. 175)
    - MY_CONSUMER_ID    (name of each workers (consumers) ex. A, B, C)


First you need to create a images of both receiver and sender python runtimes.
> make build

After you created the images you can start the program:
> make up

And in order to stop the whole program, you can run:
> make down


If you want to restart the program:
> make recompose


If you change the source code of either reciever or sender
you have to create images again, so I added a shortcut for that:
> make recompose-build

this will basically shutdowns all the containers, builds the all required images and starts containers again.

You can check the output of the program by running:
> make logs

---
RabbitMQ dashboard url is `localhost:15672` user is `dev_user` and password is `pa55w0rd`