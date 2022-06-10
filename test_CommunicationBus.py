import unittest
import json
from CommunicationBus import badRequest, returnIsValid

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


if __name__ == '__main__':
    unittest.main()