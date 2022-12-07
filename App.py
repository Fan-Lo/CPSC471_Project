from Login import *
from Employee import * 
from DatabaseConnect import *
from AppointmentScreens import *
from EditEmployeeScreens import *
from Patient import *
# from EmployeePatientScreens import *

from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.checkbox import CheckBox
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
            on_press: root.manager.current = root.verify()
        
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
            on_press: root.manager.current = 'Add Patient'

        Button:
            text: 'Edit Existing Patient'   
            font_size: 30
            background_color: 0, 0, 8, 0.5
            on_press: root.manager.current = 'Choose Patient'
    
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
    welcome:welcome
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
            on_press: 
                root.formatEditPatient()
                root.manager.current = 'Edit Patient Info'
        Button:
            text: 'View Exam Detail'   
            font_size: 30
            background_color: 0, 0, 8, 0.5
            on_press: 
                app.root.get_screen('View Exam Detail').message.text = root.getExamDetail()
                root.manager.current = 'View Exam Detail'
        Button:
            text: 'Appointments'
            font_size: 30
            background_color: 0, 0, 8, 0.5
            on_press: 
                root.manager.current = 'PAppointment'
                app.root.get_screen('PAppointment').AHC = app.root.get_screen('Patient Login').username
        Button:
            text: 'Logout'
            font_size: 30
            background_color: 0, 0, 8, 0.5
            on_press: root.manager.current = 'menu'


<ChoosePatient>:
    GridLayout: 
        spacing: 20, 20 
        cols: 1

        Label:
            text: 'Enter Patient Alberta Health Care Number'
            font_size: 40
            color: "#000000"

        TextInput:
            id: AHC
            multiline: False
            size_hint: (1, 0.7)
            font_size: 20
            on_text: root.storeAHC(self.text)

        Button:
            text: 'Search'
            font_size: 20
            background_color: 0, 0, 8, 0.5
            on_press: root.manager.current = root.search()

        Button:
            text: 'Back'
            font_size: 20
            background_color: 0, 0, 8, 0.5
            on_press: root.manager.current = 'Employee Page'

<PatientScreen>:
    GridLayout:
        spacing: 20, 20 
        cols: 1

        Button:
            text: 'Edit Patient'
            font_size: 20
            background_color: 0, 0, 8, 0.5
            on_press: 
                root.formatEditPatient()
                root.manager.current = 'Edit Patient'

        Button:
            text: 'Add Invoice'
            font_size: 20
            background_color: 0, 0, 8, 0.5
            on_press: root.manager.current = 'Add Invoice'
 
        Button:
            text: 'Add Insurance'
            font_size: 20
            background_color: 0, 0, 8, 0.5
            on_press: root.manager.current = 'Add Insurance'

        Button:
            text: 'View Patient Details'
            font_size: 20
            background_color: 0, 0, 8, 0.5
            on_press: 
                root.formatDetails()
                root.manager.current = 'View Patient Details'

        Button:
            text: 'Back'
            font_size: 20
            background_color: 0, 0, 8, 0.5
            on_press: root.manager.current = 'Employee Page'
        
