from Login import *
from Employee import * 
from DatabaseConnect import *
from AppointmentScreens import *
from EditEmployeeScreens import *
from EmployeePatientScreens import *

from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window
from kivy.uix.popup import Popup

Window.clearcolor = (1, 1, 1, 1)    #Sets Background Color

Builder.load_string("""
<MenuScreen>:
    GridLayout:
        cols: 1
        spacing: 80, 20
        
        Label: 
            text: 'Select Login Type'
            font_size: 50
            color: "#000000"
            bold: True

        Button:
            text: 'Employee'
            size_hint: (0.5, 0.5)
            bold: True
            font_size: 30
            background_color: 0, 0, 100, 0.5
            on_press: root.manager.current = 'Employee Login'
        
        Button:
            text: 'Patient'
            size_hint: (0.5, 0.5)
            bold: True
            font_size: 30
            background_color: 0, 0, 8, 0.5
            on_press: root.manager.current = 'Patient Login'

<EmployeeLoginScreen>:
    GridLayout:
        cols: 1
        spacing: 20, 20

        Label: 
            text: 'Employee Login'
            font_size: 50
            color: "#000000"
            bold: True
        
        Label: 
            text: 'Username'
            font_size: 50
            color: "#000000"
        
        TextInput:
            id: username
            multiline: False
            size_hint: (1, 0.7)
            font_size: 30
            on_text: root.storeUsername(self.text)

        Label: 
            text: 'Password'
            font_size: 50
            color: "#000000"
            
        TextInput:
            id: password
            multiline: False
            size_hint: (1, 0.7)
            font_size: 30
            password: True
            on_text: root.storePassword(self.text)

        Button:
            text: 'Sign In'
            font_size: 30
            background_color: 0, 0, 8, 0.5
            on_press: 
                root.manager.current = root.verify()
                app.root.get_screen('Employee Page').welcome.text = root.employee.getName()
        
        Button:
            text: 'Back'
            font_size: 30
            background_color: 0, 0, 8, 0.5
            on_press: root.manager.current = 'menu'

<EmployeePage>:
    welcome: welcome 
    GridLayout:
        cols: 1
        spacing: 20, 20

        Label: 
            id: welcome
            font_size: 50
            color: "#000000"
        
        Button:
            text: 'Add Patient'
            font_size: 30
            background_color: 0, 0, 8, 0.5
            on_press: root.manager.current = 'Edit Patient'

        Button:
            text: 'Edit Existing Patient'   
            font_size: 30
            background_color: 0, 0, 8, 0.5
            on_press: root.manager.current = 'menu'
    
        Button:
            text: 'Appointments'
            font_size: 30
            background_color: 0, 0, 8, 0.5
            on_press: 
                root.manager.current = 'Appointment'
                app.root.get_screen('Appointment').SIN = app.root.get_screen('Employee Login').username

        Button:
            text: 'Edit Employee'
            font_size: 30
            background_color: 0, 0, 8, 0.5
            on_press: root.manager.current = root.verifySuper()

        Button:
            text: 'Logout'
            font_size: 30
            background_color: 0, 0, 8, 0.5
            on_press: root.manager.current = 'menu'

<PatientLoginScreen>:
    GridLayout:
        cols: 1
        
        Label: 
            text: 'Patient Login'
            font_size: 50
            color: "#000000"
            bold: True
        
        Label: 
            text: 'Username'
            font_size: 50
            color: "#000000"
        
        TextInput:
            id: username
            multiline: False
            size_hint: (1, 0.7)
            font_size: 30
            on_text: root.storeUsername(self.text)

        Label: 
            text: 'Password'
            font_size: 50
            color: "#000000"
        
        TextInput:
            id: password
            multiline: False
            size_hint: (1, 0.7)
            font_size: 30
            password: True
            on_text: root.storePassword(self.text)

        Button:
            text: 'Sign In'
            font_size: 30
            background_color: 0, 0, 8, 0.5
            on_press: root.manager.current = root.verify() 

        Button:
            text: 'Back'
            font_size: 30
            background_color: 0, 0, 8, 0.5
            on_press: root.manager.current = 'menu'

<PatientHomePage>:
    GridLayout:
        cols: 1
        spacing: 20,20    
        
        Label: 
            id: welcome
            font_size: 50
            color: "#000000"
        
        Button:
            text: 'Edit Personal Information'
            font_size: 30
            background_color: 0, 0, 8, 0.5
            on_press: root.manager.current = 'Edit Personal Information'

        Button:
            text: 'View Exam Detail'   
            font_size: 30
            background_color: 0, 0, 8, 0.5
            on_press: root.manager.current = 'View Exam Detail'

        Button:
            text: 'Appointments'
            font_size: 30
            background_color: 0, 0, 8, 0.5
            on_press: root.manager.current = 'PAppointment'

        Button:
            text: 'Logout'
            font_size: 30
            background_color: 0, 0, 8, 0.5
            on_press: root.manager.current = 'menu'

<PAppointmentScreen>:
    GridLayout:
        cols: 1
        spacing: 20, 20

        Button:
            text: 'View Appointment'
            font_size: 30
            background_color: 0, 0, 8, 0.5
            on_press: 
                app.root.get_screen('View Appointment').message.text = root.getPAppointments()
                root.manager.current = 'View Appointment'

        Button:
            text: 'Delete Appointment'   
            font_size: 30
            background_color: 0, 0, 8, 0.5
            on_press: root.manager.current = 'Delete Appointment'

        Button:
            text: 'Back'
            font_size: 30
            background_color: 0, 0, 8, 0.5
            on_press: root.manager.current = 'Patient Home Page'
                                 
<DeleteAppointment>:
    GridLayout:
        cols: 1

        Label: 
            text: 'Enter Patient AHC'
            font_size: 50
            color: "#000000"
        
        TextInput:
            id: AHC
            multiline: False
            size_hint: (1, 0.7)
            font_size: 30
            on_text: root.storeAHC(self.text)

        Label: 
            text: 'Enter Time of Appointment'
            font_size: 50
            color: "#000000"
        
        TextInput:
            id: time
            multiline: False
            size_hint: (1, 0.7)
            font_size: 30
            on_text: root.storeTime(self.text)
        
        Label: 
            text: 'Enter Date of Appointment'
            font_size: 50
            color: "#000000"
        
        TextInput:
            id: date
            multiline: False
            size_hint: (1, 0.7)
            font_size: 30
            on_text: root.storeDate(self.text)

        Button:
            text: 'Delete Appointment'
            font_size: 30
            background_color: 0, 0, 8, 0.5
            on_press: 
                root.deleteAppointment()
                root.manager.current = 'PAppointment'

        Button:
            text: 'Cancel'
            font_size: 30
            background_color: 0, 0, 8, 0.5
            on_press: root.manager.current = 'PAppointment'

<ViewAppointment>:
    message: message
    GridLayout:
        cols: 1

        Label: 
            id: message 
            font_size: 20
            color: "#000000"
            text_size: self.size
            halign: 'left'
            valign: 'middle'

        Button:
            text: 'Back'
            font_size: 20
            background_color: 0, 0, 8, 0.5
            on_press: root.manager.current = 'PAppointment'

<ViewExamDetail>:
    message: message
    GridLayout:
        spacing: 20, 20
        cols: 2

        Label: 
            id: message 
            font_size: 20
            color: "#000000"
            text_size: self.size
            halign: 'left'
            valign: 'middle'

        Button:
            text: 'Exit'
            font_size: 20
            background_color: 0, 0, 8, 0.5
            on_press: root.manager.current = 'Patient Home Page'


<EditPersonalInformation>:
    title: 'Edit Personal Information'
    GridLayout:
        spacing: 20, 20
        cols: 2

        Label: 
            text_size: self.size
            halign: 'right'
            valign: 'middle'
            text: 'Edit Name:    '
            font_size: 20
            color: "#000000"

        TextInput:
            id: name
            multiline: False
            size_hint: (1, 0.7)
            font_size: 20

        Label: 
            text_size: self.size
            halign: 'right'
            valign: 'middle'        
            text: 'Edit Date of Birth:   '
            font_size: 20
            color: "#000000"

        TextInput:
            id: DOB
            multiline: False
            size_hint: (1, 0.7)
            font_size: 20

        Label:
            text_size: self.size
            halign: 'right'
            valign: 'middle' 
            text: 'Edit Address: '
            font_size: 20
            color: "#000000"

        TextInput:
            id: address
            multiline: False
            size_hint: (1, 0.7)
            font_size: 20

        Label: 
            text_size: self.size
            halign: 'right'
            valign: 'middle'
            text: 'Edit Postal Code: '
            font_size: 20
            color: "#000000"

        TextInput:
            id: pCode
            multiline: False
            size_hint: (1, 0.7)
            font_size: 20
                
        Label: 
            text_size: self.size
            halign: 'right'
            valign: 'middle'
            text: 'Edit City:    '
            font_size: 20
            color: "#000000"

        TextInput:
            id: city
            multiline: False
            size_hint: (1, 0.7)
            font_size: 20

        Label: 
            text_size: self.size
            halign: 'right'
            valign: 'middle'
            text: 'Edit Country: '
            font_size: 20
            color: "#000000"

        TextInput:
            id: country
            multiline: False
            size_hint: (1, 0.7)
            font_size: 20

        Button:
            text: 'Edit Information'
            font_size: 20
            background_color: 0, 0, 8, 0.5
            on_press: root.manager.current = root.editPatient()

        Button:
            text: 'Exit'
            font_size: 20
            background_color: 0, 0, 8, 0.5
            on_press: root.manager.current = 'Patient Home Page'

<Error>:
    GridLayout:
        cols: 1     
        
        Label: 
            text: 'Error'
            font_size: 50
            color: "#000000"
        
        Button:
            text: 'Back'
            font_size: 30
            background_color: 0, 0, 8, 0.5
            on_press: root.manager.current = 'menu'
""")

