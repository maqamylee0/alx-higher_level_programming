#!/usr/bin/python3

"""Start link class to table in database and fetchall
"""
import sys
from model_state import Base, State
from sqlalchemy.orm import Session

from sqlalchemy import (create_engine)

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    session = Session(engine)
    first_state = session.query(State).filter(State.name.like(sys.argv[4])).order_by(State.id).first()
    if first_state:
        print("{}".format(first_state.id))
    else:
        print("Not Found")

    session.close()
