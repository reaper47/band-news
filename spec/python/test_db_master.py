import sys
import os
dir = ''.join([os.path.dirname(__file__), '/../../src/api'])
sys.path.append(dir)
import db_master
import pytest

OPEN = 1
CLOSED = 0

class TestDbMaster(object):

    def setup(self):
        self.db = db_master.DbMaster()
        self.db_conn_status = self.db.open_connection()

        assert self.db_conn_status == OPEN

    def teardown(self):
        self.conn_status = self.db.close_connection()

        assert self.conn_status == CLOSED

