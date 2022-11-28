class PhoneNumber:
    def __init__(self, areaCode, tel, line,country=None, extension=None):
        self.__countryCode = country
        self.__areaCode = areaCode
        self.__telephonePrefix = tel
        self.__lineNumber = line
        self.__extension = extension
    
    def display(self):
        return self.__countryCode + self.__areaCode + self.__telephonePrefix + self.__lineNumber + self.__extension
    
    def setCountryCode(self, code):
        self.__countryCode = code
    
    def setAreaCode(self, code):
        self.__areaCode = code
    
    def setTelephonePrefix(self, code):
        self.__telephonePrefix = code
    
    def setLineNumber(self, code):
        self.__lineNumber = code
    
    def setExtension(self, code):
        self.__extension = code