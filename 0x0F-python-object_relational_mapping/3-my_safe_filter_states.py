#!/usr/bin/python3
"""
    Usage: ./3-my_safe_filter_states.py <username>
    <password> <database> <search term>
"""

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
        cur.execute("SELECT * FROM states WHERE \
                name LIKE %s \
                ORDER BY id ASC", (sys.argv[4],))
        query_rows = cur.fetchall()
        for row in query_rows:
            print(row)
    except MySQLdb.Error as e:
        print(f"Error {e}")
    finally:
        cur.close()
        conn.close()
