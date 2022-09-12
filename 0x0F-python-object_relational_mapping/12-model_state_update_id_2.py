#!/usr/bin/python3
"""
    script that changes the name of a State object
    from the database hbtn_0e_6_usa
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

    # get object to be updated
    info = session.query(State).filter(State.id == 2).first()

    # now modify the name
    info.name = 'New Mexico'

    session.commit()
