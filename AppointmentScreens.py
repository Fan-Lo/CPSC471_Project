from Appointment import *

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
<AppointmentScreen>:
    GridLayout:
        cols: 1
        spacing: 20, 20

        Button:
            text: 'Create Appointment'
            font_size: 30
            background_color: 0, 0, 8, 0.5
            on_press: root.manager.current = 'Create Appointment'

        Button:
            text: 'Delete Appointment'   
            font_size: 30
            background_color: 0, 0, 8, 0.5
            on_press: root.manager.current = 'Delete Appointment'

        Button:
            text: 'View Appointment'
            font_size: 30
            background_color: 0, 0, 8, 0.5
            on_press: 
                app.root.get_screen('View Appointment').message.text = root.getAppointments()
                root.manager.current = 'View Appointment'

        Button:
            text: 'Back'
            font_size: 30
            background_color: 0, 0, 8, 0.5
            on_press: root.manager.current = 'Employee Page'

<CreateAppointment>:
    GridLayout: 
        cols: 2
        spacing: 20, 20

        Label: 
            text: 'Patient Alberta Health Care Number:  '
            font_size: 20
            color: '#000000'
            text_size: self.size
            halign: 'right'
            valign: 'middle'
        
        TextInput:
            id: AHC
            multiline: False
            size_hint: (1, 0.7)
            font_size: 20
            on_text: root.storeAHC(self.text)


        Label: 
            text: 'Employee Last Name:  '
            font_size: 20
            color: "#000000"
            text_size: self.size
            halign: 'right'
            valign: 'middle'
        
        TextInput:
            id: name
            multiline: False
            size_hint: (1, 0.7)
            font_size: 20
            on_text: root.storeLname(self.text)


        Label: 
            text: 'Date:    '
            font_size: 20
            color: "#000000"
            text_size: self.size
            halign: 'right'
            valign: 'middle'
        
        TextInput:
            id: date
            multiline: False
            size_hint: (1, 0.7)
            font_size: 20
            on_text: root.storeDate(self.text)


        Label: 
            text: 'Time:    '
            font_size: 20
            color: "#000000"
            text_size: self.size
            halign: 'right'
            valign: 'middle'
        
        TextInput:
            id: time
            multiline: False
            size_hint: (1, 0.7)
            font_size: 20
            on_text: root.storeTime(self.text)

        Button:
            text: 'Cancel'
            font_size: 30
            background_color: 0, 0, 8, 0.5
            on_press: root.manager.current = 'Appointment'
            
        Button:
            text: 'Create Appointment'
            font_size: 30
            background_color: 0, 0, 8, 0.5
            on_press:  
                root.addAppointment()
                root.manager.current = 'Appointment'
                                 
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
                root.manager.current = 'Appointment'

        Button:
            text: 'Cancel'
            font_size: 30
            background_color: 0, 0, 8, 0.5
            on_press: root.manager.current = 'Appointment'

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
            on_press: root.manager.current = 'Appointment'

<PAppointmentScreen>:
    GridLayout:
        cols: 1
        spacing: 20, 20

        Button:
            text: 'Delete Appointment'   
            font_size: 30
            background_color: 0, 0, 8, 0.5
            on_press: root.manager.current = 'Delete PAppointment'

        Button:
            text: 'View Appointment'
            font_size: 30
            background_color: 0, 0, 8, 0.5
            on_press: 
                app.root.get_screen('View PAppointment').message.text = root.getPAppointments()
                root.manager.current = 'View PAppointment'

        Button:
            text: 'Back'
            font_size: 30
            background_color: 0, 0, 8, 0.5
            on_press: root.manager.current = 'Patient Home Page'

<DeletePAppointment>:
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

<ViewPAppointment>:
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

""")

class AppointmentScreen(Screen):
    def getAppointments(self):
        self.allAppointment = Appointment().viewAppointments(self.SIN)
        return self.allAppointment

class PAppointmentScreen(Screen):
    def getPAppointments(self):
        self.allAppointment = Appointment().viewPAppointments(self.AHC)
        return self.allAppointment

class CreateAppointment(Screen):
    def storeAHC(self, AHC):
        self.AHC = AHC 

    def storeLname(self, Lname):
        self.Lname = Lname

    def storeDate(self, date):
        self.date = date 

    def storeTime(self, time):
        self.time = time 

    def addAppointment(self):
        self.newAppointment = Appointment().addAppointment(self.AHC, self.date, self.time, self.Lname) 
    
class DeleteAppointment(Screen):
    def storeAHC(self, AHC):
        self.AHC = AHC 

    def storeDate(self, date):
        self.date = date 

    def storeTime(self, time):
        self.time = time 

    def deleteAppointment(self):
        self.newAppointment = Appointment().deleteAppointment(self.AHC, self.date, self.time) 

class DeletePAppointment(Screen):
    def storeAHC(self, AHC):
        self.AHC = AHC 

    def storeDate(self, date):
        self.date = date 

    def storeTime(self, time):
        self.time = time 

    def deletePAppointment(self):
        self.newAppointment = Appointment().deletePAppointment(self.AHC, self.date, self.time) 

class ViewAppointment(Screen):
    pass

class ViewPAppointment(Screen):
    pass
'''
class MobileApp(App):
    def build(self):
        self.sm = ScreenManager()
        self.sm.add_widget(AppointmentScreen(name='Appointment'))
        self.sm.add_widget(CreateAppointment(name='Create Appointment'))
        self.sm.add_widget(DeleteAppointment(name='Delete Appointment'))
        self.sm.add_widget(ViewAppointment(name='View Appointment'))

        return self.sm
        
if __name__ == "__main__":
    app = MobileApp()
    app.run()
'''