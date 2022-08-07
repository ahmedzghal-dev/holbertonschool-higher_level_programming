#!/usr/bin/python3
""" write a script that lists all states from
the database hbtn_0e_0_usa """
import MySQLdb
from sys import argv

if __name__ == "__main__":
    """connect to database"""
    db = MySQLdb.connect(
        user=argv[1],
        passwd=argv[2],
        db=argv[3]
    )

cursor = db.cursor()
cursor.execute(("SELECT * FROM states".format(argv[4])))
result = cursor.fetchall()
for a in result:
    if a[1] == argv[4]:
        """ loop through the states"""
        print(a)
""" close the cursor"""
cursor.close()
""" close the database"""
db.close()
