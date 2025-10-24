#!/usr/bin/python3
"""Print the State object with the name passed as argument"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from model_state import Base, State

if __name__ == "__main__":
    # Ensure correct number of arguments
    if len(sys.argv) != 5:
        print(
            "Usage: ./10-model_state_my_get.py <username> "
            "<password> <database> <state_name>"
        )
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    state_name = sys.argv[4]

    # Create engine to connect to MySQL
    engine = create_engine(
        f'mysql+mysqldb://{username}:{password}@localhost/{db_name}',
        pool_pre_ping=True
    )

    # Create a session
    session = Session(engine)

    # Fetch the first State object with the given name (SQL injection safe)
    state = session.query(State).filter(State.name == state_name).first()

    # Print result or 'Not found'
    if state:
        print(state.id)
    else:
        print("Not found")

    # Close session
    session.close()
