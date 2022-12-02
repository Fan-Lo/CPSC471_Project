from DatabaseConnect import *

class Address:
    def __init__(self, country=None, city=None, streetNum=None, streetName=None, posCode=None):
        # member vars: country, city, address, posCode, streetName, streetNum
        self.__country = country
        self.__city = city
        self.__streetNum = streetNum
        self.__streetName = streetName
        self.__posCode = posCode
    
    def setCountry(self, con):
        self.__country = con
        self.database = DatabaseConnect()
        self.database.insert(
        f"UPDATE PATIENT SET Country = '{con}' WHERE AHC = {self.__ahcNum}; ")
        self.database.close()
    
    def setCity(self, city):
        self.__city = city
        
    def setPostalCode(self, posCode):
        self.__posCode = posCode
    
    def setAddress(self, add):
        self.__streetName = ""
        self.__streetNum = ""
        addList = add.split()
        for i in addList:
            if i.isDigit():
                self.__streetNum += i
            else:
                self.__streetName += i
        
    
    def parseAddress(self, address):
        addressList = address.split()
        self.__StreetName = addressList[1].strip()
        self.__StreetNum = addressList[0].strip()
    
    def getPostalCode(self):
        return self.__posCode

    def getStreetNum(self): 
        return self.__streetNum
    
    def getStreetName(self):
        return self.__streetName
        
    def getCountry(self):
        return self.__country
    
    def getCity(self):
        return self.__city
    
    def getAddress(self):
        return self.__streetNum + " " + self.__streetName

# Testing parseAddress()  
'''
if __name__ == '__main__':
    add = Address()
    add.parseAddress("1 Sage Hill NW, Calgary, Alberta, Canada")
    print(add.getAddress())
    print(add.getCountry())
'''  

