from kivy.properties import ObjectProperty
from kivy.uix.screenmanager import ScreenManager
from base.search import Search
from base.word import Word
from base.menu import Menu
from base.review import Review


class Dictionary(ScreenManager):

    # The main app
    app = ObjectProperty(None)
    menu = ObjectProperty(None)
    search = ObjectProperty(None)
    word = ObjectProperty(None)
    review = ObjectProperty(None)

    # The currently selected search result data
    search_result = ObjectProperty(None)

    def __init__(self, font, font_awesome, **kwargs):
        super(Dictionary, self).__init__(**kwargs)

        self.menu = Menu(dictionary=self, name="menu", font=font, font_awesome=font_awesome)
        self.word = Word(dictionary=self, name="word", font=font, font_awesome=font_awesome)
        self.search = Search(dictionary=self, name="search", font=font, font_awesome=font_awesome)
        self.review = Review(dictionary=self, name="review", font=font, font_awesome=font_awesome)

        # Set the search screen as default
        self.add_widget(self.search)
        self.add_widget(self.menu)
        self.add_widget(self.word)
        self.add_widget(self.review)