<EditPatient>:
    n: n 
    sex: sex
    ahc: ahc
    dob: dob
    phone: phone
    address: address
    pCode: pCode
    city: city
    country: country

    GridLayout:
        spacing: 20, 20
        cols: 2

        Label: 
            text_size: self.size
            halign: 'right'
            valign: 'middle'
            text: 'Name:    '
            font_size: 20
            color: "#000000"

        TextInput:
            id: n
            multiline: False
            size_hint: (1, 0.7)
            font_size: 20
            on_text: root.storeName(self.text)
        
        Label: 
            text_size: self.size
            halign: 'right'
            valign: 'middle'
            text: 'Sex: '
            font_size: 20
            color: "#000000"

        TextInput:
            id: sex
            multiline: False
            size_hint: (1, 0.7)
            font_size: 20
            text: 'Ex. F'
            on_text: root.storeSex(self.text)

        Label:
            text_size: self.size
            halign: 'right'
            valign: 'middle' 
            text: 'Alberta Health Card Number:  '
            font_size: 20
            color: "#000000"

        TextInput:
            id: ahc
            multiline: False
            size_hint: (1, 0.7)
            font_size: 20
            on_text: root.storeAHC(self.text)
        
        Label: 
            text_size: self.size
            halign: 'right'
            valign: 'middle'        
            text: 'Date of Birth:   '
            font_size: 20
            color: "#000000"

        TextInput:
            id: dob
            multiline: False
            size_hint: (1, 0.7)
            font_size: 20
            text: 'YYYY-MM-DD'
            on_text: root.storeDOB(self.text)

        Label: 
            text_size: self.size
            halign: 'right'
            valign: 'middle'        
            text: 'Phone Number:   '
            font_size: 20
            color: "#000000"

        TextInput:
            id: phone
            multiline: False
            size_hint: (1, 0.7)
            font_size: 20
            text: 'XXX-XXX-XXXX'
            on_text: root.storePhone(self.text)

        Button:
            text: 'Add Phone'
            font_size: 20
            background_color: 0, 0, 8, 0.5
            on_press: root.addPhone()

        Button:
            text: 'Remove Phone'
            font_size: 20
            background_color: 0, 0, 8, 0.5
            on_press:root.removePhone()

        Label:
            text_size: self.size
            halign: 'right'
            valign: 'middle' 
            text: 'Address: '
            font_size: 20
            color: "#000000"

        TextInput:
            id: address
            multiline: False
            size_hint: (1, 0.7)
            font_size: 20
            on_text: root.storeAddress(self.text)

        Label: 
            text_size: self.size
            halign: 'right'
            valign: 'middle'
            text: 'Postal Code: '
            font_size: 20
            color: "#000000"

        TextInput:
            id: pCode
            multiline: False
            size_hint: (1, 0.7)
            font_size: 20
            on_text: root.storePostalCode(self.text)
                
        Label: 
            text_size: self.size
            halign: 'right'
            valign: 'middle'
            text: 'City:    '
            font_size: 20
            color: "#000000"

        TextInput:
            id: city
            multiline: False
            size_hint: (1, 0.7)
            font_size: 20
            on_text: root.storeCity(self.text)

        Label: 
            text_size: self.size
            halign: 'right'
            valign: 'middle'
            text: 'Country: '
            font_size: 20
            color: "#000000"

        TextInput:
            id: country
            multiline: False
            size_hint: (1, 0.7)
            font_size: 20
            on_text: root.storeCountry(self.text)

        Button:
            text: 'Cancel'
            font_size: 20
            background_color: 0, 0, 8, 0.5
            on_press: root.manager.current = 'Patient Screen'

        Button:
            text: 'Make Changes'
            font_size: 20
            background_color: 0, 0, 8, 0.5
            on_press: 
                root.makeChanges()
                root.manager.current = 'Patient Screen'

