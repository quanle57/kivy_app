from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window
from FirstPage import FirstWindowLayout
from SecondPage import SecondWindowLayout


# Designate our .kv file
Builder.load_file('ui/first_page.kv')
Builder.load_file('ui/second_page.kv')

class MyLayout(GridLayout):
    pass

class MyApp(App):
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.first_scr = FirstWindowLayout(name='first')
        self.second_scr = SecondWindowLayout(name='second')

        self.scr_manager = ScreenManager()
        self.scr_manager.add_widget(self.first_scr)
        self.scr_manager.add_widget(self.second_scr)

    def build(self):
        Window.clearcolor = (1,1,1,1)
        self.title = "Demo App"
        self.icon = "banana.png"

        return self.scr_manager

if __name__ == '__main__':
    MyApp().run()