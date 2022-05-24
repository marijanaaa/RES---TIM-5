import MySQLdb
class ConnectToMySQL:
    def __init__(self):
        self.hostname = 'localhost'
        self.username = 'root'
        self.password = 'hejhej1'
        self.database = 'bolnica'

    def CreateConnection(self):
        return MySQLdb.connect( host=self.hostname, user=self.username, passwd=self.password, db=self.database )




