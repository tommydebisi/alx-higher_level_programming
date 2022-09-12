#!/usr/bin/python3
"""
    script that lists all State objects from
    the database hbtn_0e_6_usa
"""
from sys import argv, exit
from model_state import State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    if len(argv) != 4:
        print('The format: mysql_username mysql_password database_name')
        exit(1)

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(argv[1], argv[2], argv[3]))

    # Getting mapped elements, get session object
    Session = sessionmaker(bind=engine)
    session = Session()

    info = session.query(State).order_by(State.id).all()

    for instance in info:
        print('{}: {}'.format(instance.id, instance.name))

    # commits the transactions so far
    session.commit()
