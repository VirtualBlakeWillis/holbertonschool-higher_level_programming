#!/usr/bin/python3
""" create table cities using SQLAlchemy """
from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import declarative_base
from sqlalchemy import ForeignKey

Base = declarative_base()


class City(Base):
    """ City class """
    __tablename__ = "cites"
    id = Column(Integer(), autoincrement=True, primary_key=True,
                nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)
