#!/usr/bin/python3
"""
Lists all states with a name starting with N.
"""

import MySQLdb
import sys


if __name__ == "__main__":
    # Get MySQL credentials and database name from command-line arguments
    username, password, database, state_name = sys.argv[1],
    sys.argv[2], sys.argv[3], sys.argv[4]

    # Connect to the MySQL server
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database,
        charset="utf8"
    )

    # Create a cursor object to interact with the database
    cur = db.cursor()

    # Execute the SQL query
    cur.execute(
        "SELECT * FROM states WHERE BINARY name = '{}' ORDER "
        "BY id ASC".format(state_name))

    # Fetch and display all results
    for row in cur.fetchall():
        print(row)

    # Close cursor and database connection
    cur.close()
    db.close()
