from kivy.properties import StringProperty, NumericProperty, ObjectProperty
from kivy.uix.widget import Widget
from base.dataclass.flashcard import FlashCardBase
# An object used for generic flash cards


class FlashCard(FlashCardBase, Widget):

    key = NumericProperty()  # Id in the db
    traditional = StringProperty()
    simplified = StringProperty()
    pinyin = StringProperty()
    english = StringProperty()
    sentence_traditional = StringProperty()
    sentence_simplified = StringProperty()
    sentence_pinyin = StringProperty()
    sentence_english = StringProperty()
    review_time = NumericProperty()

    @property
    def id_as_string(self):
        return StringProperty(self.key)

    @id_as_string.setter
    def id_as_string(self, key: str):
        return NumericProperty(key)

    def text(self):
        return self.traditional

    def __init__(self, key: int, traditional: str, simplified: str, pinyin: str, english: str,
                 sentence_traditional: str, sentence_simplified: str, sentence_pinyin: str, sentence_english: str,
                 review_time, **kwargs):
        super(FlashCard, self).__init__(**kwargs)
        self.key = key
        self.traditional = traditional
        self.simplified = simplified
        self.pinyin = pinyin
        self.english = english
        self.sentence_traditional = sentence_traditional
        self.sentence_simplified = sentence_simplified
        self.sentence_pinyin = sentence_pinyin
        self.sentence_english = sentence_english
        self.review_time = review_time
