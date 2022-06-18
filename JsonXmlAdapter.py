import json 
import xmltodict

class JsonXmlAdapter:
    def json_to_xml(self, json_obj):
        dict = json.loads(json_obj)

        myDict ={
            "data": dict,
        }
        return xmltodict.unparse(myDict)
     
    def xml_to_json(self, xml_obj):
        dict = xmltodict.parse(xml_obj)
        dict = dict["data"]
        return json.dumps(dict)