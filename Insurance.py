class Insurance:
    def __init__(self, MEMBERID, POLICYNO):
        self.__MEMBERID = MEMBERID
        self.__POLICYNO = POLICYNO

    def getPolicyNO(self):
        return self.__POLICYNO

    def getMemberID(self):
        return self.__MEMBERID
