#!/usr/bin/python3
"""Print the first State object from the database hbtn_0e_6_usa"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from model_state import Base, State

if __name__ == "__main__":
    # Ensure correct number of arguments
    if len(sys.argv) != 4:
        print(
            "Usage: ./8-model_state_fetch_first.py <username> "
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

    # Fetch the first State object ordered by id
    first_state = session.query(State).order_by(State.id).first()

    # Print result or 'Nothing' if table is empty
    if first_state:
        print(f"{first_state.id}: {first_state.name}")
    else:
        print("Nothing")

    # Close session
    session.close()
