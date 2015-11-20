import os
from kivy.uix.screenmanager import Screen
from kivy.lang import Builder
from kivy.properties import ObjectProperty, StringProperty

view = Builder.load_file(os.path.dirname(__file__) + "/view/word.kv")


class Word(Screen):

    dictionary = ObjectProperty(None)

    # The fonts
    font = StringProperty(None)
    font_awesome = StringProperty(None)

    @property
    def definition(self):
        return self.dictionary.search_result.definition

    @property
    def title(self):
        return self.dictionary.search_result.title

    @property
    def character(self):
        return self.dictionary.search_result.character

    def __init__(self, **kwargs):
        super(Word, self).__init__(**kwargs)

    def on_pre_enter(self, *args):
        # Set all the data
        self.ids.definition.text = self.definition
        self.ids.title.text = self.title
        # self.ids.character.text = self.character
