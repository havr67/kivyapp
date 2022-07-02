from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.scrollview import ScrollView
from kivy.uix.dropdown import DropDown
from kivy.uix.popup import Popup
from kivy.uix.image import Image


class MainWidget(Widget):
    pass

class MyGrid(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.cols = 1
        self.inside = GridLayout(cols=2)
        self.inside.add_widget(Label(text='Name: '))
        self.name = TextInput(multiline=False)
        self.inside.add_widget(self.name)
        self.inside.add_widget(Label(text='Last: '))
        self.lastname = TextInput(multiline=False)
        self.inside.add_widget(self.lastname)
        self.add_widget(self.inside)
        self.button = Button(text='Submit')
        self.button.bind(on_press=self.pressed)
        self.add_widget(self.button)

    def pressed(self, instance):
        print('Pressed!')
        print(self.name.text)
        print(self.lastname.text)
        print(self.button.text)

class MyApp(App):
    def build(self):
        return MyGrid()


if __name__ == '__main__':
    MyApp().run()

