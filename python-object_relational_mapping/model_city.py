#!/usr/bin/python3
"""module that contains the class definition of a City"""
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

# Create the base class for the class definitions
Base = declarative_base()


class City(Base):
    """City class mapped to 'cities' table"""
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('state.id'), nullable=False)