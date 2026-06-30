import os as o
import sys
import platform as p


version_list = []

version = sys.version
parts = version.split(" ")
version_number = parts[0]
version_list.append(version_number)

print(version_list)

# or

print(sys.version_info)


# or

print(f"Python version: {sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}")

print(o.name)

# exercise
print(sys.argv)

if len(sys.argv) > 1:
    name = sys.argv[1]
    print(f"Hello, {name}! You are running Python version {sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro} on {p.system()}.")
else:
    print("Please enter a name.")