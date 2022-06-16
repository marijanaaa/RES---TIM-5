import socket
import threading
import unittest
from unittest.mock import patch
import unittest.mock as mock
from WebClient import Client, printResponse, conenctToServer
import builtins

class TestWebClient(unittest.TestCase):
    @patch('builtins.input')
    def test_DeleteWithQuery(self, m_input):
        m_input.side_effect=["DELETE", "radnik", "ime='Ana'"]
        expected_query={
            'verb': 'DELETE', 
            'noun': 'radnik', 
            'query': "ime='Ana'"
        }
        response=Client()
        self.assertEqual(expected_query, response)
    @patch('builtins.input')
    def test_DeleteWithoutQuery(self, m_input):
        m_input.side_effect=["DELETE", "radnik", ""]
        expected_query={
            'verb':'DELETE',
            'noun':'radnik'
        }
        response=Client()
        self.assertEqual(expected_query, response)

    @patch('builtins.input')
    def test_GetWithAll(self, m_input):
        m_input.side_effect=['GET', 'radnik', 'ime=\'Ana\'', 'id']
        expected_query={
            "verb" : "GET",
            "noun" : "radnik",
            "query" : "ime=\'Ana\'",
            "fields" : "id"
        }
        response=Client()
        self.assertEqual(expected_query, response)
    
    @patch('builtins.input')
    def test_GetWithoutFields(self, m_input):
        m_input.side_effect=['GET', 'radnik', 'ime=\'Ana\'', '']
        expected_query={
            "verb" : "GET",
            "noun" : "radnik",
            "query" : "ime=\'Ana\'"
        }
        response=Client()
        self.assertEqual(expected_query, response)

    @patch('builtins.input')
    def test_GetWithoutQuery(self, m_input):
        m_input.side_effect=['GET', 'radnik', '', 'id']
        expected_query={
             "verb" : "GET",
            "noun" : "radnik",
            "fields" : "id"
        }
        response=Client()
        self.assertEqual(expected_query, response)
    
    @patch('builtins.input')
    def test_GetWithoutQueryAndFields(self, m_input):
        m_input.side_effect=['GET', 'radnik', '', '']
        expected_query={
             "verb" : "GET",
            "noun" : "radnik",
        }
        response=Client()
        self.assertEqual(expected_query, response)
    @patch('builtins.input')
    def test_Update(self, m_input):
        m_input.side_effect=['PATCH', 'radnik', 'ime=\'Anica\'', 'ime=\'Ana\'']
        expected_query={
            "verb" : "PATCH",
            "noun" : "radnik",
            "query" : "ime=\'Anica\'",
            "fields" : "ime=\'Ana\'"
        }
        response=Client()
        self.assertEqual(expected_query, response)

    @patch('builtins.input')

    def test_Insert(self, m_input):

        m_input.side_effect=['POST', 'radnik', 'jmbg=\'44\', ime=\'Ana\', opis=\'nesto\', id_vrsta=\'8\'']

        expected_query={

            "verb" : "POST",

            "noun" : "radnik",

            "query" : "jmbg=\'44\', ime=\'Ana\', opis=\'nesto\', id_vrsta=\'8\'",

        }
        response=Client()
        self.assertEqual(expected_query, response)

    def test_printResponseError(self):
        mock_print=mock.Mock(side_effect=lambda:(print("REJECTED\nBAD_FORMAT")))
        response={'status_code': 5000, 'status': 'BAD_FORMAT', 'payload': 'Request is not valid'}
        self.assertEquals(mock_print(), printResponse(response))

    def test_printResponseSuccessSingle(self):
        mock_print=mock.Mock(side_effect=lambda:(print("SUCCESS\n1003, 'Ana', 'Medicinski tehnicar  u odeljenju za ginekologiju', 2")))
        response={'status_code': '2000', 'status': 'SUCCESS', 'payload': "(1003, 'Ana', 'Medicinski tehnicar  u odeljenju za ginekologiju', 2)"}
        self.assertEqual(mock_print(), printResponse(response))

    def test_printResponseSuccessMultiple(self):
        mock_print=mock.Mock(side_effect=lambda:(print("SUCCESS\n1, 1003, 4566, 1\n2, 9699, 4566, 1")))
        response={'status_code': '2000', 'status': 'SUCCESS', 'payload': ['(1, 1003, 4566, 1)', '(2, 9699, 4566, 1)']}
        self.assertEqual(mock_print(), printResponse(response))
    def fakeServerWC(self):
        server_sock = socket.socket()
        server_sock.bind(('localhost', 10005))
        server_sock.listen(0)
        server_sock.accept()
        server_sock.close()
    @patch('socket.socket')
    def test_konekcijaWebClientToServer(self, mock_socketconstructor):
        mock_socket=mock_socketconstructor.return_value
        mock_socket.recv.return_value="{\"status_code\": \"2000\", \"status\": \"SUCCESS\", \"payload\": \"(1003, 'Ana', 'Medicinski tehnicar  u odeljenju za ginekologiju', 2)\"}"
        server_thread = threading.Thread(target=self.fakeServerWC)
        server_thread.start()
    
        json_obj="{ 'verb': 'GET', 'noun':'radnik', 'query':'ime='Ana''}"
        conenctToServer(json_obj);
    
        server_thread.join()
if __name__ == '__main__':
    unittest.main()
