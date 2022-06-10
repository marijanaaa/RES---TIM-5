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



if __name__ == '__main__':
    unittest.main()
