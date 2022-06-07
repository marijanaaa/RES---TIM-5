import json as j
import xml.etree.cElementTree as elementTree
from bs4 import BeautifulSoup
class JsonXmlAdapter:
    def JsonToXml(self, json_obj):
        json_object=j.loads(json_obj)
        root_element = elementTree.Element("request")
        elementTree.SubElement(root_element,"verb").text = json_object['verb']
        elementTree.SubElement(root_element,"noun").text = json_object["noun"]
        if("query" in json_object):
            elementTree.SubElement(root_element,"query").text = json_object["query"]
        if("fields" in json_object):
            elementTree.SubElement(root_element,"fields").text = json_object["fields"]
        json_notation = elementTree.ElementTree(root_element)
        json_notation.write("json_to_xml.xml")
        return "json_to_xml.xml"
    
    def XmlToJson(self, fileName):
        with open(fileName, 'r') as file:
            raw_data = file.read()
        data = BeautifulSoup(raw_data, 'xml')

        statusTag = data.find("status")
        status = statusTag.text

        status_codeTag = data.find("status_code")
        status_code=status_codeTag.text
        
        payloadTag=data.find("payload")
        payload=''
        if(status_code == 3000):
            payload=payloadTag.text
        else:
            rows=data.findAll("row")
            for x in rows:
                subrows=x.findAll("subrow")
                for y in subrows:
                    payload+=y.text+" "
                payload+="\n"

        if(len(payload) == 0):
            payload="Operation successfull"

        json_data={
            "status":status,
            "status_code" : status_code,
            "payload" : payload
        }

        json_object=j.dumps(json_data, indent=3)
        
        return json_object

