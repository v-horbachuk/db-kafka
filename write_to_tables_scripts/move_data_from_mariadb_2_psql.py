from db_connectors import postgres, mariadb
 
mdb_connection = mariadb()
mdb_cursor = mdb_connection.cursor()

pdb_conection = postgres()
pdb_cursor = pdb_conection.cursor()

# Write to "alien_types" table
mdb_cursor.execute('SELECT distinct alien_type FROM mysql.raw_input ORDER BY 1')
alien_types = mdb_cursor.fetchall()
for ttype in alien_types:
    pdb_cursor.execute('INSERT INTO alien_types(alien_type) VALUES(\'{}\')'.format(ttype[0]))

# Write to "colors" table
mdb_cursor.execute('SELECT distinct alien_color FROM mysql.raw_input ORDER BY 1')
alien_colors = mdb_cursor.fetchall()
for color in alien_colors:
    pdb_cursor.execute('INSERT INTO colors(color) VALUES(\'{}\')'.format(color[0]))

# Write to "witness_names" table
mdb_cursor.execute('SELECT distinct witness_name FROM mysql.raw_input ORDER BY 1')
witness_names = mdb_cursor.fetchall()
for name in witness_names:
    pdb_cursor.execute('INSERT INTO names(name) VALUES(\'{}\')'.format(name[0]))

# Write to "witness_last_names" table
mdb_cursor.execute('SELECT distinct witness_last_name FROM mysql.raw_input ORDER BY 1')
witness_last_names = mdb_cursor.fetchall()
for last_name in witness_last_names:
    pdb_cursor.execute('INSERT INTO last_names(last_name) VALUES(\'{}\')'.format(last_name[0]))

# Write to "places" table
mdb_cursor.execute('SELECT distinct place FROM mysql.raw_input ORDER BY 1')
places = mdb_cursor.fetchall()
for place in places:
    pdb_cursor.execute('INSERT INTO places(place) VALUES(\'{}\')'.format(place[0]))

# Write to "countries" table
mdb_cursor.execute('SELECT distinct country FROM mysql.raw_input ORDER BY 1')
countries = mdb_cursor.fetchall()
for country in countries:
    pdb_cursor.execute('INSERT INTO countries(country) VALUES(\'{}\')'.format(country[0]))

# Write to "region" table
mdb_cursor.execute('SELECT distinct region FROM mysql.raw_input ORDER BY 1')
regions = mdb_cursor.fetchall()
for region in regions:
    pdb_cursor.execute('INSERT INTO regions(region) VALUES(\'{}\')'.format(region[0]))

# Write to "times_of_day" table
mdb_cursor.execute('SELECT distinct time_of_day FROM mysql.raw_input ORDER BY 1')
times_of_day = mdb_cursor.fetchall()
for tod in times_of_day:
    pdb_cursor.execute('INSERT INTO times_of_day(time_of_day) VALUES(\'{}\')'.format(tod[0]))



# Write to "aliens" table
mdb_cursor.execute('SELECT distinct alien_id, alien_name, alien_type, alien_color FROM mysql.raw_input ORDER BY 1')
aliens = mdb_cursor.fetchall()

pdb_cursor.execute('SELECT * FROM alien_types')
pdb_alien_types = pdb_cursor.fetchall()

pdb_cursor.execute('SELECT * FROM colors')
pdb_colors = pdb_cursor.fetchall()

# Fetching corresponding ID's for alien type and color from "alien_types" and "colors" normalized tables
list_of_alien_type_ids = list()
list_of_alien_color_ids = list()
for row1 in aliens:
    for row2 in pdb_alien_types:
        if row1[2] == row2[1]:
            list_of_alien_type_ids.append(row2[0])
    for row3 in pdb_colors:
        if row1[3] == row3[1]:
            list_of_alien_color_ids.append(row3[0])

i = 0
for alien in aliens:
    pdb_cursor.execute('INSERT INTO aliens(alien_id, alien_name, alien_type_id, color_id) \
         VALUES(\'{}\', \'{}\', \'{}\', \'{}\')'.format(alien[0], alien[1], list_of_alien_type_ids[i], list_of_alien_color_ids[i]))
    i += 1



# Write to "witnesses" table
mdb_cursor.execute('SELECT distinct witness_id, witness_name, witness_last_name, witness_address, witness_age FROM mysql.raw_input ORDER BY 1')
witnesses = mdb_cursor.fetchall()

pdb_cursor.execute('SELECT * FROM names')
pdb_names = pdb_cursor.fetchall()

