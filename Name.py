class Name:
    def __init__(self, Fname, Lname, MiddleIn, Preferred):
        self.Fname = Fname
        self.Lname = Lname
        self.MiddleIn = MiddleIn
        self.Preferred = Preferred
    
    def setFname(self, f):
        self.Fname = f
    
    def getFname(self):
        return self.Fname
    
    def setLname(self,l):
        self.Lname = l
    
    def getLname(self):
        return self.Lname
    
    def setMiddleIn(self, m):
        self.MiddleIn = m
    
    def getMiddleIn(self):
        return self.MiddleIn
    
    def setPreferred(self, p):
        self.Preferred = p
    
    def getPreferred(self):
        return self.Preferred
    
    def getFullName(self):
        return f"{self.Fname} ({self.Preferred}) {self.MiddleIn} {self.Lname}"