#!/usr/bin/python3
"""
Defines the State class and creates a Base instance for SQLAlchemy ORM.
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

# Base class for all ORM models
Base = declarative_base()


class State(Base):
    """
    State class that represents the 'states' table in MySQL.
    """
    __tablename__ = 'states'  # Table name in MySQL

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
