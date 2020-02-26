# docker run --rm  --name pg-docker -e POSTGRES_PASSWORD=docker -d -p 5432:5432 -v $HOME/Amit/docker/postgres:/var/lib/postgresql/data  postgres

# psql -h localhost -U postgres -d postgres

from DBManagerInterface import DBManagerInterface
import psycopg2


class DataBaseManager(DBManagerInterface):

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
        sql = '''SELECT * FROM ''' + self.table_name
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
         INCOME FLOAT
      )'''
        self.cursor.execute(sql)
        self.conn.commit()

    def add_emloyee(self, name, last, age, sex, income):
        sql = '''INSERT INTO ''' + self.table_name + '''(FIRST_NAME,LAST_NAME, AGE,SEX,INCOME)
            VALUES (%s, %s, %s, %s, %s)'''
        self.cursor.execute(sql, (name, last, age, sex, income))
        self.conn.commit()
        print("Add Succssfully")

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

    # def create_and_run_thread_pool(cur, table_name):
    #     from random import randint
    #     from concurrent.futures import ThreadPoolExecutor
    #
    #     with ThreadPoolExecutor(max_workers=4) as e:
    #         for i in range(10):
    #             e.submit(add_emloyee(cur, table_name, randomString(10), randomString(10), randint(0, 100), "M",
    #                                  randint(0, 10000)))
    #
    # def sleep_in_sec(sleep_time):
    #     import time
    #     time.sleep(sleep_time)

    def close_db(self):
        self.cursor.close()


# def main():
    # conn = psycopg2.connect(user='postgres', password='docker', host='127.0.0.1', port='5432')
    # cursor = conn.cursor()
    # table_name = "EMPLOYEE"
    # drop_table(cursor, table_name)
    # create_table(cursor, table_name)
    # # add_emloyee(cursor, table_name, "amit", "liron", 36, 'M', 1000)
    # # add_emloyee(cursor, table_name, "sivan", "liron", 32, 'F', 500)
    # #create_and_run_thread_pool(cursor, table_name)
    # #sleep_in_sec(1)
    # print("Num Of Employess in DB: ", get_number_of_records(cursor, table_name))
    # conn.close()
    # print("\nFinished")

