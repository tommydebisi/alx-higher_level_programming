#!/usr/bin/python3
import MySQLdb
from sys import argv

if __name__ == "__main__":
    db_obj = MySQLdb.connect(user=argv[1], passwd=argv[2], db=argv[3],
                            host="localhost", port=3306)

    cursor = db_obj.cursor()
    cursor.execute(
        "SELECT cities.name \
        FROM cities \
        LEFT JOIN states ON cities.state_id=states.id \
        WHERE states.name=%(name_of_state)s\
        ORDER BY cities.id ASC",
        {"name_of_state": argv[4]}
    )

    rows = cursor.fetchall()
    separate = ""
    for row in rows:
        print(separate, end='')
        print(row[0], end='')
        separate = ", "
    print()

    cursor.close()
    db_obj.close()
