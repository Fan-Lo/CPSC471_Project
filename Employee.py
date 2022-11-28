from DatabaseConnect import *
from datetime import datetime

class Employee:
    def __init__(self, S):
        self.SIN = S
        self.database = DatabaseConnect()
        self.employeeInfo = self.database.performQuery(f"SELECT * FROM EMPLOYEE WHERE SIN = '{S}';")
        self.database.close()
        self.parseInfo()

    def parseInfo(self):
        self.phoneNum = self.employeeInfo[0][1]
        self.title = self.employeeInfo[0][2]
        self.superSIN = self.employeeInfo[0][3]
        self.DOB = self.employeeInfo[0][4]
        self.Fname = self.employeeInfo[0][5]
        self.MIn = self.employeeInfo[0][6]
        self.Lname = self.employeeInfo[0][7]

    def getName(self):
        return f'{self.Fname} {self.MIn}. {self.Lname}'


if __name__ == "__main__":
    emp = Employee('987654321')
    print(emp.getName())

