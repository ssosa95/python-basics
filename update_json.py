# Exercise: Update JSON File - 
# read user.json, add a new field to it ("last_seen" with today's date as a string), 
# then write it back to the same file. Open the file and confirm the new field is there.

import json
from datetime import datetime


with open("user.json", "r") as file: # read the file
    data = json.load(file)           # load the JSON data into a Python dictionary

data["last_seen"] = datetime.now().strftime("%d/%m/%Y %H:%M:%S")  # add a new field with today's date as a string

with open("user.json", "w") as file:  # write the updated dictionary back to the same file
    json.dump(data, file, indent=4)   # dump the updated dictionary to the file with indentation for readability


# Advanced method: read the file, update the dictionary, then write it back to the same file.
#with open("user.json", "r+") as file:
#    data = json.load(file)
#    data["last_seen"] = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
#    file.seek(0)
#    json.dump(data, file, indent=4)
#    file.truncate()