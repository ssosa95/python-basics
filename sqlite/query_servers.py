import sqlite3

with sqlite3.connect("C:/Users/user/projects/sqlite-basics/sysadmin_practice.db") as conn:
    cursor = conn.cursor()
    cursor.execute("SELECT hostname, ip_address FROM servers WHERE status = ?", ("online",))
    rows = cursor.fetchall()
    columns = [desc[0] for desc in cursor.description]
    for row in rows:
        for col, value in zip(columns, row):
            print(f"{col}: {value}")
    
    cursor.execute(
        "SELECT status, COUNT(*) FROM servers GROUP BY status"
)
    status_counts = cursor.fetchall()
    for status, count in status_counts:
        print(f"{status}: {count}")