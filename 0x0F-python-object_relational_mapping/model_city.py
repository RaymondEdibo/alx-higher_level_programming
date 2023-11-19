#!/usr/bin/python3
"""City module.

Contains City class from Base = declarative_base()
"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.sql.schema import ForeignKey
from model_state import Base


class City(Base):
    """links to `cities` table of database.

    Attributes:
        id (int): id of the city.
        name (str): name of the city.
        state_id (int): id of the associated state.
    """

    __tablename__ = 'cities'

    id = Column(Integer, autoincrement=True, nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
