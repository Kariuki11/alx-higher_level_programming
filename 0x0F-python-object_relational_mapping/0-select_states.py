#!/usr/bin/python3
import MySQLdb
import sys

if__name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

# Connect to MySQL server
    db = MySQLdb.connect(host="localhost", port=3306, user=username, passwd=password, db=database)

    # Create a cursor object using cursor() method
    cursor = db.cursor()

    # Execute SQL query
    cursor.execute("SELECT * FROM states ORDER BY id ASC")

    # Fetch all the rows in a list of lists
    results = cursor.fetchall()

    # Print results
    for row in results:
        print(row)

    # Disconnect from server
    db.close()
