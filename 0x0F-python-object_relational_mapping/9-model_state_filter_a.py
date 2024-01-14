#!/usr/bin/python3
"""Start link class to table in database
"""
import sys
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import (create_engine)

if __name__ == "__main__":
    if len(argv) == 4:
        engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                               .format(sys.argv[1], sys.argv[2], sys.argv[3]))
        Session = sessionmaker(bind=engine)
        session = Session()

        states = session.query(State)\
                        .filter(State.name.like('%a%'))\
                        .order_by(State.id)
        for i in states:
            print(f"{state.id}: {state.name}")
        session.close()