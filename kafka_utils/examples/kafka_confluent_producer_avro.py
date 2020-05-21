from confluent_kafka import avro
from confluent_kafka.avro import AvroProducer
import time
import random

# this implementation uses the confluent kafka library
# docs: https://docs.confluent.io/current/clients/confluent-kafka-python/

# this producer sends avro messages to a topic

topic = "pg_sink_test"

schema_path = "/avro_schemas/pg_sink_test_schema.avsc"

value_schema = avro.loads(open(schema_path).read())
avro_prodcuer = AvroProducer({
    'bootstrap.servers': 'localhost:9092',
    'schema.registry.url': 'http://127.0.0.1:8081'
}, default_value_schema=value_schema)
num = 1
while True:
    # pass a dictionary and the encoder object to the writer
    num = num + (random.randint(80, 150) / 100)

    data = {"timestamp": int(time.time() * 1000), "value1": num, "value2": random.randint(0, 1000)}
    avro_prodcuer.produce(topic=topic, value=data)

    print("Sent ", data)
    time.sleep(0.5)
    avro_prodcuer.flush()
