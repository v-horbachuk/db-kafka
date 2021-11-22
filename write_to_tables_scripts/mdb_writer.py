from db_connectors import mariadb

def write_to_mdb(topic, msg):
    connection = mariadb()
    mdb_cursor = connection.cursor()

    if topic == "alien_types":
        mdb_cursor.execute('INSERT INTO alien_types(id, alien_type) VALUES(\'{}\', \'{}\')'.format(msg[0], msg[1]))
    elif topic == "colors":
        mdb_cursor.execute('INSERT INTO colors(id, color) VALUES(\'{}\', \'{}\')'.format(msg[0], msg[1]))
    elif topic == "names":
        mdb_cursor.execute('INSERT INTO names(id, name) VALUES(\'{}\', \'{}\')'.format(msg[0], msg[1]))
    elif topic == "last_names":
        mdb_cursor.execute('INSERT INTO last_names(id, last_name) VALUES(\'{}\', \'{}\')'.format(msg[0], msg[1]))
    elif topic == "places":
        mdb_cursor.execute('INSERT INTO places(id, place) VALUES(\'{}\', \'{}\')'.format(msg[0], msg[1]))
    elif topic == "countries":
        mdb_cursor.execute('INSERT INTO countries(id, country) VALUES(\'{}\', \'{}\')'.format(msg[0], msg[1]))
    elif topic == "regions":
        mdb_cursor.execute('INSERT INTO regions(id, region) VALUES(\'{}\', \'{}\')'.format(msg[0], msg[1]))
    elif topic == "times_of_day":
        mdb_cursor.execute('INSERT INTO times_of_day(id, time_of_day) VALUES(\'{}\', \'{}\')'.format(msg[0], msg[1]))
    elif topic == "aliens":
        mdb_cursor.execute('INSERT INTO aliens(id, alien_name, alien_type_id, color_id) \
         VALUES(\'{}\', \'{}\', \'{}\', \'{}\')'.format(msg[0], msg[1], msg[2], msg[3]))
    elif topic == "witnesses":
        mdb_cursor.execute('INSERT INTO witnesses(id, name_id, last_name_id, witness_address, witness_age) \
         VALUES(\'{}\', \'{}\', \'{}\', \'{}\', \'{}\')'.format(msg[0], msg[1], msg[2], msg[3], msg[4]))
    elif topic == "locations":
        mdb_cursor.execute('INSERT INTO locations(id, lon, lat, place_id, country_id, region_id) \
         VALUES(\'{}\', \'{}\', \'{}\', \'{}\', \'{}\', \'{}\')'.format(msg[0], msg[1], msg[2], msg[3], msg[4], msg[5]))
    elif topic == "aliens_witnesses_locations":
        mdb_cursor.execute('INSERT INTO aliens_witnesses_locations(alien_id, witness_id, location_id, time_of_day_id) \
         VALUES(\'{}\', \'{}\', \'{}\', \'{}\')'.format(msg[0], msg[1], msg[2], msg[3]))

    mdb_cursor.close()
    connection.commit()