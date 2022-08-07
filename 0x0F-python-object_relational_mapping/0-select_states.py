#!/usr/bin/python3
"""this a script that lists all states from the database hbtn_0e_0_usa"""
import MySQLdb
from sys import argv

if __name__ == "__main__":

    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=argv[1],
        passwd=argv[2],
        db=argv[3]
    )
# Start cursor
cursor = db.cursor()
# Query
cursor.execute("SELECT * from states ORDER BY id ASC")
result = cursor.fetchall()
# Print query
for a in result:
    print(a)

# Close cursor & database
cursor.close()
db.close()
