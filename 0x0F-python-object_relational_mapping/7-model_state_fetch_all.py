#!/usr/bin/python3

import sqlalchemy
from sqlalchemy import create_engine
from model_state import Base, State

from sys import argv

if __name__ == '__main__':
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.
        format(argv[1], argv[2], argv[3]))
    Base.metadata.create_all(engine)
    session = Session(engine)
    states = session.query(State).order_by(State.id.asc()).all()
    print("{}: {}".format(state.id, state.name))
    session.close()
