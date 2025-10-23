#!/usr/bin/python3
"""
Displays all values in the states table where name matches the argument.
"""

import MySQLdb
import sys


if __name__ == "__main__":
    # Get MySQL credentials and database name from command-line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

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
    query = """
        SELECT cities.name
        FROM cities
        JOIN states ON cities.state_id = states.id
        WHERE states.name = %s
        ORDER BY cities.id ASC
    """
    cur.execute(query, (state_name,))

    # Fetch results and print as comma-separated string
    cities = [row[0] for row in cur.fetchall()]
    print(", ".join(cities))

    # Close cursor and database connection
    cur.close()
    db.close()
