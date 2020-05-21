from confluent_kafka.avro import AvroConsumer, AvroProducer
from confluent_kafka import avro
import configparser
import os

CONFIG_PATH = ''


def do_something_fancy(text):
    return text


if __name__ == '__main__':
    # Config
    config = configparser.ConfigParser()
    config.read(CONFIG_PATH)
    twitter_config = config['twitter']
    twitter_sent_config = config['twitter_sent']
    kafka_config = config['kafka']

    # Kafka consumers and prodcuers
    source_schema = avro.loads(
        open(os.path.join(kafka_config['schema_folder'], twitter_sent_config['source_schema'])).read())
    consumer = AvroConsumer({
        'bootstrap.servers': kafka_config['bootstrap_url'],
        'schema.registry.url': kafka_config['schema_registry_url'],
        'group.id': twitter_sent_config['group_id']
    }, reader_value_schema=source_schema)
    consumer.subscribe([twitter_sent_config['source_topic']])

    target_schema = avro.loads(
        open(os.path.join(kafka_config['schema_folder'], twitter_sent_config['target_schema'])).read())

    producer = AvroProducer({
        'bootstrap.servers': kafka_config['bootstrap_url'],
        'schema.registry.url': kafka_config['schema_registry_url']
    }, default_value_schema=target_schema)
    target_topic = twitter_sent_config['target_topic']

    while True:
        try:
            msg = consumer.poll(1)

            # There were no messages on the queue, continue polling
            if msg is None:
                continue

            if msg.error():
                print("Consumer error: {}".format(msg.error()))
                continue

            record = msg.value()
            text = record["text"]

            data = do_something_fancy(text)

            producer.produce(topic=target_topic, value=data)
            print('Processed Tweet Data sent: ', data)
            # check https://github.com/confluentinc/confluent-kafka-python/issues/16 in case of full buffer issue
            producer.flush()

        except KeyboardInterrupt:
            consumer.close()
            break
