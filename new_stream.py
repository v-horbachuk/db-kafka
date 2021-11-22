import json
import sys
from db_connectors import mariadb
# from write_to_tables_scripts.mdb_writer import write_to_mdb
from kafka import KafkaProducer, KafkaConsumer, KafkaAdminClient, admin, TopicPartition

# MariaDB connection
mdb_connection = mariadb()
mdb_cursor = mdb_connection.cursor()

# Create Consumer and Produser
consumer = KafkaConsumer(bootstrap_servers='localhost:9092', group_id='kafka_comsumers', value_deserializer=lambda value: json.loads(value.decode("utf-8")))
producer = KafkaProducer(bootstrap_servers='localhost:9092', value_serializer=lambda value: json.dumps(value).encode('utf-8'))

# Get data from table
# mdb_cursor.execute('SELECT DISTINCT witness_name, witness_last_name, witness_age FROM raw_input WHERE time_of_day="day" AND alien_name="c/\\0H"')
# messages = mdb_cursor.fetchall()
# # Stream data to Kafka standalone
# for msg in messages:
#     producer.send(topic=topic, value=msg)
# producer.flush()

mdb_cursor.execute('SELECT DISTINCT witness_address FROM raw_input WHERE time_of_day="night" AND alien_color!="yellow"')
messages = mdb_cursor.fetchall()
# Stream data to Kafka standalone
# producer.send(topic='notyellow', value='aaaaaa')
# for msg in messages:
#     # print(msg)
#     producer.send(topic='slon', value=msg)
# producer.flush()


# # Get messages by Consumer and stop listening to Kafka
top_part = TopicPartition('notyellow',0)
consumer.assign([top_part])
consumer.seek_to_beginning(top_part)  
last_offset = consumer.end_offsets([top_part])[top_part]
print(last_offset)

# for message in consumer:
#     # write_to_mdb(topic, message.value)
#     print(message.value)
#     if message.offset == last_offset - 1:
#         break