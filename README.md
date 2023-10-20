# Confluent Kafka Data Ingestion and MongoDB Storage Application

## Overview

This application is designed to showcase a data pipeline that leverages Apache Kafka for data ingestion and MongoDB Atlas for data storage. It provides a practical example of how to use Kafka as a messaging system to collect data from various sources, and then efficiently store that data in a MongoDB database hosted on MongoDB Atlas.

## Features

- Data Ingestion: The application reads data from a sample file, simulating data ingestion from an external source. Kafka is used to publish this data as messages to a Kafka topic.

- Kafka Integration: It includes a Kafka producer component that produces data to a Kafka topic, which serves as the central message bus.

- Data Consumption: A Kafka consumer component reads data from the Kafka topic, simulating data consumption by your application.

- MongoDB Storage: The consumed data is stored in MongoDB Atlas, a cloud-based MongoDB database service, allowing for scalable and reliable data storage.

## Prerequisites
Before running the application, make sure you have the following prerequisites in place:

- Create a free account on [Confluent](https://confluent.cloud/).
    - Create environment
    - Create api keys
    - Create topic
    - Create Stream Governance API
    - Create Stream Governance Credentials

- Create a free account in [MongoDB Atlas](https://cloud.mongodb.com)
    - Create Collection
    - Create Database
    - Get MongoDB URL
Note : you can also install mongodb in local and connect to MongoDB

- Create environment and install required packages

    -  Create a conda environment
    ```
    conda create -p venv python==3.8 -y
    ```

    - Activate conda environment
    ```
    conda activate venv/
    ```

    - Install required packages
    ```
    pip install -r requirements.txt
    ```

## Getting Started

1. Configuration: Update the Confluent Kafka and MongoDB connection details in the application configuration.

2. Running the Producer: Execute the Kafka producer component to start ingesting data and publishing it to the Kafka topic.
```
python producer_main.py
```

3. Running the Consumer: Execute the Kafka consumer component to consume data from the Kafka topic and store it in MongoDB Atlas.
```
python consumer_main.py
```

## Usage

This application is intended for educational and demonstration purposes, providing a foundation for understanding how Confluent Kafka can be integrated with MongoDB Atlas for data processing and storage.



