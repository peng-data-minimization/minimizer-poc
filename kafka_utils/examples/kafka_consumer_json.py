from kafka import KafkaConsumer
import json

# this implementation uses the kafka-python library.
# docs: https://kafka-python.readthedocs.io/en/master/


# To consume latest messages and auto-commit offsets
TOPIC = 'testomatiko'

def json_deserializer(message):
    print("hello")
    print(message)
    # return json.loads(message.decode('utf-8'))


consumer = KafkaConsumer(TOPIC,
                         bootstrap_servers=['localhost:9092'],
                         auto_offset_reset='earliest', enable_auto_commit=False,
                         value_deserializer=json_deserializer
                         )

while True:
    while True:
        msg_pack = consumer.poll(timeout_ms=500)
        for tp, messages in msg_pack.items():
            for message in messages:
                print(f"{tp.topic}:{tp.partition}:{message.offset}: key={message.offset} value={message.value}")
