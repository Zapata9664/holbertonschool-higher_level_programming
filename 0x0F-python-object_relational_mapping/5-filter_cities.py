#!/usr/bin/python3
'''Lists all states from the database hbtn_0e_0_usa'''
import sys
import MySQLdb

if __name__ == "__main__":
    conn = MySQLdb.connect(host="localhost", port=3306,
                           user=sys.argv[1], passwd=sys.argv[2],
                           db=sys.argv[3], charset="utf8")
    cur = conn.cursor()
    cur.execute('SELECT cities.name FROM cities \
    JOIN states ON cities.state_id = states.id WHERE states.name LIKE %s \
    ORDER BY cities.id', (sys.argv[4],))
    query_rows = cur.fetchall()
    print(", ".join(city[0] for city in query_rows))
    cur.close()
    conn.close()
