# Simple Queue with Producer and Consumer

this folder's content demonstrates a simple queue with one producer and one consumer

The producer is as name suggests produce messages and send them to queue named 'hello'

The consumer will process messages one by one from queue in order they are sent by producer.

In this demo producer will be sending messages that contains randomly generated characters in random intervals. In this example the message queue is not persistant so if you restart rabbitmq all unprocessed messages in the queue will be lost.


## How to run this example

First you need to create a images of both receiver and sender python runtimes.
> make build

After you created the images you can run:
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