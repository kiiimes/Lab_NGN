#! /usr/bin/env python

import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('210.107.212.93'))
channel = connection.channel()

channel.queue_declare(queue='hello')

channel.basic_publish(exchange='',
                      routing_key='hello',
                      body='Hello World!')
print(" [x] Sent 'Hello World!'")

connection.close()
