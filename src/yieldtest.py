from collections import deque
import json

from kafka import KafkaProducer, KafkaConsumer
from anonymizer import Anonymizer

consumer = KafkaConsumer(bootstrap_servers="localhost:9092", value_deserializer=json.loads)
consumer.subscribe(["unanon"])
producer = KafkaProducer(bootstrap_servers="localhost:9092")


def anonymize(consumer):
    cache = deque()
    for msg in consumer:
        print(msg)
        cache.append(msg)
        if len(cache) > CACHE_SIZE:
            output = anonymizer.process([{**msg.value} for msg in cache])
            if isinstance(output, list):
                for _ in output:
                    yield _
            else:
                yield output


CACHE_SIZE = 5
anonymizer = Anonymizer({
    "drop": {"keys": ["something-unimportant"]},
    "mean": {"keys": ["some-number"]}
})

for anon_msg in anonymize(consumer):
    producer.send("anon", anon_msg.value if hasattr(anon_msg, "value") else str(anon_msg).encode())
