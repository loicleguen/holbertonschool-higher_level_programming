#!/usr/bin/python3
"""Delete all State objects with a name containing the letter 'a'"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from model_state import Base, State

if __name__ == "__main__":
    # Ensure correct number of arguments
    if len(sys.argv) != 4:
        print(
            "Usage: ./13-model_state_delete_a.py <username> "
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

    # Query all State objects containing 'a' in the name
    states_to_delete = session.query(State).filter(
        State.name.like('%a%')
    ).all()

    # Delete each state found
    for state in states_to_delete:
        session.delete(state)

    # Commit the session to apply changes
    session.commit()

    # Close session
    session.close()
