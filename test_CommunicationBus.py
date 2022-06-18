from asyncio import sleep
import socket
import threading
import unittest
import json
from CommunicationBus import bad_request, return_is_valid, parse_request, CommunicationBus
from JsonXmlAdapter import JsonXmlAdapter
from unittest.mock import MagicMock, patch

class TestCommunicationBus(unittest.TestCase):
    def fakeServerCB2(self):
        server_sock = socket.socket()
        server_sock.bind(('localhost', 10003))
        server_sock.listen(0)
        server_sock.accept()
        server_sock.close()

    @patch('socket.socket')
    @patch("JsonXmlAdapter.JsonXmlAdapter")
    def test_ParseRequest(self,mock_JsonXMLAdapterConstructor,mock_socketconstructor):
        dict = {'verb': 'GET', 'noun': 'radnik', 'query': "ime='Ana'"}
        data = b'{"verb": "GET", "noun": "radnik", "query": "ime=\'Ana\'"}'
        odg = "{\"status_code\": \"2000\", \"status\": \"SUCCESS\", \"payload\": \"(1003, 'Ana', 'Medicinski tehnicar  u odeljenju za ginekologiju', 2)\"}"
        mock_socket=mock_socketconstructor.return_value
        mock_socket.recv.return_value=bytes("<?xml version=\"1.0\" encoding=\"utf-8\"?>\n<data><status_code>2000</status_code><status>SUCCESS</status><payload>(1003, 'Ana', 'Medicinski tehnicar  u odeljenju za ginekologiju', 2)</payload></data>", encoding="utf-8")
        server_thread = threading.Thread(target=self.fakeServerCB2)
        server_thread.start()
    
        xml_obj="<?xml version=\"1.0\" encoding=\"utf-8\"?>\n<data><verb>GET</verb><noun>radnik</noun><query>ime='Ana'</query></data>"
        xml_returned = CommunicationBus.connect_to_adapter(self, xml_obj);
        expected_xml="<?xml version=\"1.0\" encoding=\"utf-8\"?>\n<data><status_code>2000</status_code><status>SUCCESS</status><payload>(1003, 'Ana', 'Medicinski tehnicar  u odeljenju za ginekologiju', 2)</payload></data>"
        self.assertEqual(expected_xml, xml_returned)
        server_thread.join()

        mock_json=mock_JsonXMLAdapterConstructor.return_value
        mock_json.JsonToXml.return_value="<?xml version=\"1.0\" encoding=\"utf-8\"?>\n<data><verb>GET</verb><noun>radnik</noun><query>ime='Ana'</query></data>"
        comm=CommunicationBus()
        jsonString = "{\"verb\": \"GET\",\"noun\": \"radnik\", \"query\":\"ime='Ana'\"}"
        expected_response = json.dumps({"status_code": "2000", "status": "SUCCESS", "payload": "(1003, 'Ana', 'Medicinski tehnicar  u odeljenju za ginekologiju', 2)"})
        comm.connectToAdapter=MagicMock(return_value = "<?xml version=\"1.0\" encoding=\"utf-8\"?>\n<data><status_code>2000</status_code><status>SUCCESS</status><payload>(1003, 'Ana', 'Medicinski tehnicar  u odeljenju za ginekologiju', 2)</payload></data>")

        res = parse_request(data, comm)
        

        

    def test_badRequest(self):
        json_response = {
            "status_code":5000,
            "status":"BAD_FORMAT",
            "payload":"Request is not valid",
        }
        expected_response=json.dumps(json_response)
        response=bad_request()
        self.assertEquals(response, expected_response)
    
    def test_return_is_valid_get_true(self):
        dict_data={'verb': 'GET', 'noun': 'radnik', 'query': "ime='Ana'"}
        expected_response=True
        response=return_is_valid(dict_data)
        self.assertEquals(response, expected_response)

    def test_return_is_valid_post(self):
        dict_data={'verb': 'POST', 'noun': 'radnik'}
        expected_response=False
        response=return_is_valid(dict_data)
        self.assertEquals(response, expected_response)

    def test_return_is_valid_patch(self):
        dict_data={'verb': 'PATCH', 'noun': 'radnik'}
        expected_response=False
        response=return_is_valid(dict_data)
        self.assertEquals(response, expected_response)
    
    def test_return_is_valid_unknown_verb(self):
        dict_data={'verb': 'EE'}
        expected_response=False
        response=return_is_valid(dict_data)
        self.assertEquals(response, expected_response)
    @patch("JsonXmlAdapter.JsonXmlAdapter")
    def test_execute_request(self, mock_JsonXMLAdapterConstructor):
        mock_json=mock_JsonXMLAdapterConstructor.return_value
        mock_json.json_to_xml.return_value="<?xml version=\"1.0\" encoding=\"utf-8\"?>\n<data><verb>GET</verb><noun>radnik</noun><query>ime='Ana'</query></data>"
        comm=CommunicationBus()
        json_string = "{\"verb\": \"GET\",\"noun\": \"radnik\", \"query\":\"ime='Ana'\"}"
        expected_response = json.dumps({"status_code": "2000", "status": "SUCCESS", "payload": "(1003, 'Ana', 'Medicinski tehnicar  u odeljenju za ginekologiju', 2)"})
        comm.connect_to_adapter=MagicMock(return_value = "<?xml version=\"1.0\" encoding=\"utf-8\"?>\n<data><status_code>2000</status_code><status>SUCCESS</status><payload>(1003, 'Ana', 'Medicinski tehnicar  u odeljenju za ginekologiju', 2)</payload></data>")
        self.assertEqual(comm.execute_request(json_string), expected_response)
    def fake_server_cb(self):
        server_sock = socket.socket()
        server_sock.bind(('localhost', 10003))
        server_sock.listen(0)
        server_sock.accept()
        server_sock.close()
    @patch('socket.socket')
    def test_konekcija_cb_to_adapter(self, mock_socketconstructor):
        mock_socket=mock_socketconstructor.return_value
        mock_socket.recv.return_value=bytes("<?xml version=\"1.0\" encoding=\"utf-8\"?>\n<data><status_code>2000</status_code><status>SUCCESS</status><payload>(1003, 'Ana', 'Medicinski tehnicar  u odeljenju za ginekologiju', 2)</payload></data>", encoding="utf-8")
        server_thread = threading.Thread(target=self.fake_server_cb)
        server_thread.start()
    
        xml_obj="<?xml version=\"1.0\" encoding=\"utf-8\"?>\n<data><verb>GET</verb><noun>radnik</noun><query>ime='Ana'</query></data>"
        xml_returned = CommunicationBus.connect_to_adapter(self, xml_obj);
        expected_xml="<?xml version=\"1.0\" encoding=\"utf-8\"?>\n<data><status_code>2000</status_code><status>SUCCESS</status><payload>(1003, 'Ana', 'Medicinski tehnicar  u odeljenju za ginekologiju', 2)</payload></data>"
        self.assertEqual(expected_xml, xml_returned)
    
        server_thread.join()
        

if __name__ == '__main__':
    unittest.main()