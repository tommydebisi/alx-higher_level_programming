#!/usr/bin/python3
"""
    script that prints the State object with the name
    passed as argument from the database hbtn_0e_6_usa
"""
from sys import argv, exit
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from model_state import State


if __name__ == "__main__":
    if len(argv) != 5:
        print('USAGE: {} username password database'.format(argv[0]))
        exit(1)

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(argv[1], argv[2], argv[3]))

    Session = sessionmaker(bind=engine)
    session = Session()

    info = session.query(State).filter(State.name == argv[4]).first()

    if info:
        print(info.id)
    else:
        print('Not found')

    session.commit()
