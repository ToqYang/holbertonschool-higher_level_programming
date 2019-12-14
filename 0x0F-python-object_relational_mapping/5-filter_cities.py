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
    cursor.execute("SELECT cities.name FROM cities LEFT JOIN states\
    ON states.id = cities.state_id WHERE states.name = %s\
    ORDER BY cities.id ASC;", (sys.argv[4],))

    # Store the column of the tables
    tables = cursor.fetchall()
    # Print the column of the tables
    lista = []
    for element in tables:
        lista.append(element[0])
    result = ", ".join(lista)
    print(result)

    cursor.close()
    db.close()
