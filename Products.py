
class Products:
    def __init__(self, names, Supplier, cost):
        self.__names = names
        self.__Supplier = Supplier
        self.__cost = cost

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

