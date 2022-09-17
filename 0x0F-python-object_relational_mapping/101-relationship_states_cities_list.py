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

    info = session.query(State, City).filter(State.id == City.state_id) \
        .order_by(State.id, City.id).all()
    state_name = ""
    for state, city in info:
        if state.name != state_name:
            print("{}: {}".format(state.id, state.name))
            state_name = state.name

        print("    {}: {}".format(city.id, city.name))

    session.commit()
