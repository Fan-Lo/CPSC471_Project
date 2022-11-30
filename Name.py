class Name:
    # def __init__(self, Fname, Lname, MiddleIn, Preferred):
    #     self.__Fname = Fname
    #     self.__Lname = Lname
    #     self.__MiddleIn = MiddleIn
    #     self.__Preferred = Preferred

    def __init__(self, *args ):
        # fullname, Fname, Lname, MiddleIn, Preferred

        #if full name is given
        if len(args) == 1:
            self.__fullName = args[0]
            self.parseName()
        
        # if name is given in parts. order in Fname, Lname, MiddleIn, Preferred
        else:
            self.__Fname = args[0]
            self.__Lname = args[1]
            self.__MiddleIn = args[2]
            self.__Preferred = args[3]

    
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
    
    #class method
    def getFullName(self):
        return self.__fullName
    
    def parseName(self):
        nameList = self.__fullName.split()
        self.__Fname = nameList[0].strip()
        self.__MiddleIn = nameList[1].strip()
        self.__Lname = nameList[2].strip()
    
    #static method 
    def concatName(self):
        if self.__Fname == self.__Preferred:
            name = f"{self.__fname} {mIN} {lname}"
        else:
            name = f"{fname} ({pname}) {mIN} {lname}"
        self.__Fname = name