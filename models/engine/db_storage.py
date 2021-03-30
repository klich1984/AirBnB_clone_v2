#!/usr/bin/python3
"""Database storage"""
import os
import models
from sqlalchemy.orm import Session
from models.base_model import BaseModel, Base
from sqlalchemy import *


class DBStorage():
    """class DBStorage"""
    __engine = None
    __session = None

    def __init__(self):
        """Constructor"""
        username = os.getenv('HBNB_MYSQL_USER')
        password = os.getenv('HBNB_MYSQL_PWD')
        host = os.getenv('HBNB_MYSQL_HOST' )
        database = os.getenv('HBNB_MYSQL_DB')
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'
                           .format(username, password, host, database),
                           pool_pre_ping=True)
        if os.getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)
    
    def all(self, cls=None):
        """Query on the current database session

        Args:
            cls ([type], optional): [description]. Defaults to None.
        """
        if cls is None:



