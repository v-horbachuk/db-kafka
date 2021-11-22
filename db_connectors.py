import MySQLdb
import psycopg2


def mariadb():
    connection = MySQLdb.connect(host='0.0.0.0',
        port=3366,
        user='root',
        passwd='1234',
        db='mysql')
    return connection

def postgres():
    connection = psycopg2.connect(host = "localhost",
        port = "5533",
        database = "postgres",
        user = "postgres",
        password = "1234"
    )
    return connection