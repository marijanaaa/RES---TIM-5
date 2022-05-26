from email import message
import MySQLdb
class Repository:
    def __init__(self, connection):
        self.connection = connection.CreateConnection()

    def doQuery(self,query):
        cur = self.connection.cursor()
        try:
            cur.execute(query)
            list=cur.fetchall()
            return [2000, list]
        except (MySQLdb.Error,MySQLdb.Warning) as e:
            return [3000, e.args[1]]