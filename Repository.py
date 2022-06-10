import MySQLdb
import socket
from ConnectSQL import ConnectToMySQL
import json

def openConnection(repository):
    serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    serverSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    serverSocket.bind(('localhost', 10004))
    serverSocket.listen(1)
    while(1):
        clientConnection, addr = serverSocket.accept()
        data=clientConnection.recv(1024)
        if not data:
            break

        response=repository.doQuery(data.decode("utf-8"))

        json_string = json.dumps(response)

        clientConnection.sendall(bytes(json_string,encoding="utf-8"))
        clientConnection.close()
    serverSocket.close()

class Repository:
    def __init__(self):
        self.connection = ConnectToMySQL()

    def doQuery(self,query):
        #cursor = self.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor=self.connection.CreateConnection().cursor()
        
        try:
            cursor.execute(query)
            data=cursor.fetchall()

            dict = {
                "status_code":2000,
                "status":"SUCCESS",
                "payload":data,
            }
            return dict
        except (MySQLdb.Error,MySQLdb.Warning) as warning:
            statusCode = 3000
            status = "REJECTED"
            if(warning.args[0] == 1064):
                statusCode = 5000
                status = "BAD_FORMAT"
            
            dict = {
                "status_code":statusCode,
                "status":status,
                "payload":warning.args[1],
            }
            return dict

if __name__ == '__main__': 
    repository=Repository()
    openConnection(repository)