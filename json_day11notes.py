import json

# string → dictionary
data = json.loads('{"name": "Samuel", "age": 25}')

# dictionary → string
text = json.dumps({"name": "Samuel", "age": 25})

# file → dictionary
with open("config.json") as f:
    data = json.load(f)

# dictionary → file
with open("config.json", "w") as f:
    json.dump(data, f)


# JSON is just a text format for storing structured data
# The pattern is consistent: the s variants (loads, dumps) work with strings. 
# The plain variants (load, dump) work with files.

# indent parameter: json.dump() 
# and json.dumps() accept an indent argument that makes the output human-readable:

json.dumps(data, indent=4)