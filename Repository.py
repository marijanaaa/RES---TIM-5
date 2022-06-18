import MySQLdb
import socket
from ConnectSQL import ConnectToMySQL
import pickle
def open_connection(repository):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind(('localhost', 10004))
    server_socket.listen(1)
    while(1):
        client_connection, addr = server_socket.accept()
        data=client_connection.recv(1024)
        if not data:
            break

        response=repository.do_query(data.decode("utf-8"))

        data = pickle.dumps(response)
        client_connection.sendall(data)
        client_connection.close()
    server_socket.close()

class Repository:
    def __init__(self):
        self.connection = ConnectToMySQL()

    def do_query(self,query):
        #cursor = self.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor=self.connection.create_connection().cursor()
        
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
            status_code = 3000
            status = "REJECTED"
            if(warning.args[0] == 1064):
                status_code = 5000
                status = "BAD_FORMAT"
            
            dict = {
                "status_code":status_code,
                "status":status,
                "payload":warning.args[1],
            }
            return dict

if __name__ == '__main__': 
    repository=Repository()
    open_connection(repository)