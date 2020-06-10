## Start Zookeeper & Kafka

From kafka.apache.org/quickstart

```sh
bin/zookeeper-server-start.sh config/zookeeper.properties
bin/kafka-server-start.sh config/server.properties
```

## Start Anonymizer

```sh
python3 yieldtest.py
```

## Start Consumer & Producer
```powershell
bin/kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic anon
1..10 | Foreach-Object {sleep 3; return $_} | bin/kafka-console-producer.sh --bootstrap-server localhost:9092 --topic unanon
```