#!/usr/bin/python3
import MySQLdb
from sys import argv

args = argv[1:]

db_obj = MySQLdb.connect(user=args[0], passwd=args[1], db=args[2],
                         host="localhost", port=3306)

cur_obj = db_obj.cursor()
cur_obj.execute("SELECT * FROM states \
                WHERE states.name='{}' \
                ORDER BY states.id ASC".format(args[3]))

rows = cur_obj.fetchall()
for row in rows:
    print(row)

cur_obj.close()
db_obj.close()
