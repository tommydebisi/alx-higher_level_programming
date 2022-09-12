#!/usr/bin/python3

import MySQLdb
from sys import argv

if __name__ == "__main__":
    # connecting and getting db object
    db_obj = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                            passwd=argv[2], db=argv[3])

    # get the cursor
    cur = db_obj.cursor()

    # perform sql queries with execute
    cur.execute("SELECT * FROM states \
                ORDER BY states.id ASC;")
    rows = cur.fetchall()
    for tup in rows:
        print(tup)

    # close cursor and db obj after use
    cur.close()
    db_obj.close()
