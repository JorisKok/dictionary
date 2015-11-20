from korean.model.korean import Korean
from korean.model.english import English
from korean.database import Base
from sqlalchemy.orm.session import Session


def init_db(session):
    # session.bind_mapper()
    e = English(word="something")
    session.add(e)
    pass

init_db(Base.session)