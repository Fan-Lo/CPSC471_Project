from PhoneNumber import PhoneNumber
from datetime import datetime, date
from DatabaseConnect import *
from Name import *
from Address import *
from Invoice import *
from Insurance import *
from ExamDetail import *

class Patient:

    # retrieves inforamtion from the patient table
    def __init__(self, AHC=None):
        # do nothing if it's an default ctor
        if AHC == None :
            return
        self.__ahcNum = AHC
        self.database = DatabaseConnect()
        pxInfo = self.database.performQuery(f"SELECT * FROM PATIENT WHERE AHC = {AHC};")
        phones = self.database.performQuery(f"SELECT PhoneNum FROM PATIENT_PHONE WHERE AHC = {AHC};")
        invoices = self.database.performQuery(f"SELECT * FROM INVOICE WHERE PatAHC = {AHC};")
        insurances = self.database.performQuery(f"SELECT * FROM INSURANCE WHERE PatAHC = {AHC};")
        examDetails = self.database.performQuery(f"SELECT * FROM EXAM_DETAIL WHERE PatAHC = {AHC};")
        self.database.close()
        
        #parse attributes stored in PATIENT Table
        self.parsePxInfo(pxInfo)

        #parse attributes stored in PATIENT_PHONE table
        phones = self.parsingDatabaseTuples(phones)
        self.__patientPhone = []
        for i in phones:
            self.__patientPhone.append(PhoneNumber(i))

        #parse attributes stored in INVOICE table
        invoices = self.parsingDatabaseTuples(invoices)
        self.__invoice = []
        for i in invoices:
            self.__invoice.append(Invoice(i))

        #parse attributes stored in INSURANCE table
        insurances = self.parsingDatabaseTuples(insurances)
        self.__insurance = []
        for i in insurances:
            self.__insurance.append(Insurance(i))

        #parse attributes stored in EXAM_DETAIL table
        examDetails = self.parsingDatabaseTuples(examDetails)
        self.__examDetails = []
        for i in examDetails:
            self.__examDetails.append(ExamDetail(i))

    def addPatient(self, AHC, sex, DOB, name,  address, City, Country, PostalCode, HeadAHC=None):
        # simple attributes
        self.__ahcNum = AHC
        self.__sex = sex
        self.__DOB = datetime.strptime(DOB, '%Y-%m-%d')
        if HeadAHC == None:
            self.headAHC = AHC
        else:
            self.headAHC = HeadAHC

        # composite attributes 
        self.__name = Name(name)

        add = address.split(' ')
        streetNum = ""
        streetName = ""
        for i in add:
            if i.isdigit():
                streetNum += i
            else:
                streetName += i
        self.__address = Address(Country, City, streetNum, streetName, PostalCode)

        # update detabase Patient table
        self.database = DatabaseConnect()
        self.database.insert(
            "INSERT INTO PATIENT VALUES" +
            f"('{self.__ahcNum}', '{self.__sex}', '{self.__DOB}','{self.__name.getFname()}', '{self.__name.getMiddleIn()}', '{self.__name.getLname()}', '{self.__name.getPreferred()}', '{self.__headAHC}', '{self.__address.getStreetName()}', '{self.__address.getStreetNum()}', '{self.__address.getCity()}', '{self.__address.getCity()}', '{self.__address.getPostalCode()}');"
        )
        self.database.insert(f"INSERT INTO PATIENT_LOGIN VALUES ('{self.__ahcNum}', '{self.__name.getLname().lower()}');")
        self.database.close()
    
    def deletePatient(self):
        self.database = DatabaseConnect()
        self.database.insert(f"DELETE FROM PATIENT WHERE AHC = '{self.__ahcNum}';")
        self.database.close()


    def parsePxInfo(self, info):
        self.__name = Name(info[0][3],info[0][4],info[0][5],info[0][6])
    
        self.__DOB = info[0][2]
        self.__sex = info[0][1]
        self.__headAHC = info[0][7]

        self.__address = Address(info[0][11], info[0][10], info[0][9], info[0][8], info[0][12])

        
    def parsingDatabaseTuples(self, tuples):
        list = []
        for i in tuples:
            list.append(i[0])
        return list

    def getPatientPhone(self):
        return self.__patientPhone 
    

    def addPatientPhone(self, p):
        phone = PhoneNumber(p)
        self.__patientPhone.append(phone)
        self.database = DatabaseConnect()
        self.database.insert(f"INSERT INTO PATIENT_PHONE VALUES ('{self.__ahcNum}', '{phone.display()}'); ")
        self.database.close()

    def removePhoneNumber(self, p):
        for i in self.__patientPhone:
            if p == i.display():
                self.__patientPhone.remove(i)
                self.database = DatabaseConnect()
                self.database.insert(f"DELETE FROM PATIENT_PHONE WHERE AHC = '{self.__ahcNum}' AND PhoneNum = '{i.display()}';")
                self.database.close()
                break
    
    def getInvoice(self, index):
        return self.__invoice[index]
    
    def getPastExamRecord(self, index):
        return self.__examRecord[index]
    
    def getInsurnace(self):
        return self.__insurance
    
    def setName(self, name):
        if self.__name.getFullName() != name:
            self.__name.setFullName(name)
            self.database = DatabaseConnect()
            self.database.insert(
                f"UPDATE PATIENT SET FName = '{self.__name.getFname()}', MidIN = '{self.__name.getMiddleIn()}', LName = '{self.__name.getLname()}', PName = '{self.__name.getPreferred()}' WHERE AHC = {self.__ahcNum}; ")
            self.database.close()
    
    def getName(self):
        return self.__name
    
    def setDOB(self, date):
        self.__DOB = date
        dt = datetime.strptime(date,'%Y-%m-%d')
        self.database = DatabaseConnect()
        self.database.insert(
            f"UPDATE PATIENT SET DOB = '{dt}' WHERE AHC = {self.__ahcNum}; ")
        self.database.close()
    
    def getDOB(self):
        dt = self.__DOB.strftime('%Y-%m-%d')
        return self.__DOB

    def setSex(self, sex):
        self.__sex = sex.upper()
        self.database = DatabaseConnect()
        self.database.insert(
            f"UPDATE PATIENT SET SEX = '{sex.upper()}' WHERE AHC = {self.__ahcNum}; ")
        self.database.close()
    
    def getSex(self):
        return self.__sex

    def displayInfo(self):
        str = self.__name.getFullname() + "\n"
        #invoice, insurance, exam detail, appointment
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
        return self.__patientPhone
    
    def getAddress(self):
        return self.__address

    def searchPatient(self, AHC):
        self.database = DatabaseConnect()
        self.AHC = self.database.performQuery(f"SELECT AHC FROM PATIENT;")
        print(self.AHC)
        i = 0
        while i < len(self.AHC):
            if AHC in self.AHC[i]:
                return True
            i += 1

        return False


'''
if __name__ == '__main__':
    px = Patient()
    print(px.verifyAHC('hello'))
    print(px.verifyAHC('123'))
    print(px.verifyAHC('123456789'))
'''

if __name__ == '__main__':
    px = Patient('113456789')
    px.setName('Mike T Ann')
    px.setDOB('1996-08-09')
    px.setSex('F')
    px.addPatientPhone('4032223333')
    # px.addPatientPhone('403','888','9999')
    # px.removePhoneNumber('4031111111')
    # px.addPatient(222222222,'f','1996-06-06','Test m Test','111 Test Rd','TestCity','TestCountry','T1T 0T0')
