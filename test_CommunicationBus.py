import socket
import threading
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
    def fakeServerCB(self):
        server_sock = socket.socket()
        server_sock.bind(('localhost', 10003))
        server_sock.listen(0)
        server_sock.accept()
        server_sock.close()
    @patch('socket.socket')
    def test_konekcijaCBToAdapter(self, mock_socketconstructor):
        mock_socket=mock_socketconstructor.return_value
        mock_socket.recv.return_value=bytes("<?xml version=\"1.0\" encoding=\"utf-8\"?>\n<data><status_code>2000</status_code><status>SUCCESS</status><payload>(1003, 'Ana', 'Medicinski tehnicar  u odeljenju za ginekologiju', 2)</payload></data>", encoding="utf-8")
        server_thread = threading.Thread(target=self.fakeServerCB)
        server_thread.start()
    
        xml_obj="<?xml version=\"1.0\" encoding=\"utf-8\"?>\n<data><verb>GET</verb><noun>radnik</noun><query>ime='Ana'</query></data>"
        xml_returned = CommunicationBus.connectToAdapter(self, xml_obj);
        expected_xml="<?xml version=\"1.0\" encoding=\"utf-8\"?>\n<data><status_code>2000</status_code><status>SUCCESS</status><payload>(1003, 'Ana', 'Medicinski tehnicar  u odeljenju za ginekologiju', 2)</payload></data>"
        self.assertEqual(expected_xml, xml_returned)
    
        server_thread.join()
        

if __name__ == '__main__':
    unittest.main()