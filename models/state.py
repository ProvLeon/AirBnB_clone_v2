#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
import os

class State(BaseModel):
    """ State class """
    __tablename__ = "states"
    if storage_type == "db":
        name = Column("name", String(128), nullable=False)
        cities = relationship('City', backref="state", cascade="all, delete")

    else:
        name = ""
