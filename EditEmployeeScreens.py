from Employee import *

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
<EditEmployee>:
    GridLayout:
        cols: 1
        spacing: 20, 20

        Button: 
            text: 'Add Employee'
            font_size: 30
            background_color: 0, 0, 8, 0.5
            on_press: root.manager.current = 'Add Employee'

        Button: 
            text: 'Remove Employee'
            font_size: 30
            background_color: 0, 0, 8, 0.5
            on_press: root.manager.current = 'Delete Employee'

        Button: 
            text: 'Back'
            font_size: 30
            background_color: 0, 0, 8, 0.5
            on_press: root.manager.current = 'Employee Page'

<DeleteEmployee>:
    GridLayout:
        cols: 2

        Label: 
            text: 'Enter Employee Last Name or SIN:     '
            font_size: 20
            color: '#000000'
            text_size: self.size
            halign: 'right'
            valign: 'middle'

        TextInput: 
            multiline: False
            size_hint: (1, 0.7)
            font_size: 20
            on_text: root.storeName(self.text)

        Button: 
            text: 'Cancel'
            font_size: 30
            background_color: 0, 0, 8, 0.5
            on_press: root.manager.current = 'Edit Employee'
            
        Button: 
            text: 'Remove Employee'
            font_size: 30
            background_color: 0, 0, 8, 0.5
            on_press: 
                root.remove()
                root.manager.current = 'Edit Employee'

<AddEmployee>:
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
            text: 'Social Insurace Number:  '
            font_size: 20
            color: "#000000"

        TextInput:
            id: SIN
            multiline: False
            size_hint: (1, 0.7)
            font_size: 20
            on_text: root.storeSIN(self.text)
        
        Label: 
            text_size: self.size
            halign: 'right'
            valign: 'middle'        
            text: 'Date of Birth:   '
            font_size: 20
            color: "#000000"

        TextInput:
            id: self.DOB
            multiline: False
            size_hint: (1, 0.7)
            font_size: 20
            text: 'YYYY-MM-DD'
            on_text: root.storeDOB(self.text)

        Label:
            text_size: self.size
            halign: 'right'
            valign: 'middle' 
            text: 'Supervisor Social Insurance Number'
            font_size: 20
            color: "#000000"

        TextInput:
            id: self.superSIN
            multiline: False
            size_hint: (1, 0.7)
            font_size: 20
            on_text: root.storeSuperSIN(self.text)

        Label: 
            text_size: self.size
            halign: 'right'
            valign: 'middle'
            text: 'Job Type'
            font_size: 20
            color: "#000000"

        TextInput:
            id: self.jobType
            multiline: False
            size_hint: (1, 0.7)
            font_size: 20
            on_text: root.storeJobType(self.text)
                
        Label: 
            text_size: self.size
            halign: 'right'
            valign: 'middle'
            text: 'Office Phone    '
            font_size: 20
            color: "#000000"

        TextInput:
            id: self.oPhone
            multiline: False
            size_hint: (1, 0.7)
            font_size: 20
            text: 'XXX-XXX-XXXX'
            on_text: root.storePhone(self.text)

        Label: 
            text_size: self.size
            halign: 'right'
            valign: 'middle'
            text: 'New Employee Password    '
            font_size: 20
            color: "#000000"

        TextInput:
            id: self.oPhone
            multiline: False
            size_hint: (1, 0.7)
            font_size: 20
            password: True
            on_text: root.storePassword(self.text)

        Button:
            text: 'Cancel'
            font_size: 20
            background_color: 0, 0, 8, 0.5
            on_press: root.manager.current = 'Edit Employee'
            
        Button:
            text: 'Add Employee'
            font_size: 20
            background_color: 0, 0, 8, 0.5
            on_press: 
                root.addEmployee()
                root.manager.current = 'Edit Employee'

""")

class EditEmployee(Screen):
    pass 

class AddEmployee(Screen):
    def storeName(self, n):
        self.name = n

    def storeSIN(self, s):
        self.SIN = s

    def storePhone(self, p):
        self.ophone = p

    def storeJobType(self, j):
        self.jobType = j

    def storeDOB(self, d):
        self.DOB = d

    def storeSuperSIN(self, s):
        self.superSIN = s

    def storePassword(self, p):
        self.password = p

    def addEmployee(self):
        self.employee = Employee().addEmp(self.SIN, self.ophone, self.jobType, self.superSIN, self.DOB, self.name, self.password)

class DeleteEmployee(Screen):
    def storeName(self, t):
        self.Lname = t

    def remove(self):
        self.employee = Employee(self.Lname)
        self.employee.deleteEmp()
        
class MobileApp(App):
    def build(self):
        self.sm = ScreenManager()
        self.sm.add_widget(EditEmployee(name='Edit Employee'))
        self.sm.add_widget(AddEmployee(name='Add Employee'))
        self.sm.add_widget(DeleteEmployee(name='Delete Employee'))

        return self.sm
        
if __name__ == "__main__":
    app = MobileApp()
    app.run()