#!/usr/bin/python3
"""
 script that changes the name of a State object from the database
"""


from sqlalchemy.orm import Session
from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine, update

if __name__ == "__main__":
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(argv[1], argv[2], argv[3]))
    Base.metadata.create_all(engine)

    session = Session(engine)
    stmt = (
    update(State).
    where(id == 2).
    values(name='New Mexico')
)
    session.add(stmt)
    session.commit()
    print(stmt.id)
    session.close()
