#!/usr/bin/python3
from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, String, Integer
Base = declarative_base()
"""
class State
id int
name str
"""
class State(Base):
    __tablename__ = "states"
    id = Column(Integer(), autoincrement=True, primary_key=True, 
                nullable=False)
    name = Column(String(128), nullable=False)