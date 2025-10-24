#!/usr/bin/python3
"""List all City objects from the database hbtn_0e_14_usa"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from model_state import Base, State
from model_city import City

if __name__ == "__main__":
    # Ensure correct number of arguments
    if len(sys.argv) != 4:
        print(
            "Usage: ./14-model_city_fetch_by_state.py <username> "
            "<password> <database>"
        )
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    # Create engine
    engine = create_engine(
        f'mysql+mysqldb://{username}:{password}@localhost/{db_name}',
        pool_pre_ping=True
    )

    # Create session
    session = Session(engine)

    # Query all cities joined with states, ordered by city id
    cities = session.query(City).join(State).order_by(City.id).all()

    # Print results
    for city in cities:
        print(f"{city.state.name}: ({city.id}) {city.name}")

    # Close session
    session.close()
