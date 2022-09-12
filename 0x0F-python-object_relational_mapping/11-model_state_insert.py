#!/usr/bin/python3
"""
    script that adds the State object “Louisiana”
    to the database hbtn_0e_6_usa
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

    # adding row to the table
    session.add(State(name="Louisiana"))
    info = session.query(State).filter(State.name == "Louisiana").first()

    print(info.id)

    session.commit()
