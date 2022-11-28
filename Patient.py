from PhoneNumber import PhoneNumber
from PastExamRecord import PastExamRecord
from datetime import date

class Patient:

    def __init__(self, name, ahc, DOB, sex, phone):
        self.__name = name
        self.__ahcNum = ahc
        self.__DOB = DOB
        self.__sex = sex
        self.__patientPhone = []
        self.__patientPhone.append(phone)
        self.__invoice = []
        self.__insurance = []
        self.__examRecord = PastExamRecord()
    
    def getPatientPhone(self):
        return self.__patientPhone
    

    def addPatientPhone(self, area, tel, line, country=None, extension=None):
        phone = PhoneNumber(area,tel, line,country, extension)
        self.__patientPhone.append(phone)

    def removePhoneNumber(self, p):
        for i in self.__patientPhone:
            if p == i.displayFull():
                self.__patientPhone.remove(i)
                break
    
    def getInvoice(self, index):
        return self.__invoice[index]
    
    def getPastExamRecord(self, index):
        return self.__examRecord[index]
    
    def getInsurnace(self):
        return self.__insurance
    
    def setName(self, name):
        self__name = name
    
    def setAHC(self, num):
        self.__ahcNum = num
    
    def setDOB(self, date):
        self.__DOB = date
    
    def setSex(self, sex):
        self.__sex = sex
    
    def displayInfo(self):
        str = self.__name.getFullname() + "\n"
        str += self.__ahcNum + "\n"
        str += self.__DOB + "\n"
        return str

    def calcAge(self):
        today = date.today()
        return today.year - self.__DOB.year - ((today.month, today.day) < (self.__DOB.month, self.__DOB.day))

    def getAHC(self):
        return self.__ahcNum