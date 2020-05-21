from confluent_kafka.avro import AvroConsumer
from confluent_kafka import avro

topic = "telegram_1"

schema_path = "/avro_schemas/telegram_channel_message_spam.avsc"

value_schema = avro.loads(open(schema_path).read())

avro_consumer = AvroConsumer({
    'bootstrap.servers': 'localhost:9092',
    'schema.registry.url': 'http://127.0.0.1:8081',
    'group.id': 'testomatiko_1',
    'auto.offset.reset': 'earliest'
}, reader_value_schema=value_schema)

avro_consumer.subscribe([topic])

while True:
    try:
        msg = avro_consumer.poll(1)

        # There were no messages on the queue, continue polling
        if msg is None:
            continue

        if msg.error():
            print("Consumer error: {}".format(msg.error()))
            continue

        record = msg.value()
        print('RECEIVED RECORD: ', record)

    except KeyboardInterrupt:
        avro_consumer.close()
        break

print("Shutting down consumer..")
