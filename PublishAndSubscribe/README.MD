# Publisher/Subscriber

this folder's content demonstrates simple publisher/subscriber pattern

The main difference in this example is that we started to use exchange. In fact, we were actually using them in previous 2 examples but we didn't explicitly declare one. Empty exchange name indicates the default exchange. In this example we created a exchange with name 'logs' type fanout.
In fanout the exchange will broadcast all the published messages to all the queues it knows. And for each subscriber, we created fresh, empty queue with auto-generated name (id). Each subscriber consumes the same messages at the same time since they all have their own queues.

Publisher publishes messages in random interval to the exchange named 'logs' it doesn't even know about the queues, the exchange will act as a gateway between queues and publisher.

Subscriber 1 is using stdout to print to console

Subscriber 2 is directly outputing into subscriber/logs/logs_from_subscriber.log file

![Publisher/Subscriber](/PublishAndSubscribe/FanoutPublisherSubscriber.png)
<p align="center">
    <a href="/PublishAndSubscribe/FanoutPublisherSubscriber.png">Publisher/Subscriber diagram</a></p>

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

---
In this example Multi-staged dockerfile has been used and build time was much faster.
