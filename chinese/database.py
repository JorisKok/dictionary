import regex
import sqlite3
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from korean.singleton import Singleton

# The models need this as a base
Base = declarative_base()


class Database(metaclass=Singleton):

    database = None
    session = None

    def __init__(self):
        # Database connection
        self.database = "sqlite:///chinese.sqlite"
        debug = False  # TODO change to false of course

        # Create the REGEXP function
        # conn = sqlite3.connect(self.database)
        # conn.create_function("REGEXP", 2, self.regex_function)
        # conn.close()

        # Connect to database
        engine = create_engine(self.database, echo=debug)
        session_factory = sessionmaker(bind=engine)
        self.session = session_factory()

        # Initialize database if it doesn't exist
        # if not os.path.exists("korean/korean.db"):
        if debug is True:
            # This should automatically create all models
            Base.metadata.create_all(engine)

    def regex_function(expr, item):
        reg = regex.compile(expr, regex.I)
        return reg.search(item) is not None
