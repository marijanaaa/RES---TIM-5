from pickle import FALSE
import socket
from JsonXmlAdapter import JsonXmlAdapter
import json
verbs = [
    "GET",
    "POST",
    "PATCH",
    "DELETE",
]
def open_connection(communication_bus):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind(('localhost', 10005))
    server_socket.listen(1)
    while(1):
        client_connection, addr = server_socket.accept();
        data=client_connection.recv(1024);
        if not data:
            break
        
        response = ParseRequest(data, communication_bus)

        client_connection.sendall(bytes(response,encoding="utf-8"))
        client_connection.close()
    server_socket.close()

def ParseRequest(data, communicationBus):
    dict = json.loads(data)
    is_valid=False
    if "verb" in dict and "noun" in dict:
        is_valid=return_is_valid(dict)
    else:
        response=bad_request()

    if is_valid == False:
        response = bad_request()
    else:
        response=communication_bus.execute_request(data.decode("utf-8"))
    return response

def return_is_valid(dict):
    is_valid=False
    for verb in verbs:
        if dict["verb"] == verb:
            is_valid = True
        if dict["verb"] == verbs[1]:
            if "query" not in dict:
                is_valid=False
        elif dict["verb"] == verbs[2]:
            if "query" not in dict or "fields" not in dict:
                is_valid=False
    return is_valid

def bad_request():
    json_response = {
        "status_code":5000,
        "status":"BAD_FORMAT",
        "payload":"Request is not valid",
    }
    dict=json.dumps(json_response)
    return dict

class CommunicationBus:
    def __init__(self,):
        self.JsonXmlAdapter=JsonXmlAdapter()
    def execute_request(self, json_obj):
        xml_obj=self.JsonXmlAdapter.json_to_xml(json_obj)
        result=self.connect_to_adapter(xml_obj)
        return self.JsonXmlAdapter.xml_to_json(result)
    def connect_to_adapter(self, xml_obj):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect(('localhost', 10003))
        s.sendall(bytes(xml_obj, "utf-8"))
        data = s.recv(1024)
        s.close()
        return data.decode("utf-8")
if __name__ == '__main__': 
    communication_bus= CommunicationBus()
    open_connection(communication_bus)