<AddPatient>:
    n: n 
    sex: sex
    ahc: ahc
    dob: dob
    phone: phone
    address: address
    pCode: pCode
    city: city
    country: country

    GridLayout:
        spacing: 20, 20
        cols: 2

        Label: 
            text_size: self.size
            halign: 'right'
            valign: 'middle'
            text: 'Name:    '
            font_size: 20
            color: "#000000"

        TextInput:
            id: n
            multiline: False
            size_hint: (1, 0.7)
            font_size: 20
            on_text: root.storeName(self.text)
        
        Label: 
            text_size: self.size
            halign: 'right'
            valign: 'middle'
            text: 'Sex: '
            font_size: 20
            color: "#000000"

        TextInput:
            id: sex
            multiline: False
            size_hint: (1, 0.7)
            font_size: 20
            text: 'Ex. F'
            on_text: root.storeSex(self.text)

        Label:
            text_size: self.size
            halign: 'right'
            valign: 'middle' 
            text: 'Alberta Health Card Number:  '
            font_size: 20
            color: "#000000"

        TextInput:
            id: ahc
            multiline: False
            size_hint: (1, 0.7)
            font_size: 20
            on_text: root.storeAHC(self.text)
        
        Label: 
            text_size: self.size
            halign: 'right'
            valign: 'middle'        
            text: 'Date of Birth:   '
            font_size: 20
            color: "#000000"

        TextInput:
            id: dob
            multiline: False
            size_hint: (1, 0.7)
            font_size: 20
            text: 'YYYY-MM-DD'
            on_text: root.storeDOB(self.text)

        Label: 
            text_size: self.size
            halign: 'right'
            valign: 'middle'        
            text: 'Phone Number:   '
            font_size: 20
            color: "#000000"

        TextInput:
            id: phone
            multiline: False
            size_hint: (1, 0.7)
            font_size: 20
            text: 'XXX-XXX-XXXX'
            on_text: root.storePhone(self.text)

        Button:
            text: 'Add Phone'
            font_size: 20
            background_color: 0, 0, 8, 0.5
            on_press: root.addPhone()

        Button:
            text: 'Remove Phone'
            font_size: 20
            background_color: 0, 0, 8, 0.5
            on_press:root.removePhone()

        Label:
            text_size: self.size
            halign: 'right'
            valign: 'middle' 
            text: 'Address: '
            font_size: 20
            color: "#000000"

        TextInput:
            id: address
            multiline: False
            size_hint: (1, 0.7)
            font_size: 20
            on_text: root.storeAddress(self.text)

        Label: 
            text_size: self.size
            halign: 'right'
            valign: 'middle'
            text: 'Postal Code: '
            font_size: 20
            color: "#000000"

        TextInput:
            id: pCode
            multiline: False
            size_hint: (1, 0.7)
            font_size: 20
            on_text: root.storePostalCode(self.text)
                
        Label: 
            text_size: self.size
            halign: 'right'
            valign: 'middle'
            text: 'City:    '
            font_size: 20
            color: "#000000"

        TextInput:
            id: city
            multiline: False
            size_hint: (1, 0.7)
            font_size: 20
            on_text: root.storeCity(self.text)

        Label: 
            text_size: self.size
            halign: 'right'
            valign: 'middle'
            text: 'Country: '
            font_size: 20
            color: "#000000"

        TextInput:
            id: country
            multiline: False
            size_hint: (1, 0.7)
            font_size: 20
            on_text: root.storeCountry(self.text)

        Button:
            text: 'Cancel'
            font_size: 20
            background_color: 0, 0, 8, 0.5
            on_press: root.manager.current = 'Employee Page'

        Button:
            text: 'Make Changes'
            font_size: 20
            background_color: 0, 0, 8, 0.5
            on_press: 
                root.makeChanges()
                root.manager.current = 'Employee Page'


<AddInvoice>:
    GridLayout:
        spacing: 20, 20
        cols: 1

        Label:
            text: 'Date:    ' + root.getDate()
            font_size: 30
            color: "#000000"

        Label:
            text: 'Invoice ID:    ' + root.createID()
            font_size: 30
            color: "#000000"

        Label:
            text: 'Select Products: '
            font_size: 30
            color: "#000000"

        Label:
            text: "Tylenol"
            font_size: 30
            color: "#000000"
        
        CheckBox:
            color:.294, .761, .623
            on_active: root.checkbox_click(self, self.active, "Tylenol")
            size_hint_x: .20
        
        Label:
            text: "Advil"
            font_size: 30
            color: "#000000"
        
        CheckBox:
            color:.294, .761, .623
            on_active: root.checkbox_click(self, self.active, "Advil")
            size_hint_x: .20

        Label:
            text: "IBProfen"
            font_size: 30
            color: "#000000"
        
        CheckBox:
            color:.294, .761, .623
            on_active: root.checkbox_click(self, self.active, "IBProfen")
            size_hint_x: .20

        Label:
            text: "Aspirin"
            font_size: 30
            color: "#000000"
        
        CheckBox:
            color:.294, .761, .623
            on_active: root.checkbox_click(self, self.active, "Aspirin")
            size_hint_x: .20

        Label:
            text: "Morphine"
            font_size: 30
            color: "#000000"
        
        CheckBox:
            id: morphine
            color:.294, .761, .623
            on_active: root.checkbox_click(self, self.active, "Morphine")
            size_hint_x: .20

        Button:
            text: 'Add Invoice'
            font_size: 20
            background_color: 0, 0, 8, 0.5
            on_press: 
                root.addInvoice()
                root.manager.current = 'Patient Screen'

        Button:
            text: 'Cancel'
            font_size: 20
            background_color: 0, 0, 8, 0.5
            on_press: root.manager.current = 'Patient Screen'

