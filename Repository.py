class Repository:

    def __init__(self, connection):

        self.connection = connection.CreateConnection()



    def doQuery(self,query):

        cur = self.connection.cursor()

        cur.execute(query)

        list = cur.fatchall()

        return list