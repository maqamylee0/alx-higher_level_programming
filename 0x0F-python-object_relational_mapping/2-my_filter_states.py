#!/usr/bin/python3
"""
    Usage: ./2-my_filter_states.py <username>
    <password> <database> <search_term>
"""

import sys
import MySQLdb

if __name__ == '__main__':
    if len(sys.argv == 5):
        try:
            conn = MySQLdb.connect(host="localhost",
                                   port=3306,
                                   user=sys.argv[1],
                                   passwd=sys.argv[2],
                                   db=sys.argv[3], charset="utf8")
            cur = conn.cursor()
            cur.execute(f"SELECT * FROM states \
                        WHERE name LIKE '{sys.argv[4]}' \
                        ORDER BY id ASC")
            query_rows = cur.fetchall()
            for row in query_rows:
                print(row)
        except MySQLdb.Error as e:
            print(f"Error {e}")
        finally:
            cur.close()
            conn.close()
    else:
        sys.exit(1)
