#!/usr/bin/python3
""" Write a script that lists all states
from the database hbtn_0e_0_usa """
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
    cursor.execute("SELECT * FROM states ORDER BY id")
    result = cursor.fetchall()
    for x in result:
        """ this is a loop through the states"""
        print(x)
    cursor.close()
    """ close the cursor"""
    db.close()
    """ close the database"""
