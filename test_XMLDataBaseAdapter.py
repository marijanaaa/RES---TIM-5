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



if __name__ == '__main__':
    unittest.main()
