#!/usr/bin/python3
"""
 a script that prints the State object with the name passed
 as argument from the database
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
    states = session.query(State).filter(State.name == argv[4]).first()
    if states is None:
        print("Not found")
    else:
        print("{}".format(states.id))
    session.close()
