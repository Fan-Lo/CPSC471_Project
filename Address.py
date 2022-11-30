class Address:
    def __init__(self, country=None, city=None, address=None, posCode=None):
        # member vars: country, city, address, posCode, 
        self.__country = country
        self.__city = city
        self.__address = address
        self.parseAddress(address)
        self.__posCode = posCode
    
    def setCountry(self, con):
        self.__country = con
    
    def setCity(self, city):
        self.__city = city
    
    def setAddress(self, address):
        self.__address = address
        
    def setPostalCode(self, posCode):
        self.__posCode = posCode
    
    def parseAddress(self, address):
        addressList = address.split()
        self.__StreetName = addressList[1].strip()
        self.__StreetNum = addressList[0].strip()
    
    def getPostalCode(self):
        return self.__posCode

    def getAddress(self):
        return self.__address
    
    def getCountry(self):
        return self.__country
    
    def getCity(self):
        return self.__city
    

# Testing parseAddress()  
'''
if __name__ == '__main__':
    add = Address()
    add.parseAddress("149 Sage Meadows Cir NW, Calgary, Alberta, Canada")
    print(add.getAddress())
    print(add.getCountry())
'''  

