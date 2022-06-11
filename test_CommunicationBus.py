import unittest
import json
from CommunicationBus import badRequest, returnIsValid, CommunicationBus
from JsonXmlAdapter import JsonXmlAdapter
from unittest.mock import MagicMock, patch

class TestCommunicationBus(unittest.TestCase):
    def test_badRequest(self):
        json_response = {
            "status_code":5000,
            "status":"BAD_FORMAT",
            "payload":"Request is not valid",
        }
        expected_response=json.dumps(json_response)
        response=badRequest()
        self.assertEquals(response, expected_response)
    
    def test_returnIsValidGetTrue(self):
        dict_data={'verb': 'GET', 'noun': 'radnik', 'query': "ime='Ana'"}
        expected_response=True
        response=returnIsValid(dict_data)
        self.assertEquals(response, expected_response)

    def test_returnIsValidPost(self):
        dict_data={'verb': 'POST', 'noun': 'radnik'}
        expected_response=False
        response=returnIsValid(dict_data)
        self.assertEquals(response, expected_response)

    def test_returnIsValidPatch(self):
        dict_data={'verb': 'PATCH', 'noun': 'radnik'}
        expected_response=False
        response=returnIsValid(dict_data)
        self.assertEquals(response, expected_response)
    
    def test_returnIsValidUnknownVerb(self):
        dict_data={'verb': 'EE'}
        expected_response=False
        response=returnIsValid(dict_data)
        self.assertEquals(response, expected_response)
    @patch("JsonXmlAdapter.JsonXmlAdapter")
    def test_executeRequest(self, mock_JsonXMLAdapterConstructor):
        mock_json=mock_JsonXMLAdapterConstructor.return_value
        mock_json.JsonToXml.return_value="<?xml version=\"1.0\" encoding=\"utf-8\"?>\n<data><verb>GET</verb><noun>radnik</noun><query>ime='Ana'</query></data>"
        comm=CommunicationBus()
        jsonString = "{\"verb\": \"GET\",\"noun\": \"radnik\", \"query\":\"ime='Ana'\"}"
        expected_response = json.dumps({"status_code": "2000", "status": "SUCCESS", "payload": "(1003, 'Ana', 'Medicinski tehnicar  u odeljenju za ginekologiju', 2)"})
        comm.connectToAdapter=MagicMock(return_value = "<?xml version=\"1.0\" encoding=\"utf-8\"?>\n<data><status_code>2000</status_code><status>SUCCESS</status><payload>(1003, 'Ana', 'Medicinski tehnicar  u odeljenju za ginekologiju', 2)</payload></data>")
        self.assertEqual(comm.ExecuteRequest(jsonString), expected_response)
        

if __name__ == '__main__':
    unittest.main()