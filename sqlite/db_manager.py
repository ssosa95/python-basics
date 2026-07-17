import sqlite3
import sys

def list_users(cursor):
    cursor.execute("SELECT * FROM users")
    rows = cursor.fetchall()
    columns = [desc[0] for desc in cursor.description]
    for row in rows:
        for col, value in zip(columns, row):
            print(f"{col}: {value}")
        print("---")

def add_user(cursor, name, role, active):
    cursor.execute("INSERT INTO users(name, role, active) VALUES(?, ?, ?)", (name, role, active))
    cursor.connection.commit()
    print(f"Added user with id {cursor.lastrowid} last.")

def delete_user(cursor, user_id):
    cursor.execute("DELETE FROM users WHERE id = ?", (user_id,))
    cursor.connection.commit()
    if cursor.rowcount == 0:
        print(f"No user found with id {user_id}.")
    else:
        print(f"Deleted user {user_id}.")

def list_servers(cursor):
    cursor.execute("SELECT * FROM servers")
    rows = cursor.fetchall()
    columns = [desc[0] for desc in cursor.description]
    for row in rows:
        for col, value in zip(columns, row):
            print(f"{col}: {value}")
        print("---")

def add_server(cursor, hostname, ip_address, os, status):
    cursor.execute("INSERT INTO servers(hostname, ip_address, os, status) VALUES(?, ?, ?, ?)", (hostname, ip_address, os, status))
    cursor.connection.commit()
    print(f"Added server with id {cursor.lastrowid} last.")

def assign_server(cursor, server_id, user_id):
    cursor.execute("UPDATE servers SET assigned_to = ? WHERE id = ?", (user_id, server_id))
    cursor.connection.commit()
    if cursor.rowcount == 0:
        print(f"No user found with id {user_id}.")
    else:
        print(f"Assigned to user {user_id}.")
def report_summary(cursor):
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

if __name__ == "__main__":
    with sqlite3.connect("C:/Users/user/projects/sqlite-basics/sysadmin_practice.db") as conn:
        cursor = conn.cursor()
        if len(sys.argv) < 2:
            print("Usage: python db_manager.py <command>")
            sys.exit(1)
        elif sys.argv[1] == "users":
            if len(sys.argv) < 3:
                print("Usage: python db_manager.py users <action>")
            elif sys.argv[2] == "list":
                if len(sys.argv) != 3:
                    print("Usage: python db_manager.py users list")
                else:
                    list_users(cursor)
            elif sys.argv[2] == "add":
                if len(sys.argv) != 6:
                    print("Usage: python db_manager.py users add <name> <role> <active>")
                else:
                    add_user(cursor, sys.argv[3], sys.argv[4], int(sys.argv[5]))
            elif sys.argv[2] == "delete":
                if len(sys.argv) != 4:
                    print("Usage: python db_manager.py users delete <user_id>")
                else:
                    delete_user(cursor, int(sys.argv[3]))
            else:
                print(f"Unrecognised command: {sys.argv[1]}")
        elif sys.argv[1] == "servers":
            if len(sys.argv) < 3:
                print("Usage: python db_manager.py servers <action>")
            elif sys.argv[2] == "list":
                if len(sys.argv) != 3:
                    print("Usage: python db_manager.py servers list")
                else:
                    list_servers(cursor)
            elif sys.argv[2] == "add":
                if len(sys.argv) != 7:
                    print("Usage: python db_manager.py servers add <hostname> <ip_address> <os> <status>")
                else:
                    add_server(cursor, sys.argv[3], sys.argv[4], sys.argv[5], sys.argv[6])
            elif sys.argv[2] == "assign":
                if len(sys.argv) != 5:
                    print("Usage: python db_manager.py servers assign <server_id> <user_id>")
                else:
                    assign_server(cursor, int(sys.argv[3]), int(sys.argv[4]))
            else:
                print(f"Unrecognised command: {sys.argv[1]}")
        elif sys.argv[1] == "report":
            report_summary(cursor)