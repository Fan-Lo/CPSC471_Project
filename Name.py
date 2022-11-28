class Name:
    def __init__(self, Fname, Lname, MiddleIn, Preferred):
        self.__Fname = Fname
        self.__Lname = Lname
        self.__MiddleIn = MiddleIn
        self.__Preferred = Preferred
    
    def setFname(self, f):
        self.__Fname = f
    
    def getFname(self):
        return self.__Fname
    
    def setLname(self,l):
        self.__Lname = l
    
    def getLname(self):
        return self.__Lname
    
    def setMiddleIn(self, m):
        self.__MiddleIn = m
    
    def getMiddleIn(self):
        return self.__MiddleIn
    
    def setPreferred(self, p):
        self.__Preferred = p
    
    def getPreferred(self):
        return self.__Preferred
    
    def getFullName(self):
        return f"{self.__Fname} ({self.__Preferred}) {self.__MiddleIn} {self.__Lname}"
    
    def parseName(self, name):
        nameList = name.split()
        self.__Fname = nameList[0]
        self.__MiddleIn = nameList[1]
        self.__Lname = nameList[2]