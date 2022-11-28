
class Products:
    def __init__(self, names, Supplier, cost, amountInStock):
        self.__names = names
        self.__Supplier = Supplier
        self.__cost = cost
        self.__amountInStock = amountInStock

    def getName(self):
        return self.__names
    
    def getSupplier(self):
        return self.__Supplier

    def setSupplier(self, s):
        self.__Supplier = s

    def getCost(self):
        return self.__cost

    def setCost(self, c):
        self.__cost = c

    def getAmountInStock(self):
        return self.__amountInStock
