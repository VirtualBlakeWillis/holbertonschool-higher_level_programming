#!/usr/bin/python3
""" create table cities using SQLAlchemy """
from sqlalchemy import Column, String, Integer
from model_state import Base
from sqlalchemy import ForeignKey


class City(Base):
    """ City class """
    __tablename__ = "cites"
    id = Column(Integer(), autoincrement=True, primary_key=True,
                nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)