<AddInsurance>:
    GridLayout:
        spacing: 20, 20
        cols: 1
    
        Label: 
            text: 'Insurance Member ID: '
            font_size: 30
            color: "#000000"

        TextInput:
            id: memberID
            multiline: False
            size_hint: (1, 0.7)
            font_size: 20
            on_text: root.storeMemberID(self.text)

        Label:
            text: 'Insurance Policy No.:    '
            font_size: 30
            color: "#000000"

        TextInput:
            id: policyNo
            multiline: False
            size_hint: (1, 0.7)
            font_size: 20
            on_text: root.storePolicyNo(self.text)

        Button:
            text: 'Add Insurance'
            font_size: 20
            background_color: 0, 0, 8, 0.5
            on_press: 
                root.addInsurance()
                root.manager.current = 'Patient Screen'

        Button:
            text: 'Cancel'
            font_size: 20
            background_color: 0, 0, 8, 0.5
            on_press: root.manager.current = 'Patient Screen'   

<ViewPatientDetails>:
    patientDetails: patientDetails 
    GridLayout: 
        cols: 1
        Label: 
            id: patientDetails 
            font_size: 20
            color: "#000000"

        Button:
            text: 'Back'
            size_hint_y: None
            height: 100
            font_size: 20
            background_color: 0, 0, 8, 0.5
            on_press: root.manager.current = 'Patient Screen' 

<EditPatientInfo>:
    n: n 
    sex: sex
    ahc: ahc
    dob: dob
    phone: phone
    address: address
    pCode: pCode
    city: city
    country: country
    GridLayout:
        spacing: 20, 20
        cols: 2
        Label: 
            text_size: self.size
            halign: 'right'
            valign: 'middle'
            text: 'Name:    '
            font_size: 20
            color: "#000000"
        TextInput:
            id: n
            multiline: False
            size_hint: (1, 0.7)
            font_size: 20
            on_text: root.storeName(self.text)
        
        Label: 
            text_size: self.size
            halign: 'right'
            valign: 'middle'
            text: 'Sex: '
            font_size: 20
            color: "#000000"
        TextInput:
            id: sex
            multiline: False
            size_hint: (1, 0.7)
            font_size: 20
            text: 'Ex. F'
            on_text: root.storeSex(self.text)
        Label:
            text_size: self.size
            halign: 'right'
            valign: 'middle' 
            text: 'Alberta Health Card Number:  '
            font_size: 20
            color: "#000000"
        TextInput:
            id: ahc
            multiline: False
            size_hint: (1, 0.7)
            font_size: 20
            on_text: root.storeAHC(self.text)
        
        Label: 
            text_size: self.size
            halign: 'right'
            valign: 'middle'        
            text: 'Date of Birth:   '
            font_size: 20
            color: "#000000"
        TextInput:
            id: dob
            multiline: False
            size_hint: (1, 0.7)
            font_size: 20
            text: 'YYYY-MM-DD'
            on_text: root.storeDOB(self.text)
        Label: 
            text_size: self.size
            halign: 'right'
            valign: 'middle'        
            text: 'Phone Number:   '
            font_size: 20
            color: "#000000"
        TextInput:
            id: phone
            multiline: False
            size_hint: (1, 0.7)
            font_size: 20
            text: 'XXX-XXX-XXXX'
            on_text: root.storePhone(self.text)
        Button:
            text: 'Add Phone'
            font_size: 20
            background_color: 0, 0, 8, 0.5
            on_press: root.addPhone()
        Button:
            text: 'Remove Phone'
            font_size: 20
            background_color: 0, 0, 8, 0.5
            on_press:root.removePhone()
        Label:
            text_size: self.size
            halign: 'right'
            valign: 'middle' 
            text: 'Address: '
            font_size: 20
            color: "#000000"
        TextInput:
            id: address
            multiline: False
            size_hint: (1, 0.7)
            font_size: 20
            on_text: root.storeAddress(self.text)
        Label: 
            text_size: self.size
            halign: 'right'
            valign: 'middle'
            text: 'Postal Code: '
            font_size: 20
            color: "#000000"
        TextInput:
            id: pCode
            multiline: False
            size_hint: (1, 0.7)
            font_size: 20
            on_text: root.storePostalCode(self.text)
                
        Label: 
            text_size: self.size
            halign: 'right'
            valign: 'middle'
            text: 'City:    '
            font_size: 20
            color: "#000000"
        TextInput:
            id: city
            multiline: False
            size_hint: (1, 0.7)
            font_size: 20
            on_text: root.storeCity(self.text)
        Label: 
            text_size: self.size
            halign: 'right'
            valign: 'middle'
            text: 'Country: '
            font_size: 20
            color: "#000000"
        TextInput:
            id: country
            multiline: False
            size_hint: (1, 0.7)
            font_size: 20
            on_text: root.storeCountry(self.text)
        Button:
            text: 'Cancel'
            font_size: 20
            background_color: 0, 0, 8, 0.5
            on_press: root.manager.current = 'Patient Home Page'
        Button:
            text: 'Make Changes'
            font_size: 20
            background_color: 0, 0, 8, 0.5
            on_press: 
                root.makeChanges()
                root.manager.current = 'Patient Home Page'

