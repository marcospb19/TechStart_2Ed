from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = 'sqlite:///./app_database.db'

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={'check_same_thread': False}
)

# Class to gather current database session
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Schema base model class
Base = declarative_base()


def init_db():
    """ Initializes the database, TODO: use migrations instead """
    Base.metadata.create_all(bind=engine)


def get_db():
    """ Retrieves the current local session of the database """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
