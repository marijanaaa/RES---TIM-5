from ConnectSQL import ConnectToMySQL

class Repository(ConnectToMySQL):

    def __init__(self):

        self.connection = ConnectToMySQL.CreateConnection(self)



    def doQuery(self,query):

        cur = self.connection.cursor()

        executedQuery = cur.execute(query)

        return executedQuery