<ViewExamDetail>:
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
            app.root.get_screen('Employee Page').welcome.text = self.employee.getName()
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
            app.root.get_screen('Patient Home Page').welcome.text = self.patient.getName()
            return 'Patient Home Page'
        return 'Error'

class PatientHomePage(Screen):
    def getName(self):
        self.AHC = app.root.get_screen('Patient Login').username
        self.name = Patient(self.AHC).getName().getFullName()
        return 'Welcome ' + str(self.name) + '!'

    def formatEditPatient(self):
        self.AHC = app.root.get_screen('Patient Login').username
        self.patient = Patient(self.AHC)
        app.root.get_screen('Edit Patient Info').n.text = str(self.patient.getName().getFullName())
        app.root.get_screen('Edit Patient Info').ahc.text = str(self.patient.getAHC())
        app.root.get_screen('Edit Patient Info').sex.text = str(self.patient.getSex())
        app.root.get_screen('Edit Patient Info').dob.text = str(self.patient.getDOB())
        app.root.get_screen('Edit Patient Info').address.text = str(self.patient.getAddress().getAddress())
        app.root.get_screen('Edit Patient Info').pCode.text = str(self.patient.getAddress().getPostalCode())
        app.root.get_screen('Edit Patient Info').city.text = str(self.patient.getAddress().getCity())
        app.root.get_screen('Edit Patient Info').country.text = str(self.patient.getAddress().getCountry())
        phonelist = self.patient.getPatientPhone()
        disp = ""
        i = 0
        while i < len(phonelist):
            disp += phonelist[i].display()
            disp += " "
            i += 1
            
        app.root.get_screen('Edit Patient Info').phone.text = disp

    def formatDetails(self):
        self.AHC = app.root.get_screen('Patient Login').username
        self.patient = Patient(self.AHC)
        self.name = self.patient.getName().getFullName()
        self.sex = self.patient.getSex()
        self.DOB = self.patient.getDOB()
        self.address = self.patient.getAddress().getAddress()
        self.pCode = self.patient.getAddress().getPostalCode()
        self.city = self.patient.getAddress().getCity()
        self.country = self.patient.getAddress().getCountry()
        self.invoices = self.patient.getAllInvoices()
        self.insurance = self.patient.getAllInsurances()
        self.examDetail = self.patient.getAllExamDetails()

    def getExamDetail(self):
        self.AHC = app.root.get_screen('Patient Login').username
        self.allDetail = ExamDetail().viewExamDetail(self.AHC)
        return self.allDetail

