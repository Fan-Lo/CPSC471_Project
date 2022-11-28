from PhoneNumber import PhoneNumber

class Patient:
    __patientPhone = []
    __invoice = []
    __insurance = []

    def __init__(self, phone, invoice, insurance, detail):
        self.__patientPhone = phone
        self.__invoice = invoice
        self.__insurance = insurance
        self.__examRecord = detail
    
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