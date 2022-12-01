from DatabaseConnect import *
from datetime import datetime

class Employee:
    def __init__(self, S = None):
        if(S != None):
            self.database = DatabaseConnect()
            if(S.isdigit() == True):
                self.employeeInfo = self.database.performQuery(f"SELECT * FROM EMPLOYEE;") # WHERE SIN = '{S}';")
            elif(S.isalpha() == True):
                self.employeeInfo = self.database.performQuery(f"SELECT * FROM EMPLOYEE WHERE LName = '{S}';")
            self.database.close()
            self.parseInfo()
        return

    def parseInfo(self):
        self.SIN = self.employeeInfo[0][0]
        self.phoneNum = self.employeeInfo[0][1]
        self.title = self.employeeInfo[0][2]
        self.superSIN = self.employeeInfo[0][3]
        self.DOB = self.employeeInfo[0][4]
        self.Fname = self.employeeInfo[0][5]
        self.MIn = self.employeeInfo[0][6]
        self.Lname = self.employeeInfo[0][7]

    def getName(self):
        return f'{self.Fname} {self.MIn}. {self.Lname}'
    
    def getSIN(self):
        return self.SIN
    
    def verifySuper(self):
        if (self.superSIN == self.SIN):
            return True
        return False
    
    def deleteEmp(self):
        self.database = DatabaseConnect()
        self.database.insert(f"DELETE FROM EMPLOYEE_LOGIN WHERE Username = '{self.SIN}';")
        self.database.insert(f"DELETE FROM EMPLOYEE WHERE SIN = '{self.SIN}';")
        self.database.close()

    def addEmp(self, SIN, phone, title, supSIN, DOB, name, password):
        DOB = datetime.strptime(DOB, '%Y-%m-%d')
        name = name.split(' ')
        self.SIN = SIN
        self.phoneNum = phone
        self.title = title
        self.superSIN = supSIN
        self.DOB = DOB
        self.Fname = name[0]
        self.MIn = name[1][0]
        self.Lname = name[-1]
        self.database = DatabaseConnect()
        self.database.insert(f"INSERT INTO EMPLOYEE VALUES ('{SIN}', '{phone}', '{title}', '{supSIN}', '{DOB}', '{self.Fname}', '{self.MIn}', '{self.Lname}');")
        self.database.insert(f"INSERT INTO EMPLOYEE_LOGIN VALUES ('{SIN}', '{password}');")
        self.database.close()


if __name__ == "__main__":
    emp = Employee('525252525')
    print(emp.getName())

    emp = Employee('White')
    print(emp.getSIN())

