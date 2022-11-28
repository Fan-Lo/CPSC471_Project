class ReferralLetter:
    def __init__(self, Date, notes, EXAMID):
        self.__Date = Date
        self.__notes = notes
        self.__EXAMID = EXAMID

    def getDate(self):
        return self.__Date

    def getNotes(self):
        return self.__notes

    def CreateLetter(self):
        return ReferralLetter
