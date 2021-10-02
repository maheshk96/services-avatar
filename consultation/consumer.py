import pika, json

from main import Consultation,User, db
params = pika.URLParameters('amqps://meiozege:n3veFiC_O8waZbEG0GVXXr1D6s9hRCLa@vulture.rmq.cloudamqp.com/meiozege')

connection = pika.BlockingConnection(params)

channel = connection.channel()

channel.queue_declare(queue='consultation')

def callback(ch,method,properties,body):
    print("Received in consultation")
    data = json.loads(body)
    print(data)

    if properties.content_type == 'consult_created':
        consults = Consultation(id=data['id'], doctor=data['doctor'], appointment=data['appointment'], type=data['type'])
        db.session.add(consults)
        db.session.commit()
        print('Consult Created')

    elif properties.content_type == 'consult_updated':
        consults = Consultation.query.get(data['id'])
        consults.doctor = data['doctor']
        consults.type = data['type']
        db.session.commit()
        print('Consult Updated')

    elif properties.content_type == 'consult_deleted':
        consults = Consultation.query.get(data)
        db.session.delete(consults)
        db.session.commit()
        print('Consult Deleted')


channel.basic_consume(queue='consultation',on_message_callback=callback, auto_ack=True)

print('Started Consuming')

channel.start_consuming()

channel.close()