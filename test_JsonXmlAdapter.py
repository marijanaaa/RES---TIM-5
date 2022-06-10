import unittest
from JsonXmlAdapter import JsonXmlAdapter

class TestXMLDataBaseAdapter(unittest.TestCase):
    def test_JSonToXml(self):
        jsonString = "{\"verb\": \"GET\",\"noun\": \"radnik\"}"
        json = JsonXmlAdapter()
        xml = json.JsonToXml(jsonString)
        xmlString = "<?xml version=\"1.0\" encoding=\"utf-8\"?>\n<data><verb>GET</verb><noun>radnik</noun></data>"
        self.assertEqual(xml,xmlString )
    def test_XMLtoJson(self):
        xmlString = "<data><verb>GET</verb><noun>haha</noun></data>"

        json = JsonXmlAdapter()
        jsonString = json.XmlToJson(xmlString)
        jsonS = "{\"verb\": \"GET\", \"noun\": \"haha\"}"
        self.assertEqual(jsonS, jsonString)
if __name__ == '__main__':
    unittest.main()
