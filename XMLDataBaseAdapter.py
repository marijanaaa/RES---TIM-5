import xml.etree.ElementTree as xmlCreate
from bs4 import BeautifulSoup
import socket
import pickle
import xmltodict
from ConnectSQL import ConnectToMySQL
from JsonXmlAdapter import JsonXmlAdapter

def openConnection(xmlDataBaseAdapter):
    serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    serverSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    serverSocket.bind(('127.0.0.1', 10003))
    serverSocket.listen(1)
    while(1):
        clientConnection, addr = serverSocket.accept();
        data=clientConnection.recv(1024);
        if not data:
            break
        response=xmlDataBaseAdapter.getResponse(data.decode("utf-8"))
        clientConnection.sendall(bytes(response,encoding="utf-8"))
    clientConnection.close()
    serverSocket.close()

class XMLDateBaseAdapter:
    def __init__(self, jsonXmlAdapter):
        self.JsonXmlAdapter=jsonXmlAdapter

    def GetMethod(self, xml_obj):
        print(xml_obj)

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

    def DeleteMethod(self, xml_obj):
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

    def InsertMethod(self, xml_obj):
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

    def UpdateMethod(self, xml_obj):
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
        
    def fromXMLtoSQL(self, xml_obj):        
        data = BeautifulSoup(xml_obj, 'xml') 
        data = data.find("data")
        method_tag = data.find("verb")
        method = method_tag.text

        if method == "GET":
            result = self.GetMethod(xml_obj)
        elif method == "DELETE":
            result = self.DeleteMethod(xml_obj)
        elif method == "POST":
            result = self.InsertMethod(xml_obj)
        elif method == "PATCH":
            result = self.UpdateMethod(xml_obj)

        return result

    def getResponse(self, xml_obj):
        result = self.fromXMLtoSQL(xml_obj)
        data = self.connectToRepository(result)
        
        object = pickle.loads(data)
        myDict ={
            "data": object,
        }

        return xmltodict.unparse(myDict)
        
    def connectToRepository(self, result):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect(('localhost', 10004))
        s.sendall(bytes(result, "utf-8"))
        data = s.recv(1024)

        s.close()
        return data
        
if __name__ == '__main__':        
    jsonXmlAdapter = JsonXmlAdapter()
    xmlDB=XMLDateBaseAdapter(jsonXmlAdapter)
    openConnection(xmlDB)