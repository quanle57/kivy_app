from kivy.uix.screenmanager import Screen


class FirstWindowLayout(Screen):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
    
    def set_data(self):
        self.manager.get_screen("second").ids.textt.text =  "{} {} like {}".format(self.ids.first_name.text, self.ids.last_name.text, self.ids.color.text)
