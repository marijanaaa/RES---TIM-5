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

if __name__ == '__main__':
    unittest.main()
