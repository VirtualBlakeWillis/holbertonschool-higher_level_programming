#!/usr/bin/python3
""" Script that prints all values in table states with name = arg4 """
import MySQLdb
from sys import argv


if __name__ == "__main__":
    """ code for script """
    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3])
    cur = db.cursor()
    query = "SELECT * FROM states WHERE name = '{}' \
             ORDER BY id ASC".format(argv[4])
    cur.execute(query)
    rows = cur.fetchall()

    for row in rows:
        print("{}".format(row))
