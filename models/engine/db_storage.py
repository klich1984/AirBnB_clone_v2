#!/usr/bin/python3
"""Database storage"""
import os
from sqlalchemy.orm import sessionmaker, scoped_session, Session
from models.base_model import BaseModel, Base
from sqlalchemy import create_engine
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review
from models.user import User



class DBStorage():
    """class DBStorage"""
    __engine = None
    __session = None

    def __init__(self):
        """Constructor"""
        username = os.getenv('HBNB_MYSQL_USER')
        password = os.getenv('HBNB_MYSQL_PWD')
        host = os.getenv('HBNB_MYSQL_HOST')
        database = os.getenv('HBNB_MYSQL_DB')
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.format(username, password, host, database), pool_pre_ping=True)
        if os.getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """Query on the current database session

        Args:
            cls ([type], optional): [description]. Defaults to None.
        """
        classes = [State, City, User]
        list_all_obj = []
        if cls is None:
            for clas in classes:
                list_all_obj += self.__session.query(clas).all()
        else:
            list_all_obj = self.__session.query(cls).all()

        dic = {}
        for element in list_all_obj:
            name = element.__class__.__name__+ '.' + str(element.id)
            dic[name] = element
        return dic

    def new(self, obj):
        """[summary]

        Args:
            obj ([type]): [description]
        """
        self.__session.add(obj)

    def save(self):
        """[summary]
        """
        self.__session.commit()

    def delete(self, obj=None):
        """[summary]

        Args:
            obj ([type], optional): [description]. Defaults to None.
        """
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """[summary]
        """
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()
