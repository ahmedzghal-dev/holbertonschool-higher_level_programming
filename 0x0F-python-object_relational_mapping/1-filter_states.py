#!/usr/bin/python3
""" write  a script that lists all states from
from the database hbtn_0e_0_usa"""
import MySQLdb
from sys import argv

if __name__ == "__main__":
    """ connect to the database"""
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=argv[1],
        passwd=argv[2],
        db=argv[3]
    )

cursor = db.cursor()
cursor.execute(
    "SELECT * FROM states WHERE name LIKE BINARY 'N%'ORDER BY id")
result = cursor.fetchall()
for a in result:
    """ loop through the states"""
    print(a)
""" close the cursor"""
cursor.close()
""" close the database"""
db.close()
