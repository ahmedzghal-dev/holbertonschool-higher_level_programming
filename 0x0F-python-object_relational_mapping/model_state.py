#!/usr/bin/python3
import sqlalchemy
from sqlalchemy.ext.declaritive import declaritive_base
from sqlalchemy import Column, Integer, String

Base = declaritive_base()

Class State(Base):
    """the class state imports Base"""

    __tablename__ = 'states'
    id = Column(
        Integer,
        nullable=False,
        primary_key=True
    )
    name = Column(String(128), nullable=False)
