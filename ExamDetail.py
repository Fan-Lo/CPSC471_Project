from DatabaseConnect import *
from datetime import datetime 
import datetime

class ExamDetail:
    __performedBy = []

    def __init__(self, id = None, d = None, notes = None, m = None, r=False):
        self.__examID = id
        self.__notes = notes
        self.__performedBy = m
        self.__date = d
        self.__referral = r

    def getExamID(self):
        return self.__examID
    
    def getPerformed(self):
        return self.__performedBy
    
    def getNotes(self):
        return self.__notes
    
    def ReferralRequired(self):
        return self.__referral
    
    def getDate(self):
        return self.__date
    
    def setPerformedBy(self, m):
        self.__performedBy = m

    def viewExamDetail(self, AHC):
        self.database = DatabaseConnect()
        self.exam_details = self.database.performQuery(f"SELECT * FROM EXAM_DETAIL WHERE PatAHC = '{AHC}';")
        self.database.close()
        if(len(self.exam_details) == 0):
            return 'You have no exam details to display'

        i = 0
        format = ''
        while (i < len(self.exam_details)):
            num = i+1
            format += ' Exam Detail ' + str(num) + ': \n'
            format += '     ' + 'Exam ID: ' + str(self.exam_details[i][0]) + '\n'
            format += '     ' + 'Patient AHC: ' + str(self.exam_details[i][1]) + '\n'
            
            # dt = self.exam_details[i][2].strftime('%Y-%m-%d')
            
            # format += '     ' + 'Date' + dt + '\n'
            format += '     ' + 'Notes: ' + str(self.exam_details[i][3]) + '\n'
            format += '     ' + 'Performed By: ' + str(self.exam_details[i][4]) + '\n' 
            i += 1
        return format