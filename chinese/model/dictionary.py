from sqlalchemy import Column, Integer, String
from korean.database import Base


class DictionaryModel(Base):

    __tablename__ = "dict"

    id = Column(Integer, primary_key=True)
    traditional = Column(String)
    simplified = Column(String)
    pinyin = Column(String)
    english = Column(String)

    def __init__(self, traditional, simplified, pinyin, english):
        self.traditional = traditional
        self.simplified = simplified
        self.pinyin = pinyin
        self.english = english

    def __repr__(self):
        return "<Record('%s, %s, %s, %s')>" % \
               (self.traditional,
                self.simplified,
                self.pinyin,
                self.english)
