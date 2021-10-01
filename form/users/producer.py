import pika, json

params = pika.URLParameters('amqps://meiozege:n3veFiC_O8waZbEG0GVXXr1D6s9hRCLa@vulture.rmq.cloudamqp.com/meiozege')

connection = pika.BlockingConnection(params)

channel = connection.channel()


def publish(method, body):
    properties = pika.BasicProperties(method)
    channel.basic_publish(exchange='', routing_key='appointment', body=json.dumps(body), properties=properties)