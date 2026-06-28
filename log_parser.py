# log_parser.py
# Reads a server status file and reports which servers are offline
# Built: Week 2, Day 8

offline_servers = []
online_servers = []

with open('sample_text.txt', 'r') as file:
    for line in file:
        line = line.strip()
        parts = line.split(" ") # splits "server-01 online" into ["server-01", "online"]
        server_name = parts[0]
        status = parts[1]

        if status == "offline":
            offline_servers.append(server_name)
        else:
            online_servers.append(server_name)

print(f"Offline servers: {len(offline_servers)}")
print(f"Online servers: {len(online_servers)}")

if len(offline_servers) > 0:
    print("\nThe following servers need attention:")
    for server in offline_servers:
        print(f" - {server}")

#Write a report file

with open('server_report_file.txt', 'w') as file:
    file.write("SERVER STATUS REPORT\n")
    file.write("====================\n")
    file.write(f"Online servers: {len(online_servers)}\n")
    file.write(f"Offline servers: {len(offline_servers)}\n")
    file.write("\nOffline servers:\n")
    for server in offline_servers:
        file.write(f" - {server}\n")

print("\nReport written to server_report_file.txt")

# File Paths

# relative path — looks in current folder
# open("sample.txt")

# relative path — looks in a subfolder
# open("logs/sample.txt")

# absolute path — works regardless of where you run from
# open("C:/Users/user/projects/python-basics/sample.txt")