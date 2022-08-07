#!/usr/bin/python3
""" Write a script that lists all states from the database hbtn_0e_4_usa """
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
        "SELECT cities.id, cities.name, states.name FROM cities" +
        " INNER JOIN states ON cities.state_id = states.id ORDER BY " +
        "cities.id ")
    """ only select cities id  and then cities name and states names"""
    result = cursor.fetchall()
    for i in result:
        """ loop through the states"""
        print(i)
    cursor.close()
    """ close the cursor"""
    db.close()
    """ close the database"""