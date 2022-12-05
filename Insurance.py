class Insurance:
    def __init__(self, policyNo, memberID):
        self.__MEMBERID = memberID
        self.__POLICYNO = policyNo

    def getPolicyNO(self):
        return self.__POLICYNO

    def getMemberID(self):
        return self.__MEMBERID
    
    def display(self):
        return f"{self.__MEMBERID} {self.__POLICYNO}"
