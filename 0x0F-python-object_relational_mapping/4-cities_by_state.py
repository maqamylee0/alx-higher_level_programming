#!/usr/bin/python3
""" Usage: ./4-cities_by_state.py <username> <password> <database> """

import sys
import MySQLdb

if __name__ == '__main__':
    try:
        conn = MySQLdb.connect(host="localhost",
                               port=3306,
                               user=sys.argv[1],
                               passwd=sys.argv[2],
                               db=sys.argv[3], charset="utf8")
        cur = conn.cursor()
        cur.execute("SELECT cities.id, cities.name, states.name FROM cities \
                    JOIN states ON cities.state_id == cities.id \
                    ORDER BY cities.id ASC")
        query_rows = cur.fetchall()
        for row in query_rows:
            print(row)
    except MySQLdb.Error as e:
        print(f"Error {e}")
    finally:
        cur.close()
        conn.close()
