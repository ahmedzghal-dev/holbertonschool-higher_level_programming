#!/usr/bin/python3
""" Write a script that lists all states from
the database hbtn_0e_4_usa """
import MySQLdb
from sys import argv

if __name__ == "__main__":
    """ connect to the database"""
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=argv[1],
        passwd=argv[2],
        db=argv[3],
    )

    cities = []
    cursor = db.cursor()
    lists = """SELECT cities.id, cities.name, states.name
        FROM cities INNER JOIN states ON cities.state_id = states.id
        WHERE states.name=%s
        ORDER BY id"""
    cursor.execute(lists, (argv[4], ))
    results = cursor.fetchall()
    for city in results:
        cities.append(city[1])
    print(', '.join(cities))
    cursor.close()
    db.close()
