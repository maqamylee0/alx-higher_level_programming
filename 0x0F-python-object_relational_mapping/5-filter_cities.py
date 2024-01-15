#!/usr/bin/python3
""" Usage: ./5-filter_cities.py <username> <password> <database> <city> """

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
        cur.execute("SELECT * FROM cities JOIN states\
                ON cities.state_id = states.id \
                WHERE states.name LIKE %s \
                ORDER BY cities.id ASC", (sys.argv[4],))
        query_rows = cur.fetchall()
        cities = [city[1] for city in query_rows]
        city_list = ", ".join(cities)
        print(city_list)
    except MySQLdb.Error as e:
        print(f"Error {e}")
    finally:
        cur.close()
        conn.close()
