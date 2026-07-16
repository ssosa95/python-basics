import sqlite3
import sys

with sqlite3.connect("C:/Users/user/projects/sqlite-basics/sysadmin_practice.db") as conn:
    cursor = conn.cursor()
    cursor.execute("INSERT INTO users(name, role, active) VALUES(?, ?, ?)", (sys.argv[1], sys.argv[2], int(sys.argv[3])))
    conn.commit()
    print(f"Added user with id {cursor.lastrowid} last.")