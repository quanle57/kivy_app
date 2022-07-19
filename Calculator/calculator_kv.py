from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.lang import Builder
from kivy.core.window import Window

# Set the appp size
# Window.size = (500, 700)

Builder.load_file('calculatorapp.kv')

class MyLayout(Widget):
    def clear(self):
        self.ids.calc_input.text = '0'
    
    def press_button(self, number):
        prior = self.ids.calc_input.text

        if prior == '0':
            self.ids.calc_input.text = ''
            self.ids.calc_input.text = f'{number}'
        else:
            self.ids.calc_input.text = f'{prior}{number}'
    
    # Add Function
    def add(self):
        prior = self.ids.calc_input.text

        self.ids.calc_input.text = f'{prior}+'
    
    def divide(self):
        prior = self.ids.calc_input.text

        self.ids.calc_input.text = f'{prior}/'
    
    def multiply(self):
        prior = self.ids.calc_input.text

        self.ids.calc_input.text = f'{prior}*'
    
    def sub(self):
        prior = self.ids.calc_input.text

        self.ids.calc_input.text = f'{prior}-'
    
    def equal(self):
        prior = self.ids.calc_input.text

        try:
            answer = eval(prior)
            self.ids.calc_input.text = f'{answer}'
        except:
            self.ids.calc_input.text = 'Error!'
    
    def remove(self):
        prior = self.ids.calc_input.text
        self.ids.calc_input.text = prior[:-1]
    
    def plus_minus(self):
        prior = self.ids.calc_input.text
        if "-" in prior:
            self.ids.calc_input.text = prior.replace('-','+')
        else:
            self.ids.calc_input.text = prior.replace('+','-')
    
    def dot(self):
        prior = self.ids.calc_input.text
        num_list = prior.split("+")

        if "+" in prior and "." not in num_list[-1]:
            prior = f'{prior}.'
            self.ids.calc_input.text = prior
        elif '.' in prior:
            pass
        else:
            prior = f'{prior}.'
            self.ids.calc_input.text = prior

class CalculatorApp(App):
    def build(self):
        return MyLayout()

if __name__ == '__main__':
    CalculatorApp().run()