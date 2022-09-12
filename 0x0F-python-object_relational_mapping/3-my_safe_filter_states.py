#!/usr/bin/python3
"""
    script that takes in an argument and displays all values in the
    states table of hbtn_0e_0_usa where name matches the argument.
    Free from sql injections.
"""
import MySQLdb
from sys import argv

if __name__ == "__main__":
    db_obj = MySQLdb.connect(user=argv[1], passwd=argv[2], db=argv[3],
                             host="localhost", port=3306)

    cur_obj = db_obj.cursor()

    # prevent sql injection by using parameterized sql
    cur_obj.execute("SELECT * FROM states \
                    WHERE states.name=%(name_state)s \
                    ORDER BY states.id ASC", {"name_state": argv[4]})

    rows = cur_obj.fetchall()
    for row in rows:
        print(row)

    cur_obj.close()
    db_obj.close()
