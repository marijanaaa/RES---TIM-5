
class Repository:

    def __init__(self, connection):

        self.connection = connection.CreateConnection()



    def doQuery(self,query):

        cur = self.connection.cursor()

        executedQuery = cur.execute(query)

        return executedQuery