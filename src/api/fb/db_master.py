import MySQLdb as mariadb
import sys
import os
sys.path.append(os.getcwd())
import auth


class DbMaster(object):

    def __init__(self):
        self.__credentionals = auth.get_db_config(auth.VARIABLES_PATH)

    def connect_to_database(self):
        user = self.__credentionals['user']
        password = self.__credentionals['password']
        database = self.__credentionals['database']
        host = self.__credentionals['host']

        self.conn = mariadb.connect(
            user=user,
            password=password, 
            database=database,
            host=host
        )
        
        return self.conn.open
        
    def close_connection(self):
        self.conn.close()

        return self.conn.open          

