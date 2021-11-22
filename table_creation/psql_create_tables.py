from db_connectors import postgres

connection = postgres()
cursor = connection.cursor()

sql_commands = (
    'CREATE TABLE IF NOT EXISTS alien_types ( \
        alien_type_id SERIAL, \
        alien_type VARCHAR(255) NOT NULL, \
        PRIMARY KEY (alien_type_id))',
    
    'CREATE TABLE IF NOT EXISTS colors ( \
        color_id SERIAL, \
        color VARCHAR(255) NOT NULL, \
        PRIMARY KEY (color_id))',

    'CREATE TABLE IF NOT EXISTS aliens ( \
        alien_id SERIAL, \
        alien_name VARCHAR(255) NOT NULL, \
        alien_type_id INTEGER NOT NULL, \
        color_id INTEGER NOT NULL, \
        PRIMARY KEY (alien_id), \
        CONSTRAINT fk_alien_type \
            FOREIGN KEY (alien_type_id) \
                REFERENCES alien_types(alien_type_id) \
                ON DELETE CASCADE, \
        CONSTRAINT fk_color \
            FOREIGN KEY (color_id) \
                REFERENCES colors(color_id) \
                ON DELETE CASCADE)',

    'CREATE TABLE IF NOT EXISTS names ( \
        name_id SERIAL, \
        name VARCHAR(255) NOT NULL, \
        PRIMARY KEY (name_id))',

    'CREATE TABLE IF NOT EXISTS last_names ( \
        last_name_id SERIAL, \
        last_name VARCHAR(255) NOT NULL, \
        PRIMARY KEY (last_name_id))',

    'CREATE TABLE IF NOT EXISTS witnesses ( \
        witness_id SERIAL, \
        name_id INTEGER NOT NULL, \
        last_name_id INTEGER NOT NULL, \
        witness_address VARCHAR(255) NOT NULL, \
        witness_age VARCHAR(255) NOT NULL, \
        PRIMARY KEY (witness_id), \
        CONSTRAINT fk_name \
            FOREIGN KEY (name_id) \
                REFERENCES names(name_id) \
                ON DELETE CASCADE, \
        CONSTRAINT fk_last_name \
            FOREIGN KEY (last_name_id) \
                REFERENCES last_names(last_name_id) \
                ON DELETE CASCADE)',

    'CREATE TABLE IF NOT EXISTS places ( \
        place_id SERIAL, \
        place VARCHAR(255) NOT NULL, \
        PRIMARY KEY (place_id))',

    'CREATE TABLE IF NOT EXISTS countries ( \
        country_id SERIAL, \
        country VARCHAR(255) NOT NULL, \
        PRIMARY KEY (country_id))',

    'CREATE TABLE IF NOT EXISTS regions ( \
        region_id SERIAL, \
        region VARCHAR(255) NOT NULL, \
        PRIMARY KEY (region_id))',

    'CREATE TABLE IF NOT EXISTS times_of_day ( \
        time_of_day_id SERIAL, \
        time_of_day VARCHAR(255) NOT NULL, \
        PRIMARY KEY (time_of_day_id))',

    'CREATE TABLE IF NOT EXISTS locations ( \
        location_id SERIAL, \
        lat DOUBLE PRECISION, \
        lon DOUBLE PRECISION, \
        place_id INTEGER NOT NULL, \
        country_id INTEGER NOT NULL, \
        region_id INTEGER NOT NULL, \
        PRIMARY KEY (location_id), \
        CONSTRAINT fk_place \
            FOREIGN KEY (place_id) \
                REFERENCES places(place_id) \
                ON DELETE CASCADE, \
        CONSTRAINT fk_country \
            FOREIGN KEY (country_id) \
                REFERENCES countries(country_id) \
                ON DELETE CASCADE,  \
        CONSTRAINT fk_region \
            FOREIGN KEY (region_id) \
                REFERENCES regions(region_id) \
                ON DELETE CASCADE)', 
        
    'CREATE TABLE IF NOT EXISTS aliens_witnesses_locations( \
        alien_id INTEGER NOT NULL, \
        witness_id INTEGER NOT NULL, \
        location_id INTEGER NOT NULL, \
        time_of_day_id INTEGER NOT NULL, \
        PRIMARY KEY (alien_id, witness_id, location_id, time_of_day_id), \
        FOREIGN KEY (alien_id) \
            REFERENCES aliens(alien_id) \
            ON DELETE CASCADE, \
        FOREIGN KEY (witness_id) \
            REFERENCES witnesses(witness_id) \
            ON DELETE CASCADE,  \
        FOREIGN KEY (location_id) \
            REFERENCES locations(location_id) \
            ON DELETE CASCADE, \
        FOREIGN KEY (time_of_day_id) \
            REFERENCES times_of_day(time_of_day_id) \
            ON DELETE CASCADE)'     
)

for command in sql_commands:
    cursor.execute(command)

cursor.close()
connection.commit()