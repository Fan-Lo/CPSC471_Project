class GovBilling:
    def __init__(self, billingNo, total, billingDate, billingCode, icd):
        self.billingNo = billingNo
        self.total = total
        self.billingDate = billingDate
        self.billingCode = billingCode
        self.icd = icd

    def getTotal(self):
        return self.total

    def getBillingNo(self):
        return self.billingNo

    def getBillingDate(self):
        return self.billingDate


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


class Service:
    def __init__(self, name, cost):
        self.name = name
        self.cost = cost

    def getName(self):
        return self.name

    def getCost(self):
        return self.cost
