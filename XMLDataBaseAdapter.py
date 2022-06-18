import xml.etree.ElementTree as xmlCreate
from bs4 import BeautifulSoup
import socket
import pickle
import xmltodict

def open_connection(xml_database_adapter):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind(('127.0.0.1', 10003))
    server_socket.listen(1)
    while(1):
        client_connection, addr = server_socket.accept();
        data=client_connection.recv(1024);
        if not data:
            break
        response=xml_database_adapter.get_response(data.decode("utf-8"))
        client_connection.sendall(bytes(response,encoding="utf-8"))
    client_connection.close()
    server_socket.close()

class XMLDateBaseAdapter:

    def get_method(self, xml_obj):
        data = BeautifulSoup(xml_obj, 'xml') 
        data = data.find("data")
        noun_tag = data.find("noun")
        noun = noun_tag.text
        fields_tag = data.find("fields")
        sql_query = "SELECT "

        if (fields_tag is None):
            sql_query+="*"
        else:
            fields = fields_tag.text
            fields_array = fields.split(";")
            for x in fields_array:
                sql_query += x + ","
            sql_query = sql_query[:-1]

        where_tag = data.find("query")
        sql_query += " from " + noun

        if (where_tag is not None):
            where = where_tag.text
            where_array = where.split(";")
            sql_query += " where "
            for x in where_array:
                 sql_query += x + " and "
            sql_query = sql_query[:-4]

        sql_query += "; commit;"
        return sql_query

    def delete_method(self, xml_obj):
        data = BeautifulSoup(xml_obj, 'xml') 
        data = data.find("data")
        noun_tag = data.find("noun")  
        noun = noun_tag.text 
        sql_query = "DELETE FROM " + noun
        where_tag = data.find("query")  

        if where_tag is not None:
            sql_query += " WHERE "
            where = where_tag.text
            where_array = where.split(";")
            for x in where_array:
                sql_query += x + " and "
            sql_query = sql_query[:-4]

        sql_query += "; commit;"

        return sql_query

    def insert_method(self, xml_obj):
        data = BeautifulSoup(xml_obj, 'xml') 
        data = data.find("data")
        noun_tag = data.find("noun")
        noun = noun_tag.text
        sql_query = "INSERT INTO " + noun + " VALUES ( "
        where_tag = data.find("query")
        where = where_tag.text
        where_array = where.split(";")

        for x in where_array:
            niz = x.split("=")
            sql_query += niz[1] + ", "

        sql_query = sql_query[:-2]
        sql_query += "); commit;"

        return sql_query

    def update_method(self, xml_obj):
        data = BeautifulSoup(xml_obj, 'xml') 
        data = data.find("data")
        noun_tag = data.find("noun")
        noun = noun_tag.text
        query_tag = data.find('query')
        set = query_tag.text
        set_array = set.split(";")
        sql_query = "UPDATE " + noun + " SET "

        for x in set_array:
                sql_query += x + ","

        sql_query = sql_query[:-1]
        where_tag=data.find('fields')
        where=where_tag.text
        sql_query +=" WHERE " + where + "; commit;"

        return sql_query
        
    def from_xml_to_sql(self, xml_obj):        
        data = BeautifulSoup(xml_obj, 'xml') 
        data = data.find("data")
        method_tag = data.find("verb")
        method = method_tag.text

        if method == "GET":
            result = self.get_method(xml_obj)
        elif method == "DELETE":
            result = self.delete_method(xml_obj)
        elif method == "POST":
            result = self.insert_method(xml_obj)
        elif method == "PATCH":
            result = self.update_method(xml_obj)

        return result

    def get_response(self, xml_obj):
        result = self.from_xml_to_sql(xml_obj)
        data = self.connect_to_repository(result)
        
        object = pickle.loads(data)
        my_dict ={
            "data": object,
        }

        return xmltodict.unparse(my_dict)
        
    def connect_to_repository(self, result):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect(('localhost', 10004))
        s.sendall(bytes(result, "utf-8"))
        data = s.recv(1024)

        s.close()
        return data
        
if __name__ == '__main__':        
    xml_db=XMLDateBaseAdapter()
    open_connection(xml_db)