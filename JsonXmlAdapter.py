import json as j
import xml.etree.cElementTree as e
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

