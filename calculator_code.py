from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.core.window import Window
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput

# Set the appp size
Window.size = (500, 700)

class MyGridLayout(GridLayout):
    def __init__(self, **kwargs):
        super(MyGridLayout, self).__init__(**kwargs)

        # Set colums
        self.cols = 1

        # Create Text Input
        self.calc_input = TextInput(text='0', font_size = 65, halign = 'right', size_hint = (1, .15))
        self.add_widget(self.calc_input)

        # Create a Second GridLayout
        self.top_grid = GridLayout(
            row_force_default = True,
            row_default_height=125,
            col_force_default = True,
            col_default_width = 125
        )
        self.top_grid.cols = 4
        self.top_grid.rows = 5

        # Row
        self.percentbutton = Button(text = "%", font_size = 32,
                        size_hint_y = None,
                        height = 125,
                        size_hint_x = None,
                        width = 125)
        self.top_grid.add_widget(self.percentbutton)
        self.percentbutton.bind(on_press= self.percent)

        self.submit = Button(text = "<<", font_size = 32,
                        size_hint_y = None,
                        height = 125,
                        size_hint_x = None,
                        width = 125)
        self.top_grid.add_widget(self.submit)
        self.submit.bind(on_press= self.remove)

        self.clearbutton = Button(text = "C", font_size = 32,
                        size_hint_y = None,
                        height = 125,
                        size_hint_x = None,
                        width = 125)
        self.top_grid.add_widget(self.clearbutton)
        self.clearbutton.bind(on_press= self.clear)

        self.submit = Button(text = "/", font_size = 32,
                        size_hint_y = None,
                        height = 125,
                        size_hint_x = None,
                        width = 125)
        self.top_grid.add_widget(self.submit)
        self.submit.bind(on_press= self.divide)

        # Row
        self.sevenbutton = Button(text = "7", font_size = 32,
                        size_hint_y = None,
                        height = 125,
                        size_hint_x = None,
                        width = 125,
                        background_color = (157/255, 157/255, 157/255, 1))
        self.top_grid.add_widget(self.sevenbutton)
        self.sevenbutton.bind(on_press= lambda instance: self.press_button(instance,7))

        self.submit = Button(text = "8", font_size = 32,
                        size_hint_y = None,
                        height = 125,
                        size_hint_x = None,
                        width = 125,
                        background_color = (157/255, 157/255, 157/255, 1))
        self.top_grid.add_widget(self.submit)
        self.submit.bind(on_press= lambda instance: self.press_button(instance,8))

        self.submit = Button(text = "9", font_size = 32,
                        size_hint_y = None,
                        height = 125,
                        size_hint_x = None,
                        width = 125,
                        background_color = (157/255, 157/255, 157/255, 1))
        self.top_grid.add_widget(self.submit)
        self.submit.bind(on_press= lambda instance: self.press_button(instance,9))

        self.submit = Button(text = "x", font_size = 32,
                        size_hint_y = None,
                        height = 125,
                        size_hint_x = None,
                        width = 125)
        self.top_grid.add_widget(self.submit)
        self.submit.bind(on_press= self.multiply)

        # Row
        self.submit = Button(text = "4", font_size = 32,
                        size_hint_y = None,
                        height = 125,
                        size_hint_x = None,
                        width = 125,
                        background_color = (157/255, 157/255, 157/255, 1))
        self.top_grid.add_widget(self.submit)
        self.submit.bind(on_press= lambda instance: self.press_button(instance,4))

        self.submit = Button(text = "5", font_size = 32,
                        size_hint_y = None,
                        height = 125,
                        size_hint_x = None,
                        width = 125,
                        background_color = (157/255, 157/255, 157/255, 1))
        self.top_grid.add_widget(self.submit)
        self.submit.bind(on_press= lambda instance: self.press_button(instance,5))

        self.submit = Button(text = "6", font_size = 32,
                        size_hint_y = None,
                        height = 125,
                        size_hint_x = None,
                        width = 125,
                        background_color = (157/255, 157/255, 157/255, 1))
        self.top_grid.add_widget(self.submit)
        self.submit.bind(on_press= lambda instance: self.press_button(instance,6))

        self.submit = Button(text = "-", font_size = 32,
                        size_hint_y = None,
                        height = 125,
                        size_hint_x = None,
                        width = 125)
        self.top_grid.add_widget(self.submit)
        self.submit.bind(on_press= self.sub)

        # Row
        self.submit = Button(text = "1", font_size = 32,
                        size_hint_y = None,
                        height = 125,
                        size_hint_x = None,
                        width = 125,
                        background_color = (157/255, 157/255, 157/255, 1))
        self.top_grid.add_widget(self.submit)
        self.submit.bind(on_press= lambda instance: self.press_button(instance,1))

        self.submit = Button(text = "2", font_size = 32,
                        size_hint_y = None,
                        height = 125,
                        size_hint_x = None,
                        width = 125,
                        background_color = (157/255, 157/255, 157/255, 1))
        self.top_grid.add_widget(self.submit)
        self.submit.bind(on_press= lambda instance: self.press_button(instance,2))

        self.submit = Button(text = "3", font_size = 32,
                        size_hint_y = None,
                        height = 125,
                        size_hint_x = None,
                        width = 125,
                        background_color = (157/255, 157/255, 157/255, 1))
        self.top_grid.add_widget(self.submit)
        self.submit.bind(on_press= lambda instance: self.press_button(instance,3))

        self.submit = Button(text = "+", font_size = 32,
                        size_hint_y = None,
                        height = 125,
                        size_hint_x = None,
                        width = 125)
        self.top_grid.add_widget(self.submit)
        self.submit.bind(on_press= self.add)

        # Row
        self.submit = Button(text = "+/-", font_size = 32,
                        size_hint_y = None,
                        height = 125,
                        size_hint_x = None,
                        width = 125,
                        background_color = (157/255, 157/255, 157/255, 1))
        self.top_grid.add_widget(self.submit)
        self.submit.bind(on_press= self.plus_minus)

        self.submit = Button(text = "0", font_size = 32,
                        size_hint_y = None,
                        height = 125,
                        size_hint_x = None,
                        width = 125,
                        background_color = (157/255, 157/255, 157/255, 1))
        self.top_grid.add_widget(self.submit)
        self.submit.bind(on_press= lambda instance: self.press_button(instance,0))

        self.submit = Button(text = ".", font_size = 32,
                        size_hint_y = None,
                        height = 125,
                        size_hint_x = None,
                        width = 125,
                        background_color = (157/255, 157/255, 157/255, 1))
        self.top_grid.add_widget(self.submit)
        self.submit.bind(on_press= self.dot)

        self.submit = Button(text = "=", font_size = 32,
                        size_hint_y = None,
                        height = 125,
                        size_hint_x = None,
                        width = 125)
        self.top_grid.add_widget(self.submit)
        self.submit.bind(on_press= self.equal)

        # Add the new top_grid to our_app
        self.add_widget(self.top_grid)

    
    def press_button(self, instance, value):
        prior = self.calc_input.text
        number = str(value)

        if prior == '0':
            self.calc_input.text = ''
            self.calc_input.text = f'{number}'
        else:
            self.calc_input.text = f'{prior}{number}'
    
    def clear(self, instance):
        self.calc_input.text = '0'
    
    # Add Function
    def add(self, instance):
        prior = self.calc_input.text

        self.calc_input.text = f'{prior}+'
    
    def divide(self, instance):
        prior = self.calc_input.text

        self.calc_input.text = f'{prior}/'
    
    def multiply(self, instance):
        prior = self.calc_input.text

        self.calc_input.text = f'{prior}*'
    
    def sub(self, instance):
        prior = self.calc_input.text

        self.calc_input.text = f'{prior}-'
    
    def equal(self, instance):
        prior = self.calc_input.text

        try:
            answer = eval(prior)
            self.calc_input.text = f'{answer}'
        except:
            self.calc_input.text = 'Error!'
    
    def remove(self, instance):
        prior = self.calc_input.text
        self.calc_input.text = prior[:-1]
    
    def plus_minus(self, instance):
        prior = self.calc_input.text
        if "-" in prior:
            self.calc_input.text = prior.replace('-','+')
        else:
            self.calc_input.text = prior.replace('+','-')
    
    def dot(self, instance):
        prior = self.calc_input.text
        num_list = prior.split("+")

        if "+" in prior and "." not in num_list[-1]:
            prior = f'{prior}.'
            self.calc_input.text = prior
        elif '.' in prior:
            pass
        else:
            prior = f'{prior}.'
            self.calc_input.text = prior
    
    def percent(self, instance):
        prior = self.calc_input.text

        try:
            answer = str(float(prior)/100)
            self.calc_input.text = f'{answer}'
        except:
            self.calc_input.text = 'Error!'

class CalculatorApp(App):
    def build(self):
        return MyGridLayout()

if __name__ == '__main__':
    CalculatorApp().run()