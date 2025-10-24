#!/usr/bin/python3
"""Define the City class mapped to the cities table"""

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from model_state import Base, State

class City(Base):
    """City class linked to the MySQL table 'cities'"""
    __tablename__ = 'cities'

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)

    # Define relationship to State
    state = relationship("State")
