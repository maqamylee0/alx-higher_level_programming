#!/usr/bin/python3
"""
script that prints the State object

"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


if __name__ == "__main__":
    if len(sys.argv) != 5:
        sys.exit(1)

    username, password, database, search_item = sys.argv[1:5]

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        username, password, database))

    Session = sessionmaker(bind=engine)
    session = Session()

    state = session.query(State)\
        .filter(State.name.like(search_item))\
        .order_by(State.id).first()
    if state:
        print("{}".format(state.id))
    else:
        print("Not found")

    session.close()
