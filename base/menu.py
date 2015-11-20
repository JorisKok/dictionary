import os
from kivy.lang import Builder
from kivy.properties import ObjectProperty
from kivy.uix.screenmanager import Screen

view = Builder.load_file(os.path.dirname(__file__) + "/view/menu.kv")


class Menu(Screen):

    # Reference to the dictionary
    dictionary = ObjectProperty(None)

    def __init__(self, **kwargs):
        super(Menu, self).__init__(**kwargs)

    def search_button_clicked(self):
        pass

    def review_button_clicked(self):
        pass
