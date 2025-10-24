#!/usr/bin/python3
"""Update the name of the State object with id = 2 to 'New Mexico'"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from model_state import Base, State

if __name__ == "__main__":
    # Ensure correct number of arguments
    if len(sys.argv) != 4:
        print(
            "Usage: ./12-model_state_update_id_2.py <username> "
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

    # Fetch the State with id = 2
    state = session.query(State).filter(State.id == 2).first()

    # Update the name if the state exists
    if state:
        state.name = "New Mexico"
        session.commit()

    # Close session
    session.close()
