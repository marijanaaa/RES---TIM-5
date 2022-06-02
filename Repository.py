from email import message
import MySQLdb
class Repository:
    def __init__(self, connection):
        self.connection = connection.CreateConnection()

    def doQuery(self,query):
        cursor = self.connection.cursor()
        try:
            cursor.execute(query)
            data=cursor.fetchall()
            return [2000, data]
        except (MySQLdb.Error,MySQLdb.Warning) as warning:
            return [3000, warning.args[1]]