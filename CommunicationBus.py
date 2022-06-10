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
def openConnection(communicationBus):
    serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    serverSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    serverSocket.bind(('localhost', 10005))
    serverSocket.listen(1)
    while(1):
        clientConnection, addr = serverSocket.accept();
        data=clientConnection.recv(1024);
        if not data:
            break
        dict = json.loads(data)
        isValid=False
        if "verb" in dict and "noun" in dict:
            for verb in verbs:
                if dict["verb"] == verb:
                    isValid = True
            if dict["verb"] == verbs[1]:
                if "query" not in dict:
                    isValid=False
            elif dict["verb"] == verbs[2]:
                if "query" not in dict or "fields" not in dict:
                    isValid=False
        else:
            response=badRequest()

        if isValid == False:
            response = badRequest()
        else:
            response=communicationBus.ExecuteRequest(data.decode("utf-8"))
        clientConnection.sendall(bytes(response,encoding="utf-8"))
        clientConnection.close()
    serverSocket.close()

def badRequest():
    json_response = {
        "status_code":5000,
        "status":"BAD_FORMAT",
        "payload":"Request is not valid",
    }
    dict=json.dumps(json_response)
    return dict

class CommunicationBus:
    def __init__(self, jsonXmlAdapter):
        self.JsonXmlAdapter=jsonXmlAdapter
    def ExecuteRequest(self, json_obj):
        xml_obj=self.JsonXmlAdapter.JsonToXml(json_obj)
        result=self.connectToAdapter(xml_obj)
        return self.JsonXmlAdapter.XmlToJson(result)
    def connectToAdapter(self, xml_obj):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect(('localhost', 10003))
        s.sendall(bytes(xml_obj, "utf-8"))
        data = s.recv(1024)
        s.close()
        return data.decode("utf-8")
jsonXmlAdapter = JsonXmlAdapter()
communicationBus= CommunicationBus(jsonXmlAdapter)
openConnection(communicationBus)