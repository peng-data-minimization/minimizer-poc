# Use Case

## Title
Think in paper titles:

`Plug and Play data minimization for streaming fitness tracking data`

`Data Minimization in ETL streaming processes`

`Real time data minimization for fitness tracking data`

Implementations for:
- Kafka using the Consumer/Producer API
- Spark using the Spark Streaming API 

## Privacy Principle


## State of scientific discussions 


## Implementation / Ideas
- Breakdown of data minimization principles 
- Conceptualization of generic python libraries that implement these principles
- Implementation of these libraries in the concrete context of Apache Spark and Apache Kafka 
- The user should be able to (dynamically) parametrize the use of the libraries (switch functionality on and off / 
set different thresholds, ...)
- The library should be able to handle different types of input data
    - Kafka: json, avro
    - Spark: `.FIT`, `.TCX` files streamed from HDFS or S3, or RDD streams. See also [the spark documentation]
    (https://spark.apache.org/docs/2.2.0/streaming-programming-guide.html#basic-sources).  

## Disclaimer
In recent times traditional ETL Pipelines, processing data in big batches, have experienced a shift towards processing
data on the fly, in near real-time, as it moves through the system so to say. Processing data in streams instead of
big chunks is becoming more and more popular as the necessity for fast availability of processed data increases and 
frameworks and tools are getting more and more powerful.


Apache Spark has been and still is at the core of a vast amount of ETL processes consuming and processing ever 
larger amounts of data. Most often seen in combination with Hadoop, it has proven itself to be a heavily reliable 
and performing data processing engine. Its Streaming API allows to perform streaming analytics based on its powerful
core engine.

Apache Kafka has seen a major hype in the industry in recent years as it has proven to be capable of handling vast
amounts of messages across large clusters. Kafka has been designed as a distributed streaming platform that comes with 
durable storage capabilities which makes it not only interesting for moving data from a to b but also to be used in 
contexts of analytics pipelines and ETL jobs. Its Connect API allows quick integration into a wide range of systems.

The aim of this project is to build a solution to enable data minimization principles for fitness tracking data on 
both of these platforms. 
The result will be a set of python libraries that can be implemented in a plug and play fashion to allow the user to 
incorporate the chosen principles into his data processing pipelines.


