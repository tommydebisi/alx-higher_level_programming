#!/usr/bin/python3
from sqlalchemy import create_engine
from sys import argv, exit
from sqlalchemy.orm import sessionmaker
from relationship_state import State
from relationship_city import City

if __name__ == "__main__":
    if len(argv) != 4:
        print('USAGE: {} user passwd database'.format(argv[0]))
        exit(1)

    user = argv[1]
    passwd = argv[2]
    db = argv[3]

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.
                           format(user, passwd, db), pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()

    info = session.query(State) \
        .order_by(State.id).all()

    for state in info:
        print("{}: {}".format(state.id, state.name))

        for city in state.cities:
            print("    {}: {}".format(city.id, city.name))

    session.commit()
