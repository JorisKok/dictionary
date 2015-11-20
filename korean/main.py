from kivy.app import App
from base.dictionary import Dictionary
from korean.search import Search
from korean.database import Database
from kivy.core.window import Window
from typing import Undefined


class Korean(App):

    search = Undefined("Search")

    def build(self):

        self.search = Search()

        # Init the database
        Database()

        # Set the background color for the app
        Window.clearcolor = (0.9, 0.9, 0.9, 1)

        return Dictionary(app=self,
                          font="file/font/korean_1.ttf",
                          font_awesome="file/font/font_awesome.ttf")

if __name__ == '__main__':
    Korean().run()
