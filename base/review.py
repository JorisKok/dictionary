import os
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
from kivy.properties import ObjectProperty, StringProperty
import random

view = Builder.load_file(os.path.dirname(__file__) + "/view/review.kv")


class Review(Screen):

    # The dictionary base
    dictionary = ObjectProperty(None)

    # The fonts
    font = StringProperty(None)
    font_awesome = StringProperty(None)

    # Flash cards
    cards = ObjectProperty(None)

    def __init__(self, **kwargs):
        super(Review, self).__init__(**kwargs)

        # Get the cards to review
        self.get_cards()

        # Set the card to the view
        self.set_card()

    def remove_button_clicked(self):
        pass

    def get_cards(self):
        self.cards = self.dictionary.app.review.get_cards()

    def set_card(self):
        nr = random.randint(0, len(self.cards)-1)
        card = self.cards[nr]
        # Easy way to fix duplicate card review
        if card.text() == self.ids.flashcard.text:
            if len(self.cards)-1 == nr:
                nr -= 1
            else:
                nr += 1
            card = self.cards[nr]

        self.ids.flashcard.text = card.text()

    def easy_clicked(self):
        self.set_card()

    def difficult_clicked(self):
        self.set_card()
