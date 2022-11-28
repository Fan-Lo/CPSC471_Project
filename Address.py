class Address:
    def __init__(self, country=None, province=None, city=None, address=None, posCode=None):
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
    
    def parseAddress(self, address):
        addressList = address.split(',')
        self.__address = addressList[0].strip()
        self.__city = addressList[1].strip()
        self.__province = addressList[2].strip()
        self.__country = addressList[3].strip()
    
    def getAddress(self):
        return self.__address
    
    def getCountry(self):
        return self.__country
    
    def getCity(self):
        return self.__city
    
    def getProvince(self):
        return self.__province

# Testing parseAddress()  
'''
if __name__ == '__main__':
    add = Address()
    add.parseAddress("149 Sage Meadows Cir NW, Calgary, Alberta, Canada")
    print(add.getAddress())
    print(add.getCountry())
'''  

