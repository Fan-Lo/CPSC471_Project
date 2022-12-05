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
        phones = self.database.performQuery(f"SELECT * FROM PATIENT_PHONE WHERE AHC = {AHC};")
        examDetails = self.database.performQuery(f"SELECT * FROM EXAM_DETAIL WHERE PatAHC = {AHC};")
        self.database.close()
        
        # empty lists, list is populated from db when needed
        self.__invoice = []
        self.__insurance = []
        self.__examDetails = []



        #parse attributes stored in PATIENT Table
        self.parsePxInfo(pxInfo)

        #parse attributes stored in PATIENT_PHONE table
        phones = self.parsingDatabaseTuples(phones,[1])
        self.__patientPhone = []
        for i in phones:
            self.__patientPhone.append(PhoneNumber(i[0]))


    #getters for whole Lists
    def getAllInvoices(self):
        #haven't retrieve invoice from database
        if len(self.__invoice) == 0 : 
            self.database = DatabaseConnect()
            invoices = self.database.performQuery(f"SELECT * FROM INVOICE WHERE PatAHC = {self.__ahcNum};")
            self.database.close()
            #parse attributes stored in INVOICE table
            invoices = self.parsingDatabaseTuples(invoices,[0, 1, 2, 3])
            for i in invoices:
                self.__invoice.append(Invoice(i[0], i[2]))
        return self.__invoice

    def getAllInsurances(self):
        if len(self.__insurance) == 0:
            self.database = DatabaseConnect()
            insurances = self.database.performQuery(f"SELECT * FROM INSURANCE WHERE PatAHC = {self.__ahcNum};")
            self.database.close()
            #parse attributes stored in INSURANCE table
            insurances = self.parsingDatabaseTuples(insurances,[0, 1])

            for i in insurances:
                self.__insurance.append(Insurance(i[0],i[1]))
        return self.__insurance

    def getAllExamDetails(self):
        if len(self.__examDetails) == 0:
            self.database = DatabaseConnect()
            examDetails = self.database.performQuery(f"SELECT * FROM EXAM_DETAIL WHERE PatAHC = {self.__ahcNum};")
            self.database.close()
            print(examDetails)
            #parse attributes stored in EXAM_DETAIL table
            examDetails = self.parsingDatabaseTuples(examDetails,[0,2,3,4])
            for i in examDetails:
                self.__examDetails.append(ExamDetail(i[0],i[1],i[2],i[3]))
        return self.__examDetails


    def addPatient(self, AHC, sex, DOB, name,  address, City, Country, PostalCode, HeadAHC=None):
        # simple attributes
        self.__ahcNum = AHC
        self.__sex = sex
        self.__DOB = datetime.strptime(DOB, '%Y-%m-%d')
        if HeadAHC != None:
            self.__headAHC = HeadAHC
        else:
            self.__headAHC = AHC

        # composite attributes 
        self.__name = Name(name)

        add = address.split(' ')
        streetNum = ""
        streetName = ""
        for i in add:
            if i.isdigit():
                streetNum += i
                streetNum += " "
            else:
                streetName += i
                streetName += " "
        self.__address = Address(Country, City, streetNum, streetName, PostalCode)

        # update detabase Patient table
        self.database = DatabaseConnect()
        self.database.insert(f"INSERT INTO PATIENT VALUES( '{self.__ahcNum}', '{self.__sex}',  '{self.__DOB}', '{self.__name.getFname()}', '{self.__name.getMiddleIn()}', '{self.__name.getLname()}', '{self.__name.getFname()}', '{self.__headAHC}', '{self.__address.getStreetName()}', '{self.__address.getStreetNum()}', '{self.__address.getCity()}', '{self.__address.getCountry()}', '{self.__address.getPostalCode()}');")
        self.database.insert(f"INSERT INTO PATIENT_LOGIN VALUES( '{self.__ahcNum}', '{self.__name.getLname()}');")
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

        
    def parsingDatabaseTuples(self, tuples, attributePosition):
        list = [[] for _ in range(len(tuples))]
        for i in range(len(tuples)): # i is number of database entry
            for j in attributePosition:
                    list[i].append(tuples[i][j])
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
    
    #getters for individual item in the lists
    def getInvoice(self, index):
        return self.getAllInvoices()[index]
    
    def getPastExamRecord(self, index):
        return self.getAllExamDetails()[index]
    
    def setName(self, name):
        if self.__name.getFullName() != name:
            self.__name.setFullName(name)
            self.database = DatabaseConnect()
            self.database.insert(
                f"UPDATE PATIENT SET FName = '{self.__name.getFname()}', MidIN = '{self.__name.getMiddleIn()}', LName = '{self.__name.getLname()}', PName = '{self.__name.getPreferred()}' WHERE AHC = {self.__ahcNum}; ")
            self.database.close()
    
    #invoiceID is autogenerated
    def addNewInvoice(self, invoiceDate, products, services):
        self.database = DatabaseConnect()
        self.database.insert
        ("INSERT INTO INVOICE WHERE AHC")


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
        str = self.__name.getFullName() + "\n"
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
    
    def setAddress(self, address, city, country, postalcode):
        self.database = DatabaseConnect()

        if self.__address.getAddress() != address:
            self.__address.parseAddress(address)
            self.database.insert(
            f"UPDATE PATIENT SET StreetName = '{self.__address.getStreetName()}', StreetNum= '{self.__address.getStreetNum()}' WHERE AHC = {self.__ahcNum}; ")
        
        if self.__address.getCity() != city:
            self.__address.setCity(city)
            self.database.insert(
            f"UPDATE PATIENT SET City = '{city}' WHERE AHC = {self.__ahcNum}; ")
        
        if self.__address.getCountry() != country:
            self.__address.setCountry(country)
            self.database.insert(
            f"UPDATE PATIENT SET Country = '{country}' WHERE AHC = {self.__ahcNum}; ")
        
        if self.__address.getPostalCode() != country:
            self.__address.setPostalCode(postalcode)
            self.database.insert(
            f"UPDATE PATIENT SET PostalCode = '{self.__address.getPostalCode()}' WHERE AHC = {self.__ahcNum}; ")

        self.database.close()


    def searchPatient(self, AHC):
        self.database = DatabaseConnect()
        self.AHC = self.database.performQuery(f"SELECT AHC FROM PATIENT;")
        i = 0
        while i < len(self.AHC):
            if AHC in self.AHC[i]:
                return True
            i += 1

        return False

    def addInsurance(self, memberID, policyNo):
        if len(self.__insurance) == 0:
            self.__insurance.append(Insurance(memberID, policyNo))
            self.database = DatabaseConnect()
            self.database.insert(f"INSERT INTO INSURANCE VALUES ('{policyNo}', '{memberID}', '{self.__name.getFullName()}','{self.__ahcNum}'); ")
            self.database.close()
            return
        for i in self.__insurance:
            if i.getPolicyNo() != policyNo and i.getMemberID() != memberID:
                self.__insurance.append(Insurance(memberID, policyNo))
                self.database = DatabaseConnect()
                self.database.insert(f"INSERT INTO INSURANCE VALUES ('{policyNo}', '{memberID}', '{self.__name.getFullName()}','{self.__ahcNum}'); ")
                self.database.close()
                break
        
# if __name__ == '__main__':
    
    # px = Patient('123456789')
    # px.setName('Mike T Ann')
    # px.setDOB('1996-08-09')
    # px.setSex('f')
    # px.setAddress('111 Test Street', 'test city', 'testContry', 'T1T 1T1')
    # for i in px.getAllInsurances():
    #     print(i.display())
    # database = DatabaseConnect()
    # insurances = database.performQuery(f"SELECT * FROM INSURANCE WHERE PatAHC = 113456789;")
    # print(insurances)

    # def parsingDatabaseTuples(self, tuples, numOfAttributes):
    # list = [[""]*numOfAttributes]*len(tuples)
    # for i in tuples:
    #     for j in range(numOfAttributes):
    #             list.append(i[j])
    # return list
    # px.addInsurance('101','2322')

    # print(list[0].display())
    # px.addPatientPhone('4032223333')
    # px.addPatientPhone('403','888','9999')
    # px.removePhoneNumber('4031111111')
    # px.addPatient(222222222,'f','1996-06-06','Test m Test','111 Test Rd','TestCity','TestCountry','T1T 0T0')
    # px = Patient()
    # print(px.verifyAHC('hello'))
    # print(px.verifyAHC('123'))
    # print(px.verifyAHC('123456789'))
