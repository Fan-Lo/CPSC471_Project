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
        
        Label: 
            id: welcome
            font_size: 50
            color: "#000000"
        
        Button:
            text: 'Edit Personal Information'
            font_size: 30
            background_color: 0, 0, 8, 0.5
            on_press: root.manager.current = 'Add Patient'

        Button:
            text: 'View Exam Detail'   
            font_size: 30
            background_color: 0, 0, 8, 0.5
            on_press: root.manager.current = 'Choose Patient'

        Button:
            text: 'Appointments'
            font_size: 30
            background_color: 0, 0, 8, 0.5
            on_press: root.manager.current = 'menu'

        Button:
            text: 'Edit Family Information'
            font_size: 30
            background_color: 0, 0, 8, 0.5
            on_press: root.manager.current = 'menu'

        Button:
            text: 'Edit Employee'
            font_size: 30
            background_color: 0, 0, 8, 0.5
            on_press: root.manager.current = 'menu'

        Button:
            text: 'Logout'
            font_size: 30
            background_color: 0, 0, 8, 0.5
            on_press: root.manager.current = 'menu'

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

class PatientHomePage(Screen):
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
        self.sm.add_widget(CreateAppointment(name='Create Appointment'))
        self.sm.add_widget(DeleteAppointment(name='Delete Appointment'))
        self.sm.add_widget(ViewAppointment(name='View Appointment'))
        self.sm.add_widget(EditEmployee(name='Edit Employee'))
        self.sm.add_widget(AddEmployee(name='Add Employee'))
        self.sm.add_widget(DeleteEmployee(name='Delete Employee'))

        return self.sm
        
if __name__ == "__main__":
    app = MobileApp()
    app.run()