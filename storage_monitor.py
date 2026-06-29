# storage_monitor.py
# CLI tool to monitor storage usage across multiple servers
# Classifies each server as OK (<60%), WARNING (60-80%), or CRITICAL (>80%)
# Outputs a summary with counts per status and average usage across all servers
# Built: Week 1, Day 4
# Known gaps: non-numeric input for server count or storage usage causes crash (fix Day 9)
#             storage values outside 0-100% are accepted without validation

servers = []
storage = []
counter_ok = 0
counter_warning = 0
counter_critical = 0
total_server_storage = 0
try:
    server_count = int(input("Enter the number of servers to monitor: "))
except ValueError:
    print("That is not a valid input. Please enter a valid whole number.")
for i in range(server_count):
    server = input("Write the server name: ")
    try:
        storage_usage = int(input("How much of the server is being used? "))
    except ValueError:
        print("That is not a valid inpit. Please enter a valid whole number.")
    servers.append(server)
    storage.append(storage_usage)



for i in range(len(servers)):
    if storage[i] < 60:
        status = "[OK]"
        counter_ok += 1
    elif storage[i] < 80:
        status = "[WARNING]"
        counter_warning += 1
    else:
        status = "[CRITICAL]"
        counter_critical += 1
    print(f"{servers[i]} : {storage[i]}% {status}")

for usage in storage:
    total_server_storage += usage

average_counter = total_server_storage / server_count

print(f"""
Total servers monitored: {server_count}
OK: {counter_ok}
WARNING: {counter_warning}
CRITICAL: {counter_critical}
Average storage usage: {average_counter}%
""")