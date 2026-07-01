import json
from datetime import datetime



with open("user.json", "r+") as file:
    data = json.load(file)
    data["last_seen"] = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    file.seek(0)
    json.dump(data, file, indent=4)
    file.truncate()