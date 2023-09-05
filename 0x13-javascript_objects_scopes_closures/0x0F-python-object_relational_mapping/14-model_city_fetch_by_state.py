#!/usr/bin/python3
"""
script to print all City objects from the database hbtn_0e_14_usa.
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_city import Base, City
from model_state import State

if __name__ == "__main__":
    if len(sys.argv) != 4:
        sys.exit(1)

    username, password, database = sys.argv[1:4]

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        username, password, database))

    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    cities = session.query(City, State)\
                    .filter(City.state_id == State.id)\
                    .order_by(City.id).all()

    for city, state in cities:
        print("{}: ({}) {}".format(state.name, city.id, city.name))

    session.close()