class MenuScreen(Screen):
    pass

class EmployeeLoginScreen(Screen):
    def storeUsername(self, u):
        self.username = u
    
    def storePassword(self, p):
        self.password = p

    def verify(self):
        self.login = Login()
        if (self.login.verifyEmployee(self.username, self.password) == True):
            self.employee = EmployeePage()
            return 'Employee Page'
        return 'Error'


class EmployeePage(Screen):
    def getName(self): 
        self.SIN = app.root.get_screen('Employee Login').username
        self.employee = Employee(self.SIN)
        return 'Welcome ' + str(self.employee.getName()) + '!'

    def verifySuper(self):
        self.SIN = app.root.get_screen('Employee Login').username
        self.Semp = Employee(self.SIN).verifySuper()
        if (self.Semp == True):
            return 'Edit Employee'
        return 'Error'

class PatientLoginScreen(Screen):
    def storeUsername(self, u):
        self.username = u
    
    def storePassword(self, p):
        self.password = p

    def verify(self):
        self.login = Login()
        if (self.login.verifyPatient(self.username, self.password) == True):
            self.patient = PatientHomePage()
            return 'Patient Home Page'
        else:
            return 'Error'

class PAppointmentScreen(Screen):
    def getPAppointments(self):
        self.allAppointment = Appointment().viewPAppointments(self.AHC)
        return self.allAppointment

