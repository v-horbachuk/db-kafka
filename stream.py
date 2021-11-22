import json
import sys
from db_connectors import postgres, mariadb
from write_to_tables_scripts.mdb_writer import write_to_mdb
from kafka import KafkaProducer, KafkaConsumer, KafkaAdminClient, admin, TopicPartition

table_names = ["alien_types", "colors", "names", "last_names", "places", "countries", "regions", \
    "time_of_day", "aliens", "witnesses", "locations", "aliens_witnesses_locations"]

usage_messages = ["usage: Please provide one of the following table names: \n \
        alien_types\n \
        colors\n \
        names\n \
        last_names\n \
        places\n \
        countries\n \
        regions\n \
        time_of_day\n \
        aliens \n \
        witnesses\n \
        locations \n \
        aliens_witnesses_locations",

        "usage: Only one table name is allowed"
]

if len(sys.argv) == 1:
    print (usage_messages[0])
    exit(1)   
elif len(sys.argv) > 2:
    print (usage_messages[1])
    exit (1)

if sys.argv[1] not in table_names:
    print(usage_messages[0])

topic = sys.argv[1]

# Postgress connection
pdb_connection = postgres()
pdb_cursor = pdb_connection.cursor()

# MariaDB connection
mdb_connection = mariadb()
mdb_cursor = mdb_connection.cursor()

# Create Consumer and Produser
consumer = KafkaConsumer(bootstrap_servers='localhost:9092', group_id='kafka_comsumers', value_deserializer=lambda value: json.loads(value.decode("utf-8")))
producer = KafkaProducer(bootstrap_servers='localhost:9092', value_serializer=lambda value: json.dumps(value).encode('utf-8'), batch_size=3355443)

# Check if topic exists and create one if not
cluster_topics = consumer.topics()
if topic not in cluster_topics:
    client = KafkaAdminClient(bootstrap_servers='localhost:9092')
    new_topic = admin.NewTopic(name=topic, num_partitions=1, replication_factor=1)
    client.create_topics([new_topic])
    client.close()

# Get data from table 
pdb_cursor.execute('SELECT * FROM {}'.format(topic))
messages = pdb_cursor.fetchall()

# Stream data to Kafka standalone
for msg in messages:
    producer.send(topic=topic, value=msg)
producer.flush()

# Get messages by Consumer and stop listening to Kafka
top_part = TopicPartition(topic,0)
consumer.assign([top_part])
consumer.seek_to_beginning(top_part)  
last_offset = consumer.end_offsets([top_part])[top_part]

for message in consumer:
    write_to_mdb(topic, message.value)
    if message.offset == last_offset - 1:
        break