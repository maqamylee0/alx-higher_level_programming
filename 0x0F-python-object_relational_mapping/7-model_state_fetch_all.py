#!/usr/bin/python3
"""
script that lists all State objects from the database
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

    states = session.query(State).order_by(State.id).all()
    for state in states:
        print("{}: {}".format(state.id, state.name))

    session.close()
