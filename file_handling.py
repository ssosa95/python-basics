file = open('sample_text.txt', 'r') # "r" means read mode
content = file.read() # Read the entire content of the file
print(content) # Print the content to the terminal
file.close() # Always close what you open

# "r" Read - file must exist
# "w" Write - creates file if it doesn't exist, overwrites if it does
# "a" Append - adds to the end without overwriting
# "r+" - Read and write

# problem with this approach is that if your code crashes between open() and close(), the file stays open

with open('sample_text.txt', 'r') as file: # as file gives the opened file a name to work with inside the block.
    content = file.read()
    print(content)
# file is automatically closed here, no matter what

# Three Ways To Read

# 1. read() - entire file in one string

with open ('sample_text.txt', 'r') as file:
    content = file.read()
    print(content)

# 2. readlines() - entire file as a list, one item per line

with open ('sample_text.txt', 'r') as file:
    lines = file.readlines()
    print(lines) # ['server-01 online\n', 'server-02 offline\n', 'server-03 online\n', 'server-04 offline\n', 'server-05 online']
    print(type(lines)) # <class 'list'>
    for line in lines:
        print(line.strip()) # gets rid of the \n and prints in a format similar to read()

# 3. readline() - one line at a time:

with open ('sample_text.txt', 'r') as file:
    line = file.readline()
    print(line)    
    line = file.readline()
    print(line)


# Writing to a File

with open ('output.txt', 'w') as file:
    file.write("First line\n")
    file.write("Second line\n")
    file.write("Third line\n")

lines = ["alpha\n", "beta\n", "gamma\n"]
with open ('output.txt', 'w') as file:
    file.writelines(lines)  # Note that write() and writelines() don't add newlines automatically
                            # Have to input \n manually


# Appending to a File

with open ('output.txt', 'a') as file:  # 'a' would be used in a log file, something that should never be overwritten
    file.write("This line was appended\n")



