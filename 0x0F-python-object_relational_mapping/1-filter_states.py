#!/usr/bin/python3
""" Write a script that lists all states with a name
starting with N (upper N) from the database hbtn_0e_0_usa:
"""
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

    cursor = db.cursor()
    cursor.execute(
    result=cursor.fetchall()
    for a in result:
        if a[1][0] == "N":
            print(a)
    cursor.close()
    db.close()
