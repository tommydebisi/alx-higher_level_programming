#!/usr/bin/python3
"""
    script that prints the first State
    object from the database hbtn_0e_6_usa
"""
from sys import argv, exit
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from model_state import State


if __name__ == "__main__":
    if len(argv) != 4:
        print('USAGE: {} username password database'.format(argv[0]))
        exit(1)

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(argv[1], argv[2], argv[3]))

    # Start Session
    Session = sessionmaker(bind=engine)
    session = Session()

    # get the first object(row in the table)
    if info := session.query(State).order_by(State.id).first():
        print("{}: {}".format(info.id, info.name))
    else:
        print()

    session.commit()
