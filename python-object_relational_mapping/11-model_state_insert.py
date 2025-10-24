#!/usr/bin/python3
"""Add the State object 'Louisiana' to the database hbtn_0e_6_usa"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from model_state import Base, State

if __name__ == "__main__":
    # Ensure correct number of arguments
    if len(sys.argv) != 4:
        print(
            "Usage: ./11-model_state_insert.py <username> "
            "<password> <database>"
        )
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    # Create engine to connect to MySQL
    engine = create_engine(
        f'mysql+mysqldb://{username}:{password}@localhost/{db_name}',
        pool_pre_ping=True
    )

    # Create a session
    session = Session(engine)

    # Create a new State object
    new_state = State(name="Louisiana")

    # Add and commit the new state to the database
    session.add(new_state)
    session.commit()

    # Print the new state's id
    print(new_state.id)

    # Close session
    session.close()
