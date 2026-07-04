import json
import sys
import os as o


def create_config_file(filename, config_data):
    with open (filename, "w") as file:
        json.dump(config_data, file, indent=4)

def read_config_file(filename):
    with open(filename, "r") as file:
        config_data = json.load(file)
    return config_data

filename = "config.json"
default_config = {
    "theme": "light",
    "language": "english",
    "keyboard": "italian"
}

if __name__ == "__main__":
    if len(sys.argv) > 2:
        if not o.path.exists(filename):
            create_config_file(filename, default_config)
        config_data = read_config_file(filename)
        config_data[sys.argv[1]] = sys.argv[2]
        create_config_file(filename, config_data)
        print(f"Updated {sys.argv[1]} to {sys.argv[2]}.") 
    else:
        if not o.path.exists(filename):
            create_config_file(filename, default_config)
        config_data = read_config_file(filename)
        for key, value in config_data.items():
            print(f"{key}: {value}")