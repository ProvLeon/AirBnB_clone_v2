#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel


class State(BaseModel):
    """ State class """
    __tablename__ = "states"
    name = Column("name", String(128), nullable=False)

    cities = relationship('City', backref='state',
                          cascade='all, delete-orphan')


@property
def cities(self):
    """getter attributes for cities in FileStorage"""
    from models import storage
    city_instances = storage.all('City')
    return [city for city in city_instances.values()
            if city.state_id == self.id]
