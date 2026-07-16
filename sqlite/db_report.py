import sqlite3

with sqlite3.connect("C:/Users/user/projects/sqlite-basics/sysadmin_practice.db") as conn:
    cursor = conn.cursor()
    cursor.execute("SELECT active, COUNT(*) FROM users GROUP BY active")
    results = cursor.fetchall()
    print("Total of each type of user.")
    for active, count in results:
        if active == 0:
            status = "Inactive"
        else:
            status = "Active"
        print(f"{status}: {count}")
    cursor.execute("SELECT status, COUNT(*) FROM servers GROUP BY status")
    results = cursor.fetchall()
    print("Total of each type of server state.")
    for state, count in results:
        print(f"{state}: {count}")
    cursor.execute("SELECT hostname, assigned_to FROM servers WHERE assigned_to IS NULL")
    results = cursor.fetchall()
    print("Servers with no assigned user.")
    for server, assigned in results:
        print(f"{server}: unassigned")
    cursor.execute("""
                   SELECT u.name, COUNT(s.assigned_to) 
                   FROM users u LEFT JOIN servers s ON u.id = s.assigned_to 
                   WHERE active = 1 
                   GROUP BY u.id
    """)
    results = cursor.fetchall()
    print("List of users and the number of servers they are responsible for.")
    for name, number in results:
        print(f"{name}: {number}")