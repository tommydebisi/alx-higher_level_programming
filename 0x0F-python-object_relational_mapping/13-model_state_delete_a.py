#!/usr/bin/python3
"""
    deletes all State objects with a name containing the
    letter a from the database hbtn_0e_6_usa
"""
from sys import argv, exit
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from model_state import State


if __name__ == "__main__":
    if len(argv) != 4:
        print('USAGE: {} username password database'.format(argv[0]))

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(argv[1], argv[2], argv[3]))

    Session = sessionmaker(bind=engine)
    session = Session()

    # filter with sql regex
    info = session.query(State).filter(State.name.like('%a%')) \
        .order_by(State.id)

    for obj in info:
        session.delete(obj)

    session.commit()
