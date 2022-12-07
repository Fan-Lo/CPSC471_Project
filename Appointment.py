from DatabaseConnect import *
from Employee import * 
from Patient import *
from datetime import datetime 

class Appointment:
    def __init__(self):
        pass

    def addAppointment(self, AHC, d, t, name):
        SIN = Employee(name).getSIN()
        self.database = DatabaseConnect()
        dt = d + ' ' + t
        dt = datetime.strptime(dt, '%Y-%m-%d %I:%M')
        self.newAppointment = self.database.insert(f"INSERT INTO APPOINTMENT VALUES ('{AHC}', '{SIN}', '{dt}');")
        #print(self.newAppointment)
        self.database.close()

    def viewAppointments(self, SIN):
        self.database = DatabaseConnect()
        self.appointments = self.database.performQuery(f"SELECT * FROM APPOINTMENT WHERE MedStaffSIN = '{SIN}';")
        self.database.close()
        if(len(self.appointments) == 0):
            return 'You have no appointments currently'

        i = 0
        format = ''
        while (i < len(self.appointments)):
            num = i+1
            format += 'Appointment ' + str(num) + ': \n'
            format += '     ' + 'Patient AHC: ' + self.appointments[i][0] + '\n'
            self.employee = Employee(self.appointments[i][1])
            format += '     ' + 'Employee Name: ' + self.employee.getName() + '\n'
            dt = self.appointments[i][2].strftime('%Y-%m-%d %I:%M')
            format += '     ' + 'Date and Time: ' + dt + '\n'
            i += 1
            
        return format

    def viewPAppointments(self, AHC):
        self.database = DatabaseConnect()
        self.appointments = self.database.performQuery(f"SELECT * FROM APPOINTMENT WHERE PatAHC = '{AHC}';")
        self.database.close()
        if(len(self.appointments) == 0):
            return 'You have no appointments currently'

        i = 0
        format = ''
        while (i < len(self.appointments)):
            num = i+1
            format += 'Appointment ' + str(num) + ': \n'
            format += '     ' + 'Patient AHC: ' + self.appointments[i][0] + '\n'
            self.employee = Employee(self.appointments[i][1])
            format += '     ' + 'Employee Name: ' + self.employee.getName() + '\n'
            dt = self.appointments[i][2].strftime('%Y-%m-%d %I:%M')
            format += '     ' + 'Date and Time: ' + dt + '\n'
            i += 1
            
        return format

    def deleteAppointment(self,AHC, d, t):
        #SIN = Employee(name).getSIN()
        self.database = DatabaseConnect()
        dt = d + ' ' + t
        dt = datetime.strptime(dt, '%Y-%m-%d %I:%M')
        self.newAppointment = self.database.insert(f"DELETE FROM APPOINTMENT WHERE PatAHC = '{AHC}' AND ApptTime ='{dt}';")
        #print(self.newAppointment)
        self.database.close()

if __name__ == "__main__":
    app = Appointment()
    app.addAppointment('123456789', '2022-11-28', '01:15:00', 'White')
    print(app.viewAppointments())
    app.deleteAppointment('123456789', '2022-11-28', '01:15:00', 'White')
    print(app.viewAppointments())