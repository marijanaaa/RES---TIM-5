#post insert into
#patch alter table

from bs4 import BeautifulSoup
class XMLDateBaseAdapter:
    def __init__(self, repository):
        self.repository = repository

    def GetMethod(self, x):

        with open(x, 'r') as f:
            data = f.read() 

        # Passing the stored data inside the beautifulsoup parser 
        bs_data = BeautifulSoup(data, 'xml') 
        # Using find() to extract attributes of the first instance of the tag 
        resursTag = bs_data.find("noun")  #izvadi mi ceo tag
        resurs = resursTag.text #iyvadi mi tekst iz taga

        returnTag = bs_data.find("fields")  #izvadi mi ceo tag
        returnC = returnTag.text #iyvadi mi tekst iz taga
        returnCNiz = returnC.split(";")

        sql = "SELECT "

        for x in returnCNiz:
                sql += x + ","

        sql = sql[:-1]
        whereTag = bs_data.find("query")  #izvadi mi ceo tag
        where = whereTag.text #iyvadi mi tekst iz taga
        whereTagNiz = where.split(";")

        sql += " from " + resurs + " where " 

        for x in whereTagNiz:
            sql += x + " and "

        sql = sql[:-4]
       

        return sql

    def DeleteMethod(self, x):
        with open(x, 'r') as f:
            data = f.read() 

        # Passing the stored data inside the beautifulsoup parser 
        bs_data = BeautifulSoup(data, 'xml') 
        # Using find() to extract attributes of the first instance of the tag 
        resursTag = bs_data.find("noun")  #izvadi mi ceo tag
        resurs = resursTag.text #iyvadi mi tekst iz taga

        sql = "DELETE FROM " + resurs + " WHERE "

        whereTag = bs_data.find("query")  #izvadi mi ceo tag
        where = whereTag.text #iyvadi mi tekst iz taga
        whereTagNiz = where.split(";")


        for x in whereTagNiz:
            sql += x + " and "

        sql = sql[:-4]
        print(sql)

        return sql

    def InsertMethod(self, x):
        with open(x, 'r') as f:
                data = f.read() 

        # Passing the stored data inside the beautifulsoup parser 
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
        sql += ")"
        sql = sql[:-1]

        return sql
    
    def UpdateMethod(self, x):
        with open(x, 'r') as f:
            data = f.read() 

        # Passing the stored data inside the beautifulsoup parser 
        bs_data = BeautifulSoup(data, 'xml') 
        # Using find() to extract attributes of the first instance of the tag 
        resursTag = bs_data.find("noun")  #izvadi mi ceo tag
        resurs = resursTag.text #iyvadi mi tekst iz taga

        returnTag = bs_data.find("fields")  #izvadi mi ceo tag
        returnC = returnTag.text #iyvadi mi tekst iz taga
        returnCNiz = returnC.split(";")

        sql = "UPDATE " + resurs + " SET "

        for x in returnCNiz:
                sql += x + ","

        sql = sql[:-1]
        whereTag = bs_data.find("query")  #izvadi mi ceo tag
        where = whereTag.text #iyvadi mi tekst iz taga
        whereTagNiz = where.split(";")

        sql +=" WHERE " 

        for x in whereTagNiz:
            sql += x + " and "

        sql = sql[:-4]
        print(sql)

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
        list = self.repository.doQuery(result)
        for row in list:
            print(row)
