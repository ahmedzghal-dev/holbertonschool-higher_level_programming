#!/usr/bin/python3
"""
a script that lists all State objects that contain
the letter a from the database
"""


from sqlalchemy.orm import Session
import sqlalchemy
from sys import argv
from model_state import Base, State
from sqlalchemy import (create_engine)
if __name__ == "__main__":
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(argv[1], argv[2], argv[3]))
    Base.metadata.create_all(engine)
    session = Session(engine)
    states = session.query(State).all()

    for i in states:
        if 'a' in i.name:
            print("{}: {}".format(i.id, i.name))
    session.close()