class PatientHomePage(Screen):
    pass

class EditPersonalInformation(Screen):
    def editPersonalInformation(self):
        pass
        self.name = app.root.get_screen('Edit Personal Information').name
        self.DOB = app.root.get_screen('Edit Personal Informatio').DOB
        self.address = app.root.get_screen('Edit Personal Information').address
        self.pcode = app.root.get_screen('Edit Personal Information').pCode
        self.city = app.root.get_screen('Edit Personal Information').city
        self.country = app.root.get_screen('Edit Personal Information').country

class ViewExamDetail(Screen):
    def viewExamDetail(self):
            pass

class DeleteAppointment(Screen):
    def storeAHC(self, AHC):
        self.AHC = AHC 

    def storeDate(self, date):
        self.date = date 

    def storeTime(self, time):
        self.time = time 

    def deleteAppointment(self):
        self.newAppointment = Appointment().deleteAppointment(self.AHC, self.date, self.time) 

class ViewAppointments(Screen):
    pass

class Error(Screen):
    pass

class MobileApp(App):
    def build(self):
        self.sm = ScreenManager()
        self.sm.add_widget(MenuScreen(name='menu'))
        self.sm.add_widget(EmployeeLoginScreen(name='Employee Login'))
        self.sm.add_widget(EmployeePage(name='Employee Page'))
        self.sm.add_widget(EditPatient(name='Edit Patient'))
        self.sm.add_widget(PatientLoginScreen(name='Patient Login'))
        self.sm.add_widget(Error(name='Error'))
        self.sm.add_widget(PatientHomePage(name='Patient Home Page'))
        self.sm.add_widget(AppointmentScreen(name='Appointment'))
        self.sm.add_widget(PAppointmentScreen(name='PAppointment'))
        self.sm.add_widget(CreateAppointment(name='Create Appointment'))
        self.sm.add_widget(DeleteAppointment(name='Delete Appointment'))
        self.sm.add_widget(ViewAppointment(name='View Appointment'))
        self.sm.add_widget(EditEmployee(name='Edit Employee'))
        self.sm.add_widget(AddEmployee(name='Add Employee'))
        self.sm.add_widget(DeleteEmployee(name='Delete Employee'))
        self.sm.add_widget(EditPersonalInformation(name='Edit Personal Information'))
        self.sm.add_widget(ViewExamDetail(name='View Exam Detail'))

        return self.sm
        
if __name__ == "__main__":
    app = MobileApp()
    app.run()