#!/usr/bin/python3
""" this is a script that lists all states from the database hbtn_0e_0_usa """
import MySQLdb
from sys import argv

if __name__ == "__main__":
    """ connect to the database"""
    db = MySQLdb.connect(
        user=argv[1],
        passwd=argv[2],
        db=argv[3],
    )

    cursor = db.cursor()
    naame = "SELECT * FROM states WHERE Name = %s ORDER BY id"
    cursor.execute(naame, (argv[4], ))
    result = cursor.fetchall()
    for i in result:
        if i[1] == argv[4]:
            """ loop through the states"""
            print(i)

    """ close the cursor"""
    cursor.close()
    """ close the database"""
    db.close()
