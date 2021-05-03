#!/usr/bin/python3
""" State Module for HBNB project """
import os
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'

    if os.getenv('HBNB_TYPE_STORAGE') == 'db':
        name = Column(String(128), nullable=False)
        cities = relationship('City', cascade="all, delete", backref="states")
        # Se necesita cities?
    else:
        @property
        def cities(self):
            list_cities = []
            for city in storage.all(City):
                # print("Una cosa mas llamativa y puros asteriscos si quiere = ", i)
                if city.state_id == self.id:
                    list_cities.append(city)
            return list_cities
        name = ""

