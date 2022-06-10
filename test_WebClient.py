import unittest
from unittest.mock import patch
from WebClient import Client
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

if __name__ == '__main__':
    unittest.main()