class EditPatient(Screen):
    def storeName(self, n = None):
        self.n = n
    
    def storeAHC(self, a = None):
        self.AHC = a

    def storeDOB(self, d = None):
        self.DOB = d

    def storePhone(self, p = None):
        self.phone = p
    
    def storeSex(self, s = None):
        self.sex = s

    def storeAddress(self, a = None):
        self.address = a

    def storePostalCode(self, p = None):
        self.pCode = p

    def storeCity(self, c = None):
        self.city = c

    def storeCountry(self, c = None):
        self.country = c
    
    def addPhone(self):
        self.exists = Patient().searchPatient(self.AHC)
        if (self.exists == False):
            return
        if(self.phone != None):
            self.addPhone = Patient(self.AHC).addPatientPhone(self.phone)

    def removePhone(self):
        self.exists = Patient().searchPatient(self.AHC)
        if (self.exists == False):
            return
        if (self.phone != None):
            self.removePhone = Patient(self.AHC).removePhoneNumber(self.phone)

    def makeChanges(self):
        #if patient doesn't exist then create new patient
        self.exists = Patient().searchPatient(self.AHC)
        
        if(self.exists == False and self.AHC != None and self.sex != None and self.DOB != None and self.n != None and self.address != None and self.city != None and self.country != None and self.pCode):
            self.patient = Patient().addPatient(self.AHC, self.sex, self.DOB, self.n, self.address, self.city, self.country, self.pCode)
            if(self.phone != None):
                self.patient = Patient(self.AHC)
                self.patient.addPatientPhone(self.phone)
            return

        #first check if patient SIN already exists in database
        #if it does exist then make changes to that patient and make changes only to things the user has changed
        # AHC can nver change once it has been set (No reason why it should ever change)

        if (self.AHC != None and self.exists == True):
            self.patient = Patient(self.AHC)
            self.patient.setName(self.n)
            self.patient.setSex(self.sex)  
            self.patient.setAddress(self.address, self.city, self.country, self.pCode)

class EditPatientInfo(Screen):
    def storeName(self, n = None):
        self.n = n
    
    def storeAHC(self, a = None):
        self.AHC = a

    def storeDOB(self, d = None):
        self.DOB = d

    def storePhone(self, p = None):
        self.phone = p
    
    def storeSex(self, s = None):
        self.sex = s

    def storeAddress(self, a = None):
        self.address = a

    def storePostalCode(self, p = None):
        self.pCode = p

    def storeCity(self, c = None):
        self.city = c

    def storeCountry(self, c = None):
        self.country = c
    
    def addPhone(self):
        self.exists = Patient().searchPatient(self.AHC)
        if (self.exists == False):
            return
        if(self.phone != None):
            self.addPhone = Patient(self.AHC).addPatientPhone(self.phone)

    def removePhone(self):
        self.exists = Patient().searchPatient(self.AHC)
        if (self.exists == False):
            return
        if (self.phone != None):
            self.removePhone = Patient(self.AHC).removePhoneNumber(self.phone)

    def makeChanges(self):
        #if patient doesn't exist then create new patient
        self.exists = Patient().searchPatient(self.AHC)
        
        if(self.exists == False):
            self.patient = Patient().addPatient(self.AHC, self.sex, self.DOB, self.n, self.address, self.city, self.country, self.pCode)
            if(self.phone != None):
                self.patient.addPatientPhone(self.phone)
            return

        #first check if patient SIN already exists in database
        #if it does exist then make changes to that patient and make changes only to things the user has changed
        # AHC can nver change once it has been set (No reason why it should ever change)

        self.patient = Patient(self.AHC)
        self.patient.setName(self.n)
        self.patient.setSex(self.sex)  
        self.patient.setAddress(self.address, self.city, self.country, self.pCode)

