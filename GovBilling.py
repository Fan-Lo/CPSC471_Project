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