pdb_cursor.execute('SELECT * FROM last_names')
pdb_last_names = pdb_cursor.fetchall()

# Fetching corresponding ID's for witnesses name and last_name from "names" and "last_name" normalized tables
list_of_witness_name_ids = list()
list_of_witness_last_name_ids = list()
for row1 in witnesses:
    for row2 in pdb_names:
        if row1[1] == row2[1]:
            list_of_witness_name_ids.append(row2[0])
    for row3 in pdb_last_names:
        if row1[2] == row3[1]:
            list_of_witness_last_name_ids.append(row3[0])

i = 0
for witness in witnesses:
    pdb_cursor.execute('INSERT INTO witnesses(witness_id, name_id, last_name_id, witness_address, witness_age) \
         VALUES(\'{}\', \'{}\', \'{}\', \'{}\', \'{}\')'.format(witness[0], list_of_witness_name_ids[i], list_of_witness_last_name_ids[i], \
             witness[3], witness[4]))
    i += 1



# Write to "locations" table
mdb_cursor.execute('SELECT distinct location_id, lon, lat, place, country, region FROM mysql.raw_input ORDER BY 1')
locations = mdb_cursor.fetchall()

pdb_cursor.execute('SELECT * FROM places')
pdb_places = pdb_cursor.fetchall()

pdb_cursor.execute('SELECT * FROM countries')
pdb_countries = pdb_cursor.fetchall()

pdb_cursor.execute('SELECT * FROM regions')
pdb_regions = pdb_cursor.fetchall()

# Fetching corresponding ID's for witnesses name and last_name from "names" and "last_name" normalized tables
list_of_places_ids = list()
list_of_country_ids = list()
list_of_regions_ids = list()
# list_of_time_of_day_ids = list()
for row1 in locations:
    for row2 in pdb_places:
        if row1[3] == row2[1]:
            list_of_places_ids.append(row2[0])
    for row3 in pdb_countries:
        if row1[4] == row3[1]:
            list_of_country_ids.append(row3[0])
    for row4 in pdb_regions:
        if row1[5] == row4[1]:
            list_of_regions_ids.append(row4[0])

i = 0
for location in locations:
    pdb_cursor.execute('INSERT INTO locations(location_id, lon, lat, place_id, country_id, region_id) \
         VALUES(\'{}\', \'{}\', \'{}\', \'{}\', \'{}\', \'{}\')'.format(location[0], location[1], location[2], list_of_places_ids[i], \
             list_of_country_ids[i], list_of_regions_ids[i]))
    i += 1



# Write to final many-to-many table
mdb_cursor.execute('SELECT distinct alien_id, alien_name, alien_type, alien_color, \
    witness_id, witness_name, witness_last_name, witness_address, witness_age, \
    location_id, lon, lat, place, country, region, time_of_day FROM mysql.raw_input')
raw_data = mdb_cursor.fetchall()

pdb_cursor.execute('SELECT alien_id FROM aliens')
pdb_alien_ids = pdb_cursor.fetchall()

pdb_cursor.execute('SELECT witness_id FROM witnesses')
pdb_witness_ids = pdb_cursor.fetchall()

pdb_cursor.execute('SELECT location_id FROM locations')
pdb_location_ids = pdb_cursor.fetchall()

pdb_cursor.execute('SELECT * FROM times_of_day')
pdb_times_of_day = pdb_cursor.fetchall()

list_of_alien_ids = list()
list_of_witness_ids = list()
list_of_location_ids = list()
list_of_time_of_day_ids = list()
for row1 in raw_data:
    for row2 in pdb_alien_ids:
        if row1[0] == row2[0]:
            list_of_alien_ids.append(row2[0])
    for row3 in pdb_witness_ids:
        if row1[4] == row3[0]:
            list_of_witness_ids.append(row3[0])
    for row4 in pdb_location_ids:
        if row1[9] == row4[0]:
            list_of_location_ids.append(row4[0])
    for row5 in pdb_times_of_day:
        if row1[15] == row5[1]:
            list_of_time_of_day_ids.append(row5[0])        

i = 0
for row in raw_data:
    pdb_cursor.execute('INSERT INTO aliens_witnesses_locations(alien_id, witness_id, location_id, time_of_day_id) \
         VALUES(\'{}\', \'{}\', \'{}\', \'{}\')'.format(list_of_alien_ids[i], list_of_witness_ids[i], list_of_location_ids[i], list_of_time_of_day_ids[i]))
    i += 1

pdb_cursor.close()
pdb_conection.commit()
pdb_conection.close()