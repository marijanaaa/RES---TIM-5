import unittest
from XMLDataBaseAdapter import XMLDateBaseAdapter

class TestXMLDataBaseAdapter(unittest.TestCase):
    def test_Delete_withoutWhere(self):
        xml_string="<data><verb>DELETE</verb><noun>radnik</noun></data>"
        xmlDB=XMLDateBaseAdapter()
        ret_value=xmlDB.DeleteMethod(xml_string)
        correct="DELETE FROM radnik; commit;"
        self.assertEqual(ret_value, correct)
    def test_Delete_withWhere(self):
        xml_string="<data><verb>DELETE</verb><noun>radnik</noun><query>ime='Ana';jmbg=12</query></data>"
        xmlDB=XMLDateBaseAdapter()
        ret_value=xmlDB.DeleteMethod(xml_string)
        correct="DELETE FROM radnik WHERE ime='Ana' and jmbg=12 ; commit;"
        self.assertEqual(ret_value, correct)
    def test_Insert(self):
        xml = "<data><verb>POST</verb><noun>radnik</noun><query>jmbg = 44; ime  = Ana; opis = nesto; id_vrsta = 111</query></data>"
        xmlDB = XMLDateBaseAdapter()
        retValue = xmlDB.InsertMethod(xml)
        sql1 = "INSERT INTO radnik VALUES (  44,  Ana,  nesto,  111); commit;"
        self.assertEqual(retValue, sql1 )
    def test_Update(self):
        xml = "<data><verb>PATCH</verb><noun>radnik</noun><query>ime  = 'Anica' </query><fields>ime='Ana'</fields></data>"
        xmlDB = XMLDateBaseAdapter()
        retValue = xmlDB.UpdateMethod(xml)
        sql1 = "UPDATE radnik SET ime  = 'Anica'  WHERE ime='Ana'; commit;"
        self.assertEqual(retValue, sql1 )

    def test_WithoutFields(self):
        xml_obj = "<data><verb>GET</verb><noun>radnik</noun><query>ime=\"Ana\"</query></data>"
        sql_query = """SELECT * from radnik where ime=\"Ana\" ; commit;"""
        adapter = XMLDateBaseAdapter()
        self.assertEqual(adapter.GetMethod(xml_obj), sql_query)
    
    def test_WithoutQueryAndFields(self):
        xml_obj = "<data><verb>GET</verb><noun>radnik</noun></data>"
        sql_query = """SELECT * from radnik; commit;"""
        adapter = XMLDateBaseAdapter()
        self.assertEqual(adapter.GetMethod(xml_obj), sql_query)

    def test_WithAll(self):
        xml_obj = "<data><verb>GET</verb><noun>radnik</noun><query>ime='Ana';jmbg=1</query><fields>id</fields></data>"
        sql_query = """SELECT id from radnik where ime='Ana' and jmbg=1 ; commit;"""
        adapter = XMLDateBaseAdapter()
        self.assertEqual(adapter.GetMethod(xml_obj), sql_query)
    
    def test_WithoutQuery(self):
        xml_obj = "<data><verb>GET</verb><noun>radnik</noun><fields>id</fields></data>"
        sql_query = """SELECT id from radnik; commit;"""
        adapter = XMLDateBaseAdapter()
        self.assertEqual(adapter.GetMethod(xml_obj), sql_query)

if __name__ == '__main__':
    unittest.main()
