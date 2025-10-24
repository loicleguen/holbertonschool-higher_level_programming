#!/usr/bin/python3
"""
Script that prints all City objects from the database `hbtn_0e_14_usa`.

Usage:
    ./14-model_city_fetch_by_state.py <username> <password> <database>

The script:
- Connects to a MySQL server on localhost.
- Joins City and State tables using SQLAlchemy ORM.
- Displays cities sorted by city.id in the format: <state name>:
(<city id>) <city name>
"""
import sys

from model_state import Base, State
from model_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(
            sys.argv[1],
            sys.argv[2],
            sys.argv[3]
        ),
        pool_pre_ping=True
    )
    Base.metadata.create_all(engine)  # type: ignore

    Session = sessionmaker(bind=engine)
    session = Session()

    cities = session.query(City).order_by(City.id).all()  # type: ignore

    for city in cities:
        print(f"{city.state.name}: ({city.id}) {city.name}")

    session.close()
