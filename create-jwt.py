#!/usr/bin/env python

import jwt
from datetime import datetime, timedelta
import pika

private_key = ""

with open("rabbit-private.pem", 'r') as private_key_f:
    private_key = private_key_f.read()

token_dict = {
"scope":  "my_rabbit_server.write:ps-push/ps-push-test-exchange/perfsonar.raw.*",
"exp": datetime.utcnow()+timedelta(hours=12),
"iat": datetime.utcnow(),
"sub": "derek-test",
"aud": "my_rabbit_server",
"sub": "ps-push-test",
"client_id": "ps-push-test"
}

header_dict = {
"kid": "pf-key"
}



encoded = jwt.encode(token_dict, private_key, algorithm='RS256', headers=header_dict)
print(encoded.decode('utf-8'))
import sys
sys.exit(0)

# The rest of this file is just to test the rabbitmq connection.
# The sys.exit(0) line above assures that this will not be executed

# Setup the pika connection
#url = 'amqps://guest:{}@clever-turkey.rmq.cloudamqp.com/ps-push'.format(encoded.decode('utf-8'))
#print(url)
#parameters = pika.URLParameters(url)

credentials = pika.PlainCredentials('derek', encoded.decode('utf-8'))
parameters = pika.ConnectionParameters('clever-turkey.rmq.cloudamqp.com', 5672, 'ps-push', credentials)
connection = pika.BlockingConnection(parameters)

channel = connection.channel()

channel.basic_publish('ps-push-test-exchange',
                      'perfsonar.raw.test',
                      'Message Body Test',
                      pika.BasicProperties(content_type='text/plain',
                                           delivery_mode=1))

connection.close()

