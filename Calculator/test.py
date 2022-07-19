from turtle import width
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput



class MyGridLayout(GridLayout):
    def __init__(self, **kwargs):
        super(MyGridLayout, self).__init__(**kwargs)

        # Set colums
        self.cols = 1

        # Create a Second GridLayout
        self.top_grid = GridLayout(
            row_force_default = True,
            row_default_height=50,
            col_force_default = True,
            col_default_width = 400
        )
        self.top_grid.cols = 2



        self.top_grid.add_widget(Label(text ="Name: "))
        self.name = TextInput(multiline=True)
        self.top_grid.add_widget(self.name)

        self.top_grid.add_widget(Label(text ="favorite pizz: "))
        self.pizz = TextInput(multiline=False)
        self.top_grid.add_widget(self.pizz)

        self.top_grid.add_widget(Label(text ="favorite color: "))
        self.color = TextInput(multiline=False)
        self.top_grid.add_widget(self.color)

        # Add the new top_grid to our_app
        self.add_widget(self.top_grid)

        self.submit = Button(text = "Submit", font_size = 32,
                        size_hint_y = None,
                        height = 50,
                        size_hint_x = None,
                        width = 200)
        self.submit.bind(on_press= self.press)
        self.add_widget(self.submit)
    
    def press(self, instance):
        name = self.name.text
        pizz = self.pizz.text
        color = self.color.text

        self.add_widget(Label(text =f'Hello {name}, {pizz} and your favorite color is {color}'))

        self.name.text = ''
        self.pizz.text = ''
        self.color.text = ''

class MyApp(App):
    def build(self):
        return MyGridLayout()

if __name__ == '__main__':
    MyApp().run()