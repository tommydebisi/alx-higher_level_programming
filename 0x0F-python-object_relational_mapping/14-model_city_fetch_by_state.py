#!/usr/bin/python3
"""
    This script prints all City objects from the database hbtn_0e_14_usa
"""
from sys import argv, exit
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from model_state import State
from model_city import City


if __name__ == "__main__":
    if len(argv) != 4:
        print('USAGE: {} username password database'.format(argv[0]))

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(argv[1], argv[2], argv[3]))

    Session = sessionmaker(bind=engine)
    session = Session()

    # use of join, it automatically joins mapped classes with foreign keys
    states_and_cities = session.query(
        State, City
        ).filter(State.id == City.state_id).all()

    for state, city in states_and_cities:
        print("{}: ({}) {}".format(state.name, city.id, city.name))

    session.commit()
