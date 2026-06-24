servers = []
storage = []
counter_ok = 0
counter_warning = 0
counter_critical = 0
total_server_storage = 0

server_count = int(input("Enter the number of servers to monitor: "))

for i in range(server_count):
    server = input("Write the server name: ")
    storage_usage = int(input("How much of the server is being used? "))
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
total_counter = counter_ok + counter_warning + counter_critical
average_counter = total_server_storage / total_counter

print(f"""
Total servers monitored: {server_count}
OK: {counter_ok}
WARNING: {counter_warning}
CRITICAL: {counter_critical}
Average storage usage: {average_counter}%
""")