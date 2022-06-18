import socket
import threading
import unittest
from unittest.mock import patch
import unittest.mock as mock
from WebClient import client, print_response, conenct_to_server
import builtins

class TestWebClient(unittest.TestCase):
    @patch('builtins.input')
    def test_delete_with_query(self, m_input):
        m_input.side_effect=["DELETE", "radnik", "ime='Ana'"]
        expected_query={
            'verb': 'DELETE', 
            'noun': 'radnik', 
            'query': "ime='Ana'"
        }
        response=client()
        self.assertEqual(expected_query, response)
    @patch('builtins.input')
    def test_delete_without_query(self, m_input):
        m_input.side_effect=["DELETE", "radnik", ""]
        expected_query={
            'verb':'DELETE',
            'noun':'radnik'
        }
        response=client()
        self.assertEqual(expected_query, response)

    @patch('builtins.input')
    def test_get_with_all(self, m_input):
        m_input.side_effect=['GET', 'radnik', 'ime=\'Ana\'', 'id']
        expected_query={
            "verb" : "GET",
            "noun" : "radnik",
            "query" : "ime=\'Ana\'",
            "fields" : "id"
        }
        response=client()
        self.assertEqual(expected_query, response)
    
    @patch('builtins.input')
    def test_get_without_fields(self, m_input):
        m_input.side_effect=['GET', 'radnik', 'ime=\'Ana\'', '']
        expected_query={
            "verb" : "GET",
            "noun" : "radnik",
            "query" : "ime=\'Ana\'"
        }
        response=client()
        self.assertEqual(expected_query, response)

    @patch('builtins.input')
    def test_get_without_query(self, m_input):
        m_input.side_effect=['GET', 'radnik', '', 'id']
        expected_query={
             "verb" : "GET",
            "noun" : "radnik",
            "fields" : "id"
        }
        response=client()
        self.assertEqual(expected_query, response)
    
    @patch('builtins.input')
    def test_get_without_query_and_fields(self, m_input):
        m_input.side_effect=['GET', 'radnik', '', '']
        expected_query={
             "verb" : "GET",
            "noun" : "radnik",
        }
        response=client()
        self.assertEqual(expected_query, response)
    @patch('builtins.input')
    def test_update(self, m_input):
        m_input.side_effect=['PATCH', 'radnik', 'ime=\'Anica\'', 'ime=\'Ana\'']
        expected_query={
            "verb" : "PATCH",
            "noun" : "radnik",
            "query" : "ime=\'Anica\'",
            "fields" : "ime=\'Ana\'"
        }
        response=client()
        self.assertEqual(expected_query, response)

    @patch('builtins.input')

    def test_insert(self, m_input):

        m_input.side_effect=['POST', 'radnik', 'jmbg=\'44\', ime=\'Ana\', opis=\'nesto\', id_vrsta=\'8\'']

        expected_query={

            "verb" : "POST",

            "noun" : "radnik",

            "query" : "jmbg=\'44\', ime=\'Ana\', opis=\'nesto\', id_vrsta=\'8\'",

        }
        response=client()
        self.assertEqual(expected_query, response)

    def test_print_response_error(self):
        mock_print=mock.Mock(side_effect=lambda:(print("REJECTED\nBAD_FORMAT")))
        response={'status_code': 5000, 'status': 'BAD_FORMAT', 'payload': 'Request is not valid'}
        self.assertEquals(mock_print(), print_response(response))

    def test_print_response_success_single(self):
        mock_print=mock.Mock(side_effect=lambda:(print("SUCCESS\n1003, 'Ana', 'Medicinski tehnicar  u odeljenju za ginekologiju', 2")))
        response={'status_code': '2000', 'status': 'SUCCESS', 'payload': "(1003, 'Ana', 'Medicinski tehnicar  u odeljenju za ginekologiju', 2)"}
        self.assertEqual(mock_print(), print_response(response))

    def test_print_response_success_multiple(self):
        mock_print=mock.Mock(side_effect=lambda:(print("SUCCESS\n1, 1003, 4566, 1\n2, 9699, 4566, 1")))
        response={'status_code': '2000', 'status': 'SUCCESS', 'payload': ['(1, 1003, 4566, 1)', '(2, 9699, 4566, 1)']}
        self.assertEqual(mock_print(), print_response(response))
    def fake_server_wc(self):
        server_sock = socket.socket()
        server_sock.bind(('localhost', 10005))
        server_sock.listen(0)
        server_sock.accept()
        server_sock.close()
    @patch('socket.socket')
    def test_konekcija_web_client_to_server(self, mock_socketconstructor):
        mock_socket=mock_socketconstructor.return_value
        mock_socket.recv.return_value="{\"status_code\": \"2000\", \"status\": \"SUCCESS\", \"payload\": \"(1003, 'Ana', 'Medicinski tehnicar  u odeljenju za ginekologiju', 2)\"}"
        server_thread = threading.Thread(target=self.fake_server_wc)
        server_thread.start()
    
        json_obj="{ 'verb': 'GET', 'noun':'radnik', 'query':'ime='Ana''}"
        conenct_to_server(json_obj);
    
        server_thread.join()
if __name__ == '__main__':
    unittest.main()
