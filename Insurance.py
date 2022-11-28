class Insurance:
    def __init__(self, MEMBERID, POLICYNO):
        self.MEMBERID = MEMBERID
        self.POLICYNO = POLICYNO

    def getPolicyNO(self):
        return self.POLICYNO

    def getMemberID(self):
        return self.MEMBERID
