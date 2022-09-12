#!/usr/bin/python3
"""
    script that lists all states with a name starting with N
    (upper N) from the database hbtn_0e_0_usa
"""
import MySQLdb
from sys import argv


def main():
    """Main function"""
    username = argv[1]
    password = argv[2]
    database = argv[3]

    db = MySQLdb.connect(host="localhost", port=3306, user=username,
                         password=password, db=database)
    cur = db.cursor()
    cur.execute("""SELECT * FROM states WHERE name LIKE
                BINARY 'N%' ORDER BY id""")
    result = cur.fetchall()
    for row in result:
        print(row)

    cur_obj.close()
    db_obj.close()


if __name__ == '__main__':
    main()
