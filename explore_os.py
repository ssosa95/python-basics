import os as o

print(o.getcwd())
print(o.listdir())

if "calculator.py" in o.listdir():
    print("calculator.py exists in the current directory.")

if o.path.exists("system_config.txt"):
    print("system_config.txt exists in the current directory.")
else:
    print("system_config.txt does not exist in the current directory.")

for file in o.listdir():
    if file.endswith(".py"):
        print(f"Python file found: {file}")


# Notes:
# import os                  # access everything as os.something()
# from os import getcwd      # bring just one function in directly
# import os as o              # alias — shorter to type
# from os import *            # avoid this one — pollutes your namespace, unclear where things came from