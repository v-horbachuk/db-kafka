from db_connectors import mariadb

connection = mariadb()
cursor = connection.cursor()

sql_commands = ('CREATE TABLE IF NOT EXISTS alien_types ( \
                    id INT(11) AUTO_INCREMENT, \
                    alien_type VARCHAR(255) NOT NULL, \
                    PRIMARY KEY (id))',

            'CREATE TABLE IF NOT EXISTS colors ( \
                id INT(11) AUTO_INCREMENT, \
                color VARCHAR(255) NOT NULL, \
                PRIMARY KEY (id))',

            'CREATE TABLE IF NOT EXISTS aliens ( \
                id INT(11) AUTO_INCREMENT, \
                alien_name VARCHAR(255) NOT NULL, \
                alien_type_id INT(11) NOT NULL, \
                color_id INT(11) NOT NULL, \
                PRIMARY KEY (id), \
                FOREIGN KEY (alien_type_id) \
                    REFERENCES alien_types(id) \
                    ON DELETE CASCADE, \
                FOREIGN KEY (color_id) \
                    REFERENCES colors(id) \
                    ON DELETE CASCADE)ENGINE=INNODB',

            'CREATE TABLE IF NOT EXISTS names ( \
                id INT(11) AUTO_INCREMENT, \
                name VARCHAR(255) NOT NULL, \
                PRIMARY KEY (id))',

            'CREATE TABLE IF NOT EXISTS last_names ( \
                id INT(11) AUTO_INCREMENT, \
                last_name VARCHAR(255) NOT NULL, \
                PRIMARY KEY (id))',

            'CREATE TABLE IF NOT EXISTS witnesses ( \
                id INT(11) AUTO_INCREMENT, \
                name_id INTEGER NOT NULL, \
                last_name_id INTEGER NOT NULL, \
                witness_address VARCHAR(255) NOT NULL, \
                witness_age VARCHAR(255) NOT NULL, \
                PRIMARY KEY (id), \
                FOREIGN KEY (name_id) \
                    REFERENCES names(id) \
                    ON DELETE CASCADE, \
                FOREIGN KEY (last_name_id) \
                    REFERENCES last_names(id) \
                    ON DELETE CASCADE)',

            'CREATE TABLE IF NOT EXISTS places ( \
                id INT(11) AUTO_INCREMENT, \
                place VARCHAR(255) NOT NULL, \
                PRIMARY KEY (id))',

            'CREATE TABLE IF NOT EXISTS countries ( \
                id INT(11) AUTO_INCREMENT, \
                country VARCHAR(255) NOT NULL, \
                PRIMARY KEY (id))',

            'CREATE TABLE IF NOT EXISTS regions ( \
                id INT(11) AUTO_INCREMENT, \
                region VARCHAR(255) NOT NULL, \
                PRIMARY KEY (id))',

            'CREATE TABLE IF NOT EXISTS times_of_day ( \
                id INT(11) AUTO_INCREMENT, \
                time_of_day VARCHAR(255) NOT NULL, \
                PRIMARY KEY (id))',

            'CREATE TABLE IF NOT EXISTS locations ( \
                id INT(11) AUTO_INCREMENT, \
                lat DOUBLE, \
                lon DOUBLE, \
                place_id INTEGER NOT NULL, \
                country_id INTEGER NOT NULL, \
                region_id INTEGER NOT NULL, \
                PRIMARY KEY (id), \
                FOREIGN KEY (place_id) \
                    REFERENCES places(id) \
                    ON DELETE CASCADE, \
                FOREIGN KEY (country_id) \
                    REFERENCES countries(id) \
                    ON DELETE CASCADE,  \
                FOREIGN KEY (region_id) \
                    REFERENCES regions(id) \
                    ON DELETE CASCADE)',

            'CREATE TABLE IF NOT EXISTS aliens_witnesses_locations( \
                alien_id INTEGER NOT NULL, \
                witness_id INTEGER NOT NULL, \
                location_id INTEGER NOT NULL, \
                time_of_day_id INTEGER NOT NULL, \
                PRIMARY KEY (alien_id, witness_id, location_id, time_of_day_id), \
                FOREIGN KEY (alien_id) \
                    REFERENCES aliens(id) \
                    ON DELETE CASCADE, \
                FOREIGN KEY (witness_id) \
                    REFERENCES witnesses(id) \
                    ON DELETE CASCADE,  \
                FOREIGN KEY (location_id) \
                    REFERENCES locations(id) \
                    ON DELETE CASCADE, \
                FOREIGN KEY (time_of_day_id) \
                    REFERENCES times_of_day(id) \
                    ON DELETE CASCADE)'                        
)

for command in sql_commands:
    cursor.execute(command)

cursor.close()
connection.commit()