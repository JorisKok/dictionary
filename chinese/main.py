import kivy
kivy.require("1.9.0")

from kivy.app import App
from base.dictionary import Dictionary
from kivy.core.window import Window
from typing import Undefined
from chinese.search import Search
from chinese.review import Review


class Chinese(App):

    # Needed for searching the db from /base
    search = Undefined(Search)
    review = Undefined(Review)

    def build(self):

        self.search = Search()
        self.review = Review()

        # Set the background color for the app
        Window.clearcolor = (0.9, 0.9, 0.9, 1)

        return Dictionary(app=self,
                          font="file/font/chinese_１.ttc",
                          font_awesome="file/font/font_awesome.ttf")


if __name__ == '__main__':
    Chinese().run()
