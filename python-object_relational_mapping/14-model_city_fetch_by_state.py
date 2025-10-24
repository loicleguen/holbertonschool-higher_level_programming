#!/usr/bin/python3
"""Script that prints all City objects from the database hbtn_0e_14_usa"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City
import sys

if __name__ == "__main__":
    # Check correct number of arguments
    if len(sys.argv) != 4:
        print(
            "Usage: ./14-model_city_fetch_by_state.py <username> "
            "<password> <database>"
        )
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    # Create database engine
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(
            username, password, db_name
        )
    )

    # Create a configured "Session" class
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query all City objects joined with State
    cities = (
        session.query(State, City)
        .join(City, State.id == City.state_id)
        .order_by(City.id)
        .all()
    )

    # Print results
    for state, city in cities:
        print(f"{state.name}: ({city.id}) {city.name}")

    # Close session
    session.close()
