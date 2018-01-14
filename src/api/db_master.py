import MySQLdb as mariadb
import sys
import os
dir = ''.join([os.path.dirname(__file__), '/fb'])
sys.path.append(dir)
import auth
import geocoder_helpers


class DbMaster(object):

    def __init__(self):
        self.__credentionals = auth.get_db_config(auth.VARIABLES_PATH)

    def open_connection(self):
        user = self.__credentionals['user']
        password = self.__credentionals['password']
        database = self.__credentionals['database']
        host = self.__credentionals['host']

        self.conn = mariadb.connect(
            user=user,
            password=password, 
            database=database,
            host=host)

        self.cursor = self.conn.cursor()
        
        return self.conn.open
        
    def close_connection(self):
        self.cursor.close()
        self.conn.close()

        return self.conn.open

    def push_countries_to_db(self):
        countries = geocoder_helpers.fetch_countries_for_db()

        add_country = ("INSERT INTO countries "
                    "(numeric_id, alpha_2, name) "
                    "VALUES (%s, %s, %s)")

        for country in countries:
            self.cursor.execute(add_country, country)

        self.conn.commit()

    #https://dev.mysql.com/doc/refman/5.7/en/example-auto-increment.html

