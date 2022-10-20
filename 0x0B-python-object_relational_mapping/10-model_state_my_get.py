#!/usr/bin/python3
""" List all State objects whos name match passed in argument in a database """
from model_state import Base, State
from sqlalchemy import (create_engine)
from sys import argv
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    my_url = "mysql+mysqldb://{}:{}@localhost/{}"
    engine = create_engine(my_url.format(argv[1], argv[2], argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    result = session.query(State).filter(State.name == argv[4]).first()

    if result is None:
        print("Not Found")
    else:
        print("{}: {}".format(result.id, result.name))
