#!/usr/bin/python3
"""
    script that lists all states from the database hbtn_0e_0_usa
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
    query = "SELECT cities.id, cities.name, states.name \
            FROM cities JOIN states ON cities.state_id = states.id \
            WHERE states.name = %s ORDER BY cities.id ASC"
    search_state = argv[4]
    cursor.execute(query, (search_state,))
    rows = cursor.fetchall()

    city_names = [row[1] for row in rows]
    formated_city_name = ", ".join(city_names)
    print(formated_city_name)
    cursor.close()
    db.close()
