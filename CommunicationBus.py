class CommunicationBus:
    def __init__(self, jsonXmlAdapter, xmlDataBaseAdapter):
          self.JsonXmlAdapter=jsonXmlAdapter
          self.XmlDataBaseAdapter=xmlDataBaseAdapter
    def ExecuteRequest(self, jsonFile):
        xmlFile=self.JsonXmlAdapter.JsonToXml(jsonFile)
        result=self.XmlDataBaseAdapter.getResponse(xmlFile)
        return self.JsonXmlAdapter.XmlToJson(result)
