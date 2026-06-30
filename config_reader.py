def read_config(filepath):
    keys = []
    values = []

    try:
        with open(filepath, 'r') as file:
            for line in file:
                if "=" not in line:
                    continue
                parts = line.split("=")
                keys.append(parts[0])
                values.append(parts[1].strip())
        return keys, values
    except FileNotFoundError:
        print(f"Error: '{filepath}' not found.")
        return [], []
    

def get_config_value(keys, values, target_key):  
    for key in range(len(keys)):                            
        if keys[key] == target_key:               #if target_key in keys:
            return values[key]                    #   return values[keys.index(target_key)]
                                                  #return None
 
    return None
 
 # the commented out code works and is cleaner, not needing a loop, 
 # but I wanted to try a different approach using a for loop and indexing

        
    
    

def validate_config(keys, values):
    required_keys = ["hostname", "port", "max_connections", "timeout"]
    missing_keys = []
    for key in required_keys:
        if key not in keys:
            print(f"Missing required config key: {key}")
            missing_keys.append(key)
    

    if len(missing_keys) > 0:
        return False
    
    return True
        
def validate_port(keys, values):
    try:
        port_number = int(get_config_value(keys, values, 'port'))
        if port_number > 0 and port_number < 65536:  # if 1 <= port_number <= 65535: cleaner way to write it
            return True
        print("Port out of range.")
        return False
    except TypeError:
        print("There is no port key.")
        return False
    except ValueError:
        print("Not a valid port number.")
        return False


filepath = 'server_config.txt'

keys, values = read_config(filepath)

if validate_config(keys, values):
    if validate_port(keys, values):
        print("Config loaded successfully.")
        print(f"Hostname: {get_config_value(keys, values, 'hostname')}")
        print(f"Port: {get_config_value(keys, values, 'port')}")
        print(f"Max connections: {get_config_value(keys, values, 'max_connections')}")
        print(f"Timeout: {get_config_value(keys, values, 'timeout')}")
        while True:
            search_key = input("\nEnter a config key to look up (or 'quit' to exit): ")
            if search_key == "quit":
                break
            try:
                result = get_config_value(keys, values, search_key)
                if result is None:
                    raise ValueError(f"Key '{search_key}' not found in config.")
                print(f"{search_key} = {result}")
            except ValueError as e:
                print(f"Error: {e}")
            else:
                print(f"Port validation failed.")
        
else:
    print("Config validation failed. Please fix the config file.")
