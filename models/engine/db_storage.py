#!/usr/bin/python3
"""DBStorage module for HBNB project"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import Base
import os


class DBStorage:
    """This class manages the database storage for the HBNB project"""
    __engine = None
    __session = None

    def __init__(self):
        """Initializes an instance of DBStorage"""
        user = os.environ.get('HBNB_MYSQL_USER')
        password = os.environ.get('HBNB_MYSQL_PWD')
        host = os.environ.get('HBNB_MYSQL_HOST', 'localhost')
        database = os.environ.get('HBNB_MYSQL_DB')

        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.
                                      format(user, password, host, database),
                                      pool_pre_ping=True)

        if os.environ.get('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """Query on the current database session (self.__session) all objects
        depending on the class name (argument cls).
        """
        from models import storage

        objects = {}
        if cls is None:
            for class_name in storage.classes:
                objects.update(storage.all(class_name))
        else:
            objects = storage.all(cls)
        return objects

    def new(self, obj):
        """Add the object to the current database session (self.__session)."""
        self.__session.add(obj)

    def save(self):
        """Commit all changes of the current database session (self.__session)."""
        self.__session.commit()

    def delete(self, obj=None):
        """Delete from the current database session obj if not None."""
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """Create all tables in the database (feature of SQLAlchemy).
        Create the current database session (self.__session) from the engine (self.__engine)
        by using a sessionmaker.
        """
        Base.metadata.create_all(self.__engine)
        Session = scoped_session(sessionmaker(bind=self.__engine,
                                              expire_on_commit=False))
        self.__session = Session()

    def close(self):
        """Close the session."""
        self.__session.remove()
