from datetime import datetime 
from Products import Products
from Services import Service 

class Invoice:
    def __init__(self, invoiceID, invoiceDate):
        self.__invoiceID = invoiceID
        self.__invoiceDate = invoiceDate
        self.__contains = []
        self.__service = []
    
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
    
    def getInvoiceID(self):
        return self.__INVOICEID

    def getDate(self):
        return self.INVOICEDATE.strftime('%Y-%m-%d')
