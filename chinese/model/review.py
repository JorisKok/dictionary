from sqlalchemy import Column, Integer, String
from korean.database import Base


class ReviewModel(Base):

    __tablename__ = "review"

    id = Column(Integer, primary_key=True)
    traditional = Column(String)
    simplified = Column(String)
    pinyin = Column(String)
    english = Column(String)
    sentence_traditional = Column(String)
    sentence_simplified = Column(String)
    sentence_pinyin = Column(String)
    sentence_english = Column(String)
    review_time = Column(String)

    def __init__(self, traditional, simplified, pinyin, english, sentence_traditional, sentence_simplified, sentence_pinyin, sentence_english, review_time):
        self.traditional = traditional
        self.simplified = simplified
        self.pinyin = pinyin
        self.english = english
        self.sentence_traditional = sentence_traditional
        self.sentence_simplified = sentence_simplified
        self.sentence_pinyin = sentence_pinyin
        self.sentence_english = sentence_english
        self.review_time = review_time

    def __repr__(self):
        return "<Record('%s, %s, %s, %s, %s, %s, %s, %s, %s')>" % \
               (self.traditional,
                self.simplified,
                self.pinyin,
                self.english,
                self.sentence_traditional,
                self.sentence_simplified,
                self.sentence_pinyin,
                self.sentence_english,
                self.review_time,
                )