class AddPatient(Screen):
    def storeName(self, n = None):
        self.n = n
    
    def storeAHC(self, a = None):
        self.AHC = a

    def storeDOB(self, d = None):
        self.DOB = d

    def storePhone(self, p = None):
        self.phone = p
    
    def storeSex(self, s = None):
        self.sex = s

    def storeAddress(self, a = None):
        self.address = a

    def storePostalCode(self, p = None):
        self.pCode = p

    def storeCity(self, c = None):
        self.city = c

    def storeCountry(self, c = None):
        self.country = c
    
    def addPhone(self):
        self.exists = Patient().searchPatient(self.AHC)
        if (self.exists == False):
            return
        if(self.phone != None):
            self.addPhone = Patient(self.AHC).addPatientPhone(self.phone)

    def removePhone(self):
        self.exists = Patient().searchPatient(self.AHC)
        if (self.exists == False):
            return
        if (self.phone != None):
            self.removePhone = Patient(self.AHC).removePhoneNumber(self.phone)

    def makeChanges(self):
        #if patient doesn't exist then create new patient
        self.exists = Patient().searchPatient(self.AHC)
        
        if(self.exists == False):
            self.patient = Patient().addPatient(self.AHC, self.sex, self.DOB, self.n, self.address, self.city, self.country, self.pCode)
            if(self.phone != None):
                self.patient = Patient(self.AHC)
                self.patient.addPatientPhone(self.phone)
            return

        #first check if patient SIN already exists in database
        #if it does exist then make changes to that patient and make changes only to things the user has changed
        # AHC can nver change once it has been set (No reason why it should ever change)

        self.patient = Patient(self.AHC)
        self.patient.setName(self.n)
        self.patient.setSex(self.sex)  
        self.patient.setAddress(self.address, self.city, self.country, self.pCode)

class ChoosePatient(Screen):
    def storeAHC(self, a):
        self.AHC = a
    
    def search(self):
        self.exists = Patient().searchPatient(self.AHC)
        if self.exists == True:
            return 'Patient Screen'
        else: 
            return 'Error'


class PatientScreen(Screen):    #Comes from clicking button for existing patients
    def formatEditPatient(self):
        self.AHC = app.root.get_screen('Choose Patient').AHC
        self.patient = Patient(self.AHC)
        app.root.get_screen('Edit Patient').n.text = str(self.patient.getName().getFullName())
        app.root.get_screen('Edit Patient').ahc.text = str(self.patient.getAHC())
        app.root.get_screen('Edit Patient').sex.text = str(self.patient.getSex())
        app.root.get_screen('Edit Patient').dob.text = str(self.patient.getDOB())
        app.root.get_screen('Edit Patient').address.text = str(self.patient.getAddress().getAddress())
        app.root.get_screen('Edit Patient').pCode.text = str(self.patient.getAddress().getPostalCode())
        app.root.get_screen('Edit Patient').city.text = str(self.patient.getAddress().getCity())
        app.root.get_screen('Edit Patient').country.text = str(self.patient.getAddress().getCountry())
        phonelist = self.patient.getPatientPhone()
        disp = ""
        i = 0
        while i < len(phonelist):
            disp += phonelist[i].display()
            disp += " "
            i += 1
            
        app.root.get_screen('Edit Patient').phone.text = disp

    def formatDetails(self):
        self.AHC = app.root.get_screen('Choose Patient').AHC
        self.patient = Patient(self.AHC)
        self.name = self.patient.getName().getFullName()
        self.sex = self.patient.getSex()
        self.DOB = self.patient.getDOB()
        self.address = self.patient.getAddress().getAddress()
        self.pCode = self.patient.getAddress().getPostalCode()
        self.city = self.patient.getAddress().getCity()
        self.country = self.patient.getAddress().getCountry()
        self.invoices = self.patient.getAllInvoices()
        self.insurance = self.patient.getAllInsurances()
        self.examDetail = self.patient.getAllExamDetails()

        format = f"Details for {self.name} \n    AHC: {self.AHC} \n    Sex: {self.sex} \n    Date of Birth: {self.DOB} \n    Address: {self.address}, {self.pCode}, {self.city}, {self.country}"
        format += "\n\nInvoices: "
        i = 0
        while(i < len(self.invoices)):
            format += f"\n    Invoice ID: {self.invoices[i].getInvoiceID()}\n"
            i += 1

        format += f"\nInsurance: "
        i = 0
        while(i < len(self.insurance)):
            format += f"\n    Member ID: {self.insurance[i].getMemberID()}"
            format += f"\n    Policy No.: {self.insurance[i].getPolicyNO()}\n"
            i += 1

        format += f"\nExam Details: "
        i = 0
        while(i < len(self.examDetail)):
            format += f"\n    Date: {self.examDetail[i].getDate()}"
            format += f"\n    Performed By: {self.examDetail[i].getPerformed()}"
            format += f"\n    Referral Required: {self.examDetail[i].ReferralRequired()}"
            format += f"\n    Notes: {self.examDetail[i].getNotes()}\n"
            i += 1

        app.root.get_screen('View Patient Details').patientDetails.text = format

