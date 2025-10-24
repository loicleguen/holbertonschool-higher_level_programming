#!/usr/bin/python3
"""List all State objects that contain the letter 'a' from the database"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from model_state import Base, State

if __name__ == "__main__":
    # Ensure correct number of arguments
    if len(sys.argv) != 4:
        print(
            "Usage: ./9-model_state_filter_a.py <username> "
            "<password> <database>"
        )
        sys.exit(1)

    username, password, db_name = sys.argv[1], sys.argv[2], sys.argv[3]

    # Create engine to connect to MySQL
    engine = create_engine(
        f'mysql+mysqldb://{username}:{password}@localhost/{db_name}',
        pool_pre_ping=True
    )

    # Create a session
    session = Session(engine)

    # Query all State objects containing 'a' in the name, ordered by id
    states = session.query(State).filter(
        State.name.like('%a%')).order_by(State.id).all()

    # Print results
    for state in states:
        print(f"{state.id}: {state.name}")

    # Close session
    session.close()
