import csv
from db_connectors import mariadb

def write_2_csv():
    connection = mariadb()
    cursor = connection.cursor()

    csv_data = csv.reader(open('big_alien_witness_data.csv'))
    next(csv_data)
    for row in csv_data:
        cursor.execute('INSERT INTO raw_input(alien_id, alien_name, alien_type, alien_color, \
            witness_id, witness_name, witness_last_name, witness_address, witness_age, \
            location_id, lat, lon, place, country, region, time_of_day)' + \
              'VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, \
                %s, %s, %s, %s, %s, %s)', tuple(row))

    connection.commit()
    cursor.close()
    print("Done")