class AddInvoice(Screen):
    ID = 0
    def getDate(self):
        self.today = date.today()
        self.products = []
        return str(self.today.strftime("%Y-%b-%d"))
    
    def createID(self):
        self.ID += 1
        return str(self.ID)

    def checkbox_click(self, instance, value, id):
        if value is True:
            self.products.append(id) 
        else:
            self.products.remove(id)

        print(self.products)

    def addInvoice(self):
        self.AHC = app.root.get_screen('Choose Patient').AHC
        self.addInvoice = Patient(self.AHC).addNewInvoice(self.ID, self.today, self.products)

class AddExamDetail(Screen):
    def storeNotes(self, d):
        self.notes = d

    def addExamDetail(self):
        self.patient = Patient()

class AddInsurance(Screen):
    def storeMemberID(self, m):
        self.memberID = m

    def storePolicyNo(self, p):
        self.policyNo = p

    def addInsurance(self):
        self.AHC = app.root.get_screen('Choose Patient').AHC
        self.insurance = Patient(self.AHC).addInsurance(self.memberID, self.policyNo)

class ViewPatientDetails(Screen):
    pass 

class ViewExamDetail(Screen):
    pass

class Error(Screen):
    pass

class MobileApp(App):
    def build(self):
        self.sm = ScreenManager()
        self.sm.add_widget(MenuScreen(name='menu'))
        self.sm.add_widget(EmployeeLoginScreen(name='Employee Login'))
        self.sm.add_widget(EmployeePage(name='Employee Page'))
        self.sm.add_widget(PatientLoginScreen(name='Patient Login'))
        self.sm.add_widget(Error(name='Error'))
        self.sm.add_widget(PatientHomePage(name='Patient Home Page'))
        self.sm.add_widget(AppointmentScreen(name='Appointment'))
        self.sm.add_widget(PAppointmentScreen(name='PAppointment'))
        self.sm.add_widget(CreateAppointment(name='Create Appointment'))
        self.sm.add_widget(DeleteAppointment(name='Delete Appointment'))
        self.sm.add_widget(DeletePAppointment(name='Delete PAppointment'))
        self.sm.add_widget(ViewAppointment(name='View Appointment'))
        self.sm.add_widget(ViewPAppointment(name='View PAppointment'))
        self.sm.add_widget(EditEmployee(name='Edit Employee'))
        self.sm.add_widget(AddEmployee(name='Add Employee'))
        self.sm.add_widget(DeleteEmployee(name='Delete Employee'))
        self.sm.add_widget(ChoosePatient(name = 'Choose Patient'))
        self.sm.add_widget(PatientScreen(name = 'Patient Screen'))
        self.sm.add_widget(EditPatient(name='Edit Patient'))
        self.sm.add_widget(EditPatientInfo(name='Edit Patient Info'))
        self.sm.add_widget(AddPatient(name='Add Patient'))
        self.sm.add_widget(AddInvoice(name='Add Invoice'))
        # self.sm.add_widget(AddExamDetail(name='Add Exam Detail'))
        self.sm.add_widget(AddInsurance(name='Add Insurance'))
        self.sm.add_widget(ViewPatientDetails(name='View Patient Details'))
        # self.sm.add_widget(CreateReferralLetter(name='Create Referral Letter'))
        self.sm.add_widget(ViewExamDetail(name='View Exam Detail'))

        return self.sm


if __name__ == "__main__":
    app = MobileApp()
    app.run()