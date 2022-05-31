#post insert into
#patch alter table
import xml.etree.ElementTree as xmlCreate
from bs4 import BeautifulSoup
class XMLDateBaseAdapter:
    def __init__(self, repository):
        self.repository = repository

    def GetMethod(self, x):
        with open(x, 'r') as f:
            data = f.read()
        bs_data = BeautifulSoup(data, 'xml')
        resursTag = bs_data.find("noun")  #izvadi mi ceo tag
        resurs = resursTag.text #iyvadi mi tekst iz taga
        returnTag = bs_data.find("fields")  #izvadi mi ceo tag
        sql = "SELECT "
        if (returnTag is None):
            sql+="*"

        else:
            returnC = returnTag.text #iyvadi mi tekst iz taga

            returnCNiz = returnC.split(";")
            for x in returnCNiz:
                sql += x + ","
            sql = sql[:-1]
        whereTag = bs_data.find("query")  #izvadi mi ceo tag
        sql += " from " + resurs

        if (whereTag is not None):
            where = whereTag.text #iyvadi mi tekst iz taga
            whereTagNiz = where.split(";")
            sql += " where "
            for x in whereTagNiz:
                 sql += x + " and "
            sql = sql[:-4]
        sql += "; commit;"
        return sql

    def DeleteMethod(self, x):

        with open(x, 'r') as f:
            data = f.read()
        bs_data = BeautifulSoup(data, 'xml')
        resursTag = bs_data.find("noun")  
        resurs = resursTag.text 
        sql = "DELETE FROM " + resurs

        whereTag = bs_data.find("query")  

        if whereTag is not None:

            sql += " WHERE "

            where = whereTag.text #iyvadi mi tekst iz taga

            whereTagNiz = where.split(";")

            for x in whereTagNiz:

                sql += x + " and "

            sql = sql[:-4]
        sql += "; commit;"
        return sql

    def InsertMethod(self, x):
        with open(x, 'r') as f:
            data = f.read() 
        bs_data = BeautifulSoup(data, 'xml') 
        # Using find() to extract attributes of the first instance of the tag 
        resursTag = bs_data.find("noun")  #izvadi mi ceo tag
        resurs = resursTag.text #iyvadi mi tekst iz taga

        sql = "INSERT INTO " + resurs + " VALUES ( "

        whereTag = bs_data.find("query")  #izvadi mi ceo tag
        where = whereTag.text #iyvadi mi tekst iz taga
        whereTagNiz = where.split(";")

        for x in whereTagNiz:
            niz = x.split("=")
            sql += niz[1] + ", "

        sql = sql[:-2]
        sql += "); commit;"
        return sql
    
    def UpdateMethod(self, x):
        with open(x, 'r') as f:
            data = f.read() 

        # Passing the stored data inside the beautifulsoup parser 
        bs_data = BeautifulSoup(data, 'xml') 
        # Using find() to extract attributes of the first instance of the tag 
        resursTag = bs_data.find("noun")  #izvadi mi ceo tag
        resurs = resursTag.text #iyvadi mi tekst iz taga
       

        returnTag = bs_data.find_all('query') #izvadi mi ceo tag
        set = returnTag[0].text
        where = returnTag[1].text

        setNiz = set.split(";")
        #returnC = returnTag.text #iyvadi mi tekst iz taga
        #returnCNiz = returnC.split(";")

        sql = "UPDATE " + resurs + " SET "

        for x in setNiz:
                sql += x + ","

        sql = sql[:-1]
        sql +=" WHERE " + where + "; commit;"

        return sql


    def fromXMLtoSQL(self, x):
        
        
        # Reading the data inside the xml file to a variable under the name  data
        with open(x, 'r') as f:
            data = f.read() 
        

        # Passing the stored data inside the beautifulsoup parser 
        bs_data = BeautifulSoup(data, 'xml') 

        method = bs_data.find("verb")
        methodText = method.text

        if methodText == "GET":
            result = self.GetMethod(x)
        elif methodText == "DELETE":
            result = self.DeleteMethod(x)
        elif methodText == "POST":
            result = self.InsertMethod(x)
        elif methodText == "PATCH":
            result = self.UpdateMethod(x)

        return result
    
    def getResponse(self, x):
        result = self.fromXMLtoSQL(x)
        [code, list] = self.repository.doQuery(result)
        return self.fromSqlToXml(code, list)
    def fromSqlToXml(self, code, list):
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
            payload.text=list
        else:
            for i in list:
                row=xmlCreate.SubElement(payload, "row")
                for j in i:
                    subrow=xmlCreate.SubElement(row, "subrow")
                    subrow.text=str(j)
        tree=xmlCreate.ElementTree(response)
        with open(outputFile, "wb") as files :
            tree.write(files)
        return outputFile

