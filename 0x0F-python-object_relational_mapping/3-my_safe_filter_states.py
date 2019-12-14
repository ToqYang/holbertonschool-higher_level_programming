#!/usr/bin/python3
""" Import the sys.arg """
import MySQLdb
import sys

if __name__ == "__main__":
    # Initializes method connect to the database
    db = MySQLdb.connect(host="localhost",
                         port=3306,
                         user=sys.argv[1],
                         passwd=sys.argv[2],
                         db=sys.argv[3])
    # Return the cursor
    cursor = db.cursor()
    # Execute the query and return to the cursor also prevent sql inj
    cursor.execute("SELECT * FROM states\
    WHERE name LIKE %s ORDER BY id ASC;", (sys.argv[4],))
    # Store the column of the tables
    tables = cursor.fetchall()
    # Print the column of the tables
    for column in tables:
        print(column)

    cursor.close()
    db.close()
