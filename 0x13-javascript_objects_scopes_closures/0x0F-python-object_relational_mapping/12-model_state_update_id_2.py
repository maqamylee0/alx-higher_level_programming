#!/usr/bin/python3
"""
script to add the State object “Loisiana” to the database
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


if __name__ == "__main__":
    if len(sys.argv) != 4:
        sys.exit(1)

    username, password, database = sys.argv[1:4]

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        username, password, database))

    Session = sessionmaker(bind=engine)
    session = Session()

    state_to_change = session.query(State).filter(State.id == 2).first()

    if state_to_change:
        state_to_change.name = "New Mexico"
        session.commit()

    session.close()
