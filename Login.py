from DatabaseConnect import *

class Login:
    def __init__(self):
        self.connect()
        
    def connect(self):
        self.database = DatabaseConnect()
    
    def close(self):
        self.database.close()

    def verifyPatient(self, u, p):
        self.patient_login = self.database.getTable('*', 'PATIENT_LOGIN')

        i = 0
        while i < len(self.patient_login):
            if u in self.patient_login[i] and p in self.patient_login[i]:
                return True
            i += 1

        return False

    def verifyEmployee(self, u, p):
        self.employee_login = self.database.getTable('*', 'EMPLOYEE_LOGIN')

        i = 0
        while i < len(self.employee_login):
            if u in self.employee_login[i] and p in self.employee_login[i]:
                return True
            i += 1

        return False


if __name__ == "__main__":
    login = Login()
    login.verifyPatient('123456789', 'password')
    login.close()