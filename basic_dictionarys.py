info = {
    "os": "Windows",
    "python": "3.11",
    "cwd": "/home/user"
}

# loop just the keys
for key in info:
    print(key)        # os, python, cwd

# loop just the values
for value in info.values():
    print(value)      # Windows, 3.11, /home/user

# loop both at once
for key, value in info.items():
    print(key, value) # os Windows, python 3.11, etc.