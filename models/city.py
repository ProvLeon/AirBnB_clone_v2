#!/usr/bin/python3
""" City Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
import os


storage_type = os.environ.get("HBNB_TYPE_STORAGE")


class City(BaseModel):
    """ The city class contains the state ID and state name """
    __tablename__ = "cities"
    if storage_type == "db":
        name = Column(String(128), nullable=False)
        state_id = Column(String(60), ForeignKey("states.id"), nullable=False)
        places = relationship("Place", backref="cities",
                              cascade="all, delete, delete-orphan")
    else:
        state_id = ""
        name = ""
