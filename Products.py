
class Products:
    def __init__(self, names, Supplier, cost, amountInStock):
        self.names = names
        self.Supplier = Supplier
        self.cost = cost
        self.amountInStock = amountInStock

    def getName(self):
        return self.names
    
    def getSupplier(self):
        return self.Supplier

    def setSupplier(self, s):
        self.Supplier = s

    def getCost(self):
        return self.cost

    def setCost(self, c):
        self.cost = c

    def getAmountInStock(self):
        return self.amountInStock
