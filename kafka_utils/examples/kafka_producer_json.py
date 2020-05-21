from json import dumps
from time import sleep
from kafka import KafkaProducer

# this implementation uses the kafka-python library.
# docs: https://kafka-python.readthedocs.io/en/master/

#this producer sends json messages to a topic
producer = KafkaProducer(bootstrap_servers=['localhost:9092'],
                         value_serializer=lambda x: dumps(x).encode('utf-8'))
for e in range(1000):
    data = {'number' : e}
    producer.send('testomatiko', value=data)
    print('sent')
    sleep(1)


