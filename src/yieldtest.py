from kafka import KafkaProducer, KafkaConsumer
from collections import deque
from statistics import mean

consumer = KafkaConsumer(bootstrap_servers="localhost:9092")
consumer.subscribe(["unanon"])
producer = KafkaProducer(bootstrap_servers="localhost:9092")

def anonymize(consumer):
	cache = deque()
	for msg in consumer:
		value = str(msg.value)
		print("Caching " + value)
		cache.append(msg)
		if len(cache) > CACHE_SIZE:
			print("Yielding")
			output = process(cache)
			if isinstance(output, list):
				for _ in output:
					yield _
			else:
				yield output
			

def popmany(count, q):
	return [q.popleft() for i in range(count)]

CACHE_SIZE = 5
# process = lambda q: q.popleft()
# process = lambda q: mean([int(msg.value) for msg in q])
process = lambda q: popmany(3, q)


print("Beginning")
for anon_msg in anonymize(consumer):
	producer.send("anon", anon_msg.value if hasattr(anon_msg, "value") else str(anon_msg).encode())
