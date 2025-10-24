#!/usr/bin/python3
"""
Defines the City class mapped to the `cities` table using SQLAlchemy ORM.

This module requires the `Base` class from `model_state` and creates a City
class with attributes corresponding to table columns.
"""
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from model_state import Base


class City(Base):
    """City model for the `cities` table in the MySQL database.

    This class represents a city and is mapped to the `cities` table
    using SQLAlchemy ORM. It includes an auto-incremented ID, a name,
    and a foreign key reference to the `states` table.

    Attributes:
        id (int): Primary key. Auto-generated, unique, non-nullable.
        name (str): Name of the city. Max length 128 characters. Non-nullable.
        state_id (int): Foreign key referencing `states.id`. Non-nullable.
    """
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)

    state = relationship("State")
