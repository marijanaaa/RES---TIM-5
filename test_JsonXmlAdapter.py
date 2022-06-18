import unittest
from JsonXmlAdapter import JsonXmlAdapter

class TestXMLDataBaseAdapter(unittest.TestCase):
    def test_json_to_xml(self):
        json_string = "{\"verb\": \"GET\",\"noun\": \"radnik\"}"
        json = JsonXmlAdapter()
        xml = json.json_to_xml(json_string)
        xml_string = "<?xml version=\"1.0\" encoding=\"utf-8\"?>\n<data><verb>GET</verb><noun>radnik</noun></data>"
        self.assertEqual(xml,xml_string )
    def test_xml_to_json(self):
        xml_string = "<data><verb>GET</verb><noun>haha</noun></data>"

        json = JsonXmlAdapter()
        json_string = json.xml_to_json(xml_string)
        json_s = "{\"verb\": \"GET\", \"noun\": \"haha\"}"
        self.assertEqual(json_s, json_string)
if __name__ == '__main__':
    unittest.main()
