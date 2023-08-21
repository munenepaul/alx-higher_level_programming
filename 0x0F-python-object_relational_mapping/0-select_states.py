#!/usr/bin/python3
"""
python script that lists all states from the database hbtn_0e_0_usa
"""

import MySQLdb
import sys

def list_states(mysql_username, mysql_password, database_name):
    try:
        # Connect to the MySQL server
        db = MySQLdb.connect(host="localhost", port=3306,
                user=mysql_username, passwd=mysql_password, db=database_name)
        cursor = db.cursor()

        # Execute the query to fetch states and sort by states.id
        query = "SELECT * FROM states ORDER BY states.id ASC;"
        cursor.execute(query)

        # Fetch all rows from the result
        rows = cursor.fetchall()

        # Print the list of states
        for row in rows:
            print(row)

    except MySQLdb.Error as e:
        print("MySQL Error: {}".format(e))
    finally:
        # Close the database connection
        if db:
            db.close()

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python script.py <mysql_username>
        <mysql_password> <database_name>")
        sys.exit(1)

    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]

    list_states(mysql_username, mysql_password, database_name)
