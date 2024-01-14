#!/usr/bin/python3
"""Start link class to table in database
"""
import sys
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import (create_engine)

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))
    Session = sessionmaker(bind=engine)
    session = Session()

    state = session.query(State)\
                    .filter(State.name.like(f"{sys.argv[4]}"))\
                    .order_by(State.id).first()
    if state:
        print(f"{state.id}")
    else:
        print("Not Found")
    session.close()
