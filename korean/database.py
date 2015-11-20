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
        self.database = "sqlite:///korean/korean.db"
        debug = True  # TODO change to false of course

        # Connect to database
        engine = create_engine(self.database, echo=debug)
        session_factory = sessionmaker(bind=engine)
        self.session = session_factory()

        # Initialize database if it doesn't exist
        # if not os.path.exists("korean/korean.db"):
        if debug is True:
            # This should automatically create all models
            Base.metadata.create_all(engine)

