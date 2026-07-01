# Exercise - 
# take the sysinfo.py project from yesterday and write the output to a file called sysinfo.json 
# instead of printing it to the terminal. Open the file afterward and check it looks readable.

import json
from sysinfo import get_system_info

info = get_system_info()
with open("sysinfo.json", "w") as file:
          json.dump(info, file, indent=4)