class ExamDetail:
    __performedBy = []

    def __init__(self, id, notes, m, d, r=False):
        self.__examID = id
        self.__notes = notes
        self.__performedBy = m
        self.__date = d
        self.__referral = r

    def getExamID(self):
        return self.__examID
    
    def getPerfroemd(self):
        return self.__performedBy
    
    def getNotes(self):
        return self.__notes
    
    def ReferralRequired(self):
        return self.__referral
    
    def getDate(self):
        return self.__date
    
    def setPerformedBy(self, m):
        self.__performedBy = m