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

print(o.name)  # operating system name, in this case 'posix' for Linux and macOS, 'nt' for Windows
print(p.system()) # operating system name, in this case 'Linux', 'Darwin' for macOS, 'Windows' for Windows
print(p.release()) # operating system version

# exercise
print(sys.argv)

if len(sys.argv) > 1:
    name = sys.argv[1]
    print(f"Hello, {name}! You are running Python version {sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro} on {p.system()}.")
else:
    print("Please enter a name.")