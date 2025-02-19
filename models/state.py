#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from models import storage
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'

    name = Column(String(128), nullable=False)

    # For DBStorage
    if type(storage).__name__ == 'DBStorage':  # Check storage type
        cities = relationship('City', backref='state', cascade='all, delete-orphan')
    # For FileStorage
    else:
        @property
        def cities(self):
            """Getter attribute that returns the list of City instances
            with state_id equals to the current State.id"""
            city_list = []
            for city in storage.all('City').values():
                if city.state_id == self.id:
                    city_list.append(city)
            return city_list
