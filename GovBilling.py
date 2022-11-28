class GovBilling:
    def __init__(self, billingNo, total, billingDate, billingCode, icd):
        self.__billingNo = billingNo
        self.__total = total
        self.__billingDate = billingDate
        self.__billingCode = billingCode
        self.__icd = icd

    def getTotal(self):
        return self.__total

    def getBillingNo(self):
        return self.__billingNo

    def getBillingDate(self):
        return self.__billingDate
