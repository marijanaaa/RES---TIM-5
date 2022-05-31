import json as j
import xml.etree.cElementTree as e
from bs4 import BeautifulSoup
class JsonXmlAdapter:
    def JsonToXml(self, filename):
        with open(filename) as json_format_file:
            d = j.load(json_format_file)
            r = e.Element("request")
            e.SubElement(r,"verb").text = d["verb"]
            e.SubElement(r,"noun").text = d["noun"]
            e.SubElement(r,"query").text = d["query"]
            e.SubElement(r,"fields").text = d["fields"]
            a = e.ElementTree(r)
            a.write("json_to_xml.xml")
            return "json_to_xml.xml"
    
    def XmlToJson(self, fileName):
        with open(fileName, 'r') as f:
            data = f.read()
        bs_data = BeautifulSoup(data, 'xml')
        statusTag = bs_data.find("status")  #izvadi mi ceo tag
        status = statusTag.text #iyvadi mi tekst iz taga
        status_codeTag = bs_data.find("status_code")  #izvadi mi ceo tag
        status_code=status_codeTag.text
        payloadTag=bs_data.find("payload")
        payload=payloadTag.text

        if(len(payload) == 0):
            payload="Operation successfull"

        json_data={
            "status":status,
            "status_code" : status_code,
            "payload" : payload
        }

        json_object=j.dumps(json_data, indent=3)

        outputFile="xml_to_json.json";
        with open(outputFile, "w") as file:
            file.write(json_object)
        
        return outputFile

