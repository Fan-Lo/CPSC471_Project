from Patient import Patient
from Address import Address

class Family:
    def __init__(self):
        self.__head = None
        self.__members = []
        self.__address = None
    
    def setHead(self, ahc):
        for i in self.__members:
            if i.getAHC() == ahc:
                self.__head = i
                break
    
    def addMember(self, name, ahc, DOB, sex, phoneNum=None):
        self.__members.append(Patient(name, ahc, DOB,sex,phoneNum))
    
    def removeMember(self, ahc):
        for i in self.__members:
            if i.getAHC() == ahc:
                self.__members.remove(i)
    
    def setAddress(self, country, province, city, address, posCode):
        self.__address = Address(country, province, city, address, posCode)
        return 