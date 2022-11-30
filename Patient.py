from PhoneNumber import PhoneNumber
from PastExamRecord import PastExamRecord
from datetime import date
from DatabaseConnect import *

class Patient:

    # retrieves inforamtion from the patient table
    def __init__(self, AHC=None):
        # do nothing if it's an default ctor
        if AHC == None :
            return
        self.__ahcNum = AHC
        self.database = DatabaseConnect()
        self.pxInfo = self.database.performQuery(f"SELECT * FROM PATIENT WHERE AHC = {AHC};")
        self.__phone = self.database.performQuery(f"SELECT PhoneNum FROM PATIENT_PHONE WHERE AHC = {AHC};")
        self.__invoice = self.database.performQuery(f"SELECT PhoneNum FROM INVOICE WHERE PatAHC = {AHC};")
        self.__insurance = self.database.performQuery(f"SELECT PhoneNum FROM INSURANCE WHERE PatAHC = {AHC};")
        self.__examDetails = self.database.performQuery(f"SELECT PhoneNum FROM EXAM_DETAIL WHERE PatAHC = {AHC};")
        self.database.close()
        self.parseInfo()

    def addPatient(self, AHC, sex, DOB, Nname, address, City, Country, PostalCode, HeadAHC=None):
        self.__name = name
        self.__ahcNum = ahc
        self.__DOB = DOB
        self.__sex = sex
        self.__patientPhone = []
        self.__patientPhone.append(phone)
        self.createPatientSQL()
    
    # def createPatientSQL(self):
    #     self.database = DatabaseConnect()
    #     self.database.performQuery(
    #         "INSERT INTO PATIENT VALUES" +
    #         f"({self.__ahcNum}, {self.__sex}, {self.__DOB})"
    #     )
    #     self.database.close()
    
    def parseInfo(self):
        self.__name = self.concatName(self.pxInfo[0][3],self.pxInfo[0][4],self.pxInfo[0][5],self.pxInfo[0][6])
        self.__DOB = self.pxInfo[0][1]
        self.__sex = self.pxInfo[0][1]
        
        self.__phone = self.parsingDatabaseTuples(self.__phone)
        self.__invoice = self.parsingDatabaseTuples(self.__invoice)
        self.__insurance = self.parsingDatabaseTuples(self.__insurance)
        self.__examDetails = self.parsingDatabaseTuples(self.__examDetails)

    def parsingDatabaseTuples(self, tuples):
        list = []
        for i in tuples:
            list.append(i[0])
        return list

    def concatName(self,fname, mIN, lname, pname):
        if fname == pname:
            name = f"{fname} {mIN} {lname}"
        else:
            name = f"{fname} ({pname}) {mIN} {lname}"
        return name

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
    
    def getName(self):
        return self.__name
    
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
    
    def verifyAHC(self, ahc):
        result = ahc.isdigit()
        if len(ahc) != 9 :
            result = False
        return result
    
    def getPhone(self):
        return self.__phone

'''
if __name__ == '__main__':
    px = Patient()
    print(px.verifyAHC('hello'))
    print(px.verifyAHC('123'))
    print(px.verifyAHC('123456789'))
'''

if __name__ == '__main__':
    px = Patient('123456789')
    print(px.getName())
    print(px.getPhone())
 