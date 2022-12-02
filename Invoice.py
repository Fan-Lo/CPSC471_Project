from Products import Products
from Services import Service 

class Invoice:
    def __init__(self, PATIENTSIN, INVOICEID, total):
        self.__PATIENTSIN = PATIENTSIN
        self.__INVOICEID = INVOICEID
        self.__total = total
        self.__contains = []
        self.__service = []

    def Invoice(self, s, p):
        self.__service = self.__service.Service(s)
        self.__contains = self.__contains.Products(p)

    def Invoice(self, s):
        self.__service = self.__service.Service(s)

    def Invoice(self, p):
        self.__contains = self.__contains.Products(p)
    
    def calculateTotal(self):
        return self.__total 

    def calculateTax(self):
        return self.__total * 0.05

    def addProduct(self, p):
        self.__contains.append(Products(p))

    def removeProduct(self, p):
        for i in self.__contains:
            if i.names == p:
                self.__contains.remove(i)

    def addService(self, s):
        self.__service.append(Service(s))

    def getPatientSIN(self):
        return self.__PATIENTSIN
    
    def getInvocieID(self):
        return self.__INVOICEID
