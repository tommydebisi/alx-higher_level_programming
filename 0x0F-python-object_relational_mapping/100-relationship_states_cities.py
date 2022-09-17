#!/usr/bin/python3
"""
    This script creates the State “California” with the City “San Francisco”
    from the database hbtn_0e_100_usa
"""
from sys import argv, exit
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from relationship_city import City
from relationship_state import State, Base

if __name__ == "__main__":
    if len(argv) != 4:
        print('USAGE: {} user passwd database'.format(argv[0]))
        exit(1)

    user = argv[1]
    passwd = argv[2]
    db = argv[3]

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.
                           format(user, passwd, db), pool_pre_ping=True)

    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    state_obj = State(name="California")
    city_obj = City(name="San Francisco")
    state_obj.cities.append(city_obj)

    session.add_all([state_obj, city_obj])
    session.commit()
