import kivy 
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen

from kivy.core.window import Window
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
            multiline: False
            size_hint: (1, 0.7)
            font_size: 30
            on_text: root.storeUsername(self.text)

        Label: 
            text: 'Password'
            font_size: 50
            color: "#000000"
            
        TextInput:
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

<EmployeeHomePage>:
    GridLayout:
        cols: 1  
        
        Label: 
            text: 'Employee Home Page'
            font_size: 50
            color: "#000000"
        
        Button:
            text: 'Option 1'
            font_size: 30
            background_color: 0, 0, 8, 0.5
            on_press: root.manager.current = 'menu'

        Button:
            text: 'Option 2'
            font_size: 30
            background_color: 0, 0, 8, 0.5
            on_press: root.manager.current = 'menu'

        Button:
            text: 'Option 3'
            font_size: 30
            background_color: 0, 0, 8, 0.5
            on_press: root.manager.current = 'menu'

        Button:
            text: 'Option 4'
            font_size: 30
            background_color: 0, 0, 8, 0.5
            on_press: root.manager.current = 'menu'

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
            multiline: False
            size_hint: (1, 0.7)
            font_size: 30
            on_text: root.storeUsername(self.text)

        Label: 
            text: 'Password'
            font_size: 50
            color: "#000000"
        
        TextInput:
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
        cols: 2    
        
        Label: 
            text: 'Patient Home Page'
            font_size: 50
            color: "#000000"

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
        if (self.username == "sobia" and self.password == "890"):
            return 'Employee Home Page'
        else:
            return 'Error'

class PatientLoginScreen(Screen):
    def storeUsername(self, u):
        self.username = u
    
    def storePassword(self, p):
        self.password = p

    def verify(self):
        if (self.username == "sobia" and self.password == "890"):
            return 'Patient Home Page'
        else:
            return 'Error'

class EmployeeHomePage(Screen):
    pass

class PatientHomePage(Screen):
    pass

class Error(Screen):
    pass

class MobileApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(MenuScreen(name='menu'))
        sm.add_widget(EmployeeLoginScreen(name='Employee Login'))
        sm.add_widget(PatientLoginScreen(name='Patient Login'))
        sm.add_widget(EmployeeHomePage(name='Employee Home Page'))
        sm.add_widget(PatientHomePage(name='Patient Home Page'))
        sm.add_widget(Error(name='Error'))

        return sm

if __name__ == "__main__":
    MobileApp().run()