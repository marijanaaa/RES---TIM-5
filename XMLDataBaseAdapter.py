import xml.etree.ElementTree as xmlCreate
from bs4 import BeautifulSoup
class XMLDateBaseAdapter:
    def __init__(self, repository):
        self.repository = repository

    def GetMethod(self, fileName):
        with open(fileName, 'r') as file:
            raw_data = file.read()
        data = BeautifulSoup(raw_data, 'xml')

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

    def DeleteMethod(self, fileName):

        with open(fileName, 'r') as file:
            raw_data = file.read()
        data = BeautifulSoup(raw_data, 'xml')
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

    def InsertMethod(self, fileName):
        with open(fileName, 'r') as file:
            raw_data = file.read() 
        data = BeautifulSoup(raw_data, 'xml') 
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
    
    def UpdateMethod(self, fileName):
        with open(fileName, 'r') as file:
            raw_data = file.read() 

        data = BeautifulSoup(raw_data, 'xml') 
        noun_tag = data.find("noun")
        noun = noun_tag.text
       

        query_tag = data.find_all('query')
        set = query_tag[0].text
        where = query_tag[1].text

        set_array = set.split(";")

        sql_query = "UPDATE " + noun + " SET "

        for x in set_array:
                sql_query += x + ","

        sql_query = sql_query[:-1]
        sql_query +=" WHERE " + where + "; commit;"

        return sql_query


    def fromXMLtoSQL(self, fileName):
        
        with open(fileName, 'r') as file:
            raw_data = file.read() 
        
        data = BeautifulSoup(raw_data, 'xml') 

        method_tag = data.find("verb")
        method = method_tag.text

        if method == "GET":
            result = self.GetMethod(fileName)
        elif method == "DELETE":
            result = self.DeleteMethod(fileName)
        elif method == "POST":
            result = self.InsertMethod(fileName)
        elif method == "PATCH":
            result = self.UpdateMethod(fileName)

        return result
    
    def getResponse(self, fileName):
        result = self.fromXMLtoSQL(fileName)
        [code, data] = self.repository.doQuery(result)
        return self.fromSqlToXml(code, data)

    def fromSqlToXml(self, code, data):
        outputFile="outputFile.xml"
        response=xmlCreate.Element("response")
        status=xmlCreate.SubElement(response, "status")
        if(code==3000):
            status.text="REJECTED"
        else:
            status.text="SUCCESS"
        status_code=xmlCreate.SubElement(response, "status_code")
        status_code.text=str(code)
        payload=xmlCreate.SubElement(response, "payload")
        if(code==3000):
            payload.text=data
        else:
            for i in data:
                row=xmlCreate.SubElement(payload, "row")
                for j in i:
                    subrow=xmlCreate.SubElement(row, "subrow")
                    subrow.text=str(j)
        tree=xmlCreate.ElementTree(response)
        with open(outputFile, "wb") as files :
            tree.write(files)
            
        return outputFile


