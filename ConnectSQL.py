from __future__ import print_function
from inspect import _Object
import MySQLdb
class ConnectToMySQL:
    def __init__(self):
        self.hostname = 'localhost'
        self.username = 'marijana'
        self.password = 'hejhej1'
        self.database = 'bp1'

    def CreateConnection(self):
        return MySQLdb.connect( host=self.hostname, user=self.username, passwd=self.password, db=self.database )




