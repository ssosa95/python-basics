import os as o
import platform as p
import sys
from datetime import datetime

def get_system_info(directory=None):
    if directory is None:
        directory = o.getcwd()
    files = o.listdir(directory)
    info = {
    "os": p.system(),
    "version": p.release(),
    "python": f"{sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}",
    "date_and_time": datetime.now().strftime("%d/%m/%Y %H:%M:%S"),
    "current_directory": directory,
    "number_of_files": len(files)

    }
    return info

if __name__ == "__main__":
    if len(sys.argv) > 1:
        if o.path.isdir(sys.argv[1]):
            info = get_system_info(sys.argv[1])
            for keys, value in info.items():
                print(f"{keys}: {value}")
        else:
            print(f"{sys.argv[1]} is not a valid directory.")
            sys.exit(1)
    else:
        info = get_system_info()
        for keys, value in info.items():
                print(f"{keys}: {value}")


# keep sys.exit(1) in mind, exits the script with an error code. 0 means "clean exit"
# and 1 means "something went wrong"
# It's a convention that other tools and scripts can read.