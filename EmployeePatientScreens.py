from Employee import *
from Patient import *
from Invoice import *
from datetime import date 

from kivy.uix.gridlayout import GridLayout
from kivy.app import App
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
                root.manager.current = 'Patient Screen'


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

""")

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


# class AddExamDetail(Screen):
#     def storeNotes(self, d):
#         self.notes = d

#     def addExamDetail(self):
#         self.patient = Patient()

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

# class CreateReferralLetter(Screen):
#     pass

class MobileApp(App):
    def build(self):
        self.sm = ScreenManager()
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

        return self.sm
        
if __name__ == "__main__":
    app = MobileApp()
    app.run()
