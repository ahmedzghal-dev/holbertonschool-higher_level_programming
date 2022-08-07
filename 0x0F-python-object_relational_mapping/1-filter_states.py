#!/usr/bin/python3
"""this  a script that lists all states with a name starting with N (upper N) from the database hbtn_0e_0_usa"""
import MySQLdb
from sys import argv

if __name__ == "__main__":
    """connect to database"""
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=argv[1],
        passwd=argv[2],
        db=argv[3]
    )

    cursor = db.cursor()
    cursor.execute(
        "SELECT * FROM states WHERE name LIKE BINARY 'N%'ORDER BY id ASC")
    result = cursor.fetchall()
    for a in result:
    print(a)

    """ close the cursor""" 
    cursor.close()
    """ close the database"""
    db.close()
