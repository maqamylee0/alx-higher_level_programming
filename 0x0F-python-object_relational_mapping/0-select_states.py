#!/usr/bin/python3
""" Usage: ./0-select_states.py <username> <password> <database> """

import sys
import MySQLdb

if __name__ == "__main__":
    if len(sys.argv) == 4:
        try:
            conn = MySQLdb.connect(host="localhost",
                                   port=3306,
                                   user=sys.argv[1],
                                   passwd=sys.argv[2],
                                   db=sys.argv[3])
            cur = conn.cursor()
            cur.execute("SELECT * FROM states ORDER BY id ASC")
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
