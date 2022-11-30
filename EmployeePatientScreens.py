from Employee import *
from Patient import *

from kivy.uix.gridlayout import GridLayout
from kivy.app import App
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
<ChoosePatient>:
    GridLayout: 
        spacing: 20, 20 
        cols: 1

        Label:
            text: 'Enter Patient Alberta Health Care Number'
            font_size: 20
            color: "#000000"

        TextInput:
            id: name
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
            
                root.manager.current = 'Edit Patient'

        Button:
            text: 'Add Exam Detail'
            font_size: 20
            background_color: 0, 0, 8, 0.5
            on_press: root.manager.current = root.search()

        Button:
            text: 'Add Invoices'
            font_size: 20
            background_color: 0, 0, 8, 0.5
            on_press: root.manager.current = root.search()

        Button:
            text: 'Add Insurance'
            font_size: 20
            background_color: 0, 0, 8, 0.5
            on_press: root.manager.current = root.search()

        Button:
            text: 'View Patient Details'
            font_size: 20
            background_color: 0, 0, 8, 0.5
            on_press: root.manager.current = root.search()

        Button:
            text: 'Create Referral Letter'
            font_size: 20
            background_color: 0, 0, 8, 0.5
            on_press: root.manager.current = root.search()

        Button:
            text: 'Back'
            font_size: 20
            background_color: 0, 0, 8, 0.5
            on_press: root.manager.current = 'Employee Page'
        
<EditPatient>:
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
            id: name
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
            id: country
            multiline: False
            size_hint: (1, 0.7)
            font_size: 20
            on_text: root.storeSex(self.text)

        Label:
            text_size: self.size
            halign: 'right'
            valign: 'middle' 
            text: 'Alberta Health Card Number:  '
            font_size: 20
            color: "#000000"

        TextInput:
            id: AHC
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
            id: DOB
            multiline: False
            size_hint: (1, 0.7)
            font_size: 20
            text: 'YYYY-MM-DD'
            on_text: root.storeDOB(self.text)

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
        cols: 2

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

<AddExamDetail>:
    GridLayout:
        spacing: 20, 20 
        cols: 1

    Button:
        text: 'Add Exam Detail'
        font_size: 20
        background_color: 0, 0, 8, 0.5
        on_press: 
            root.addExamDetail()
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

""")


class EditPatient(Screen):
    def storeName(self, n = None):
        self.name = n
    
    def storeAHC(self, a = None):
        self.AHC = a
    
    def storeDOB(self, d = None):
        self.DOB = d
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
    
    def makeChanges(self):
        #first check if patient SIN already exists in database
        #if it does exist then make changes to that patient
        self.patient = Patient().exists(self.SIN)
        if (self.patient == True):
            if self.address != None:
                self.patient.setAddress(self.address)
                self.patient.setCity(self.city)
                self.patient.setCountry()

        #if patient doesn't exist then create new patient
        else: 
            self.patient = Patient().addPatient(self.AHC, self.sex, self.DOB, self.name, self.address, self.city, self.country, self.pCode)

class ChoosePatient(Screen):
    def storeAHC(self, a):
        self.AHC = a
    
    def search(self):
        self.patient = Patient().searchPatient(self.AHC)


class PatientScreen(Screen):    #Comes from clicking button for existing patients
    pass

class AddInvoice(Screen):
    pass 

class AddExamDetail(Screen):
    pass 

class AddInsurance(Screen):
    pass 

class ViewPatientDetails(Screen):
    pass 

class CreateReferralLetter(Screen):
    pass

class MobileApp(App):
    def build(self):
        self.sm = ScreenManager()
        #self.sm.add_widget(ChoosePatient(name = 'Choose Patient'))
        #self.sm.add_widget(PatientScreen(name = 'Patient Screen'))
        self.sm.add_widget(EditPatient(name='Edit Patient'))
        self.sm.add_widget(AddInvoice(name='Add Invoice'))
        self.sm.add_widget(AddExamDetail(name='Add ExamDetail'))
        self.sm.add_widget(AddInsurance(name='Add Insurance'))
        self.sm.add_widget(ViewPatientDetails(name='View Patient Details'))
        self.sm.add_widget(CreateReferralLetter(name='Create Referral Letter'))

        

        return self.sm
        
if __name__ == "__main__":
    app = MobileApp()
    app.run()
