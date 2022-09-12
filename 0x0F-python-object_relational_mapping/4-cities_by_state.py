#!/usr/bin/python3
import MySQLdb
from sys import argv

db_obj = MySQLdb.connect(user=argv[1], passwd=argv[2], db=argv[3],
                         host="localhost", port=3306)

cursor = db_obj.cursor()
cursor.execute(
    "SELECT cities.id, cities.name, states.name \
    FROM cities \
    LEFT JOIN states ON cities.state_id=states.id \
    ORDER BY cities.id ASC"
)

rows = cursor.fetchall()
for row in rows:
    print(row)

cursor.close()
db_obj.close()
