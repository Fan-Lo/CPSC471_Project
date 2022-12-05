from datetime import datetime 
from Products import Products
from Services import Service 
from DatabaseConnect import *

class Invoice:
    def __init__(self, invoiceID, invoiceDate,  fromDB=True):
        
        self.__invoiceID = invoiceID
        self.__invoiceDate = invoiceDate
        self.__contains = []
        self.__service = []
        self.database = DatabaseConnect()

        if fromDB:
            productIDs = self.database.performQuery(f"SELECT * FROM CONTAINS WHERE InvoiceID = {invoiceID}")
            productIDs = self.parsingDatabaseTuples(productIDs, [0])
            for i in productIDs:
                product = self.database.performQuery(f"SELECT * FROM PRODUCTS WHERE ID = {i[0]};")
                product = self.parsingDatabaseTuples(product,[1,2,3])
                for j in product:
                    self.__contains.append(Products(j[0],j[1],j[2]))

        self.database.close()

        
    def parsingDatabaseTuples(self, tuples, attributePosition):
        # print(tuples)
        list = [[] for _ in range(len(tuples))]
        for i in range(len(tuples)): # i is number of database entry
            for j in attributePosition:
                    list[i].append(tuples[i][j])
        return list

    def calculateTotal(self):
        total = 0
        for i in self.__contains:
            total += i.getCost()
        return total*1.05 #tax included

    def calculateTax(self, amount):
        return amount*0.05

    def getProducts(self):
        return self.__contains

    def addProduct(self, p, pxAHC):
        self.__contains.append(Products(p,self.getProductSupplierFromName(p),self.getProductCostFromName(p)))
        productID = self.getProductIDFromName(p)
        self.database = DatabaseConnect()
        self.database.insert(f"INSERT INTO CONTAIN VALUES ({productID}, {self.__invoiceID}, {pxAHC});")
        self.database.close()


    def removeProduct(self, p, pxAHC):
        for i in self.__contains:
            if i.getName() == p:
                self.__contains.remove(i)
                self.database = DatabaseConnect()
                self.database.insert(f"DELETE FROM CONTAINS WHERE ProductID = {self.getProductIDFromName(p)} AND PatAHC = {pxAHC};")
                self.database.close()

    def addService(self, s):
        self.__service.append(Service(s))

    # def getPatientSIN(self):
    #     return self.__PATIENTSIN
    
    def getInvoiceID(self):
        return self.__invoiceID

    def getDate(self):
        return self.__invoiceDate.strftime('%Y-%m-%d')
    
    def getProductIDFromName(self, p):
        self.database = DatabaseConnect()
        productID = self.database.performQuery(f"SELECT ID FROM PRODUCTS WHERE PName = '{p}';")
        self.database.close()
        return productID[0][0]
    
    def getProductSupplierFromName(self, p):
        self.database = DatabaseConnect()
        productID = self.database.performQuery(f"SELECT Supplier FROM PRODUCTS WHERE PName = '{p}';")
        self.database.close()
        return productID[0][0]
    
    def getProductCostFromName(self, p):
        self.database = DatabaseConnect()
        productID = self.database.performQuery(f"SELECT cost FROM PRODUCTS WHERE PName = '{p}';")
        self.database.close()
        return productID[0][0]
        

