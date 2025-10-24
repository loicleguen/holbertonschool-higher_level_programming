#!/usr/bin/python3
"""Script 14-model_city_fetch_by_state.py that prints
all City objects from the database hbtn_0e_14_usa"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City
import sys


if __name__ == "__main__":
    # Create the database engine
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'
        .format(sys.argv[1], sys.argv[2], sys.argv[3])
    )
    # Create a configured "Session" class
    Session = sessionmaker(bind=engine)
    # Create a Session
    session = Session()
    # Query all City objects, joined with State to get state names
    cities = (
        session.query(State, City)
        .join(City, State.id == City.state_id)
        .order_by(City.id)
        .all())
    # Print each City object with its corresponding State name
    for state, city in cities:
        print(f"{state.name}: ({city.id}) {city.name}")
    # Close the session
    session.close()
