class ReferralLetter:
    def __init__(self, Date, notes, EXAMID):
        self.Date = Date
        self.notes = notes
        self.EXAMID = EXAMID

    def getDate(self):
        return self.Date

    def getNotes(self):
        return self.notes

    def CreateLetter(self):
        return ReferralLetter
