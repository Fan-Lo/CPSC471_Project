from ExamDetail import ExamDetail

class PastExamRecord:

    def __init__(self):
        self.__detail = []


    def getExamDetail(self, r):
        return self.__detail[r]
    
    def addExamDetail(self, examID):
        self.__detail.insert(examID, ExamDetail())