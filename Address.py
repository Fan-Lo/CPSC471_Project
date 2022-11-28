class Address:
    def __init__(self, country, province, city, address, posCode):
        self.__country = country
        self.__province = province
        self.__city = city
        self.__address = address
        self.__posCode = posCode
    
    def setCountry(self, con):
        self.__country = con
    
    def setProvince(self, prov):
        self.__province = prov
    
    def setCity(self, city):
        self.__city = city
    
    def setAddress(self, address):
        self.__address = address
        
    def setPostalCode(self, posCode):
        self.__posCode = posCode