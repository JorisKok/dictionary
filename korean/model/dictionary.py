from sqlalchemy import Column, Integer, String
from korean.database import Base


class Dictionary(Base):

    __tablename__ = "Koendict_tok"

    id = Column(Integer, primary_key=True)
    korean = Column(String, nullable=False)
    english = Column(String)
    root = Column(String)

    def __init__(self, korean, english=None, root=None):
        self.korean = korean
        self.english = english
        self.root = root

    def __repr__(self):
        return "<Record('%s, %s, root: %s')>" % (self.korean, self.english, self.root)
