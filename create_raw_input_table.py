from db_connectors import mariadb

def create_raw_input():
    connection = mariadb()
    cursor = connection.cursor()
    
    cursor.execute('CREATE TABLE IF NOT EXISTS raw_input (alien_id INT(10), \
        alien_name VARCHAR(255), \
        alien_type VARCHAR(255), \
        alien_color VARCHAR(255), \
        witness_id INT(10), \
        witness_name VARCHAR(255), \
        witness_last_name VARCHAR(255), \
        witness_address VARCHAR(255), \
        witness_age INT(10), \
        location_id INT(10), \
        lat DOUBLE(10,6), \
        lon DOUBLE(10,6), \
        place VARCHAR(255), \
        country VARCHAR(255), \
        region VARCHAR(255), \
        time_of_day VARCHAR(255))')
    
    connection.commit()
    cursor.close()

create_raw_input()