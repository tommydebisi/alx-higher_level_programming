#!/usr/bin/python3

import MySQLdb
from sys import argv

db_obj = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3])

cur_obj = db_obj.cursor()
cur_obj.execute("SELECT * FROM states \
                WHERE states.name LIKE 'N%' \
                ORDER BY states.id ASC")

rows = cur_obj.fetchall()

for row in rows:
    print(row)

cur_obj.close()
db_obj.close()
