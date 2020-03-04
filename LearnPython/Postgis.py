
# start and then connect:
# https://hub.docker.com/r/mdillon/postgis/
# 1. sudo docker run --name amit -e POSTGRES_USER='postgres' -e POSTGRES_PASSWORD=docker -d -p 5432:5432 mdillon/postgis
# 2. docker run -it --link amit:postgres --rm postgres \sh -c 'exec psql -h "$POSTGRES_PORT_5432_TCP_ADDR" -p "$POSTGRES_PORT_5432_TCP_PORT" -U postgres'

from DBManagerInterface import DBManagerInterface
import psycopg2


class DataBaseManagerWithGeo(DBManagerInterface):

    def __init__(self, table_name):
        self.table_name = table_name
        self.conn = psycopg2.connect(user='postgres', password='docker', host='127.0.0.1', port='5432')
        print("DB Connected OK")
        self.cursor = self.conn.cursor()

    def create_new_data_base(self, db_name):
        sqlCreateDatabase = "create database " + db_name + ";"
        self.cursor.execute(sqlCreateDatabase)
        self.conn.commit()

    def drop_table(self):
        self.cursor.execute("DROP TABLE IF EXISTS %s;" % self.table_name)
        self.conn.commit()

    def print_table(self):
        sql = '''SELECT FIRST_NAME, ST_Area(LOCATION) AS Area FROM ''' + self.table_name
        self.cursor.execute(sql)
        content = self.cursor.fetchall()
        for row in content:
            print(row)

    def create_table(self):
        sql = '''CREATE TABLE ''' + self.table_name + '''(
         FIRST_NAME CHAR(20) NOT NULL,
         LAST_NAME CHAR(20),
         AGE INT,
         SEX CHAR(6),
         INCOME FLOAT,
         LOCATION geometry
      )'''
        self.cursor.execute(sql)
        self.conn.commit()


    def add_emloyee(self, name, last, age, sex, income, location):

        locationString = "POLYGON(("+location+"))"
        sql = '''INSERT INTO ''' + self.table_name + '''(FIRST_NAME,LAST_NAME, AGE,SEX,INCOME,LOCATION)
            VALUES (%s, %s, %s, %s, %s, %s)'''
        self.cursor.execute(sql, (name, last, age, sex, income,locationString))

        self.conn.commit()
        print("Add Succssfully")
        self.print_table()

    def check_if_area_interset(self):
        None

    def get_number_of_records(self):
        sql = '''SELECT COUNT(*)
         FROM ''' + self.table_name
        self.cursor.execute(sql)
        num_of_emplyees = self.cursor.fetchall()
        return num_of_emplyees

    def randomString(stringLength=10):
        import random
        import string
        letters = string.ascii_lowercase
        return ''.join(random.choice(letters) for i in range(stringLength))

    def close_db(self):
        self.cursor.close()
