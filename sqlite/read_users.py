import sqlite3

with sqlite3.connect("C:/Users/user/projects/sqlite-basics/sysadmin_practice.db") as conn:
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users")
    rows = cursor.fetchall()
    columns = [desc[0] for desc in cursor.description]
    for row in rows:
        for col, value in zip(columns, row):
            print(f"{col}: {value}")