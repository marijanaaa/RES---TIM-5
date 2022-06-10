import json 
import xmltodict

class JsonXmlAdapter:
    def JsonToXml(self, json_obj):
        dict = json.loads(json_obj)

        myDict ={
            "data": dict,
        }
        return xmltodict.unparse(myDict)
     
    def XmlToJson(self, xml_obj):
        dict = xmltodict.parse(xml_obj)
        dict = dict["data"]
        return json.dumps(dict)