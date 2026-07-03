import os as o
import json


def add_task(tasks, task):
    tasks.append(task)
    print(f"Task '{task}' added.")

def list_tasks(tasks):
    if not tasks:
        print("No tasks in the list.")
    else:
        for i in range(len(tasks)):
            print(f"{i+1}. {tasks[i]}")

def remove_task(tasks, index):
    if not tasks:
        print("No tasks in the list to remove.")
    else:
        if len(tasks) < index or index < 1:
            print("Invalid task number.")
        else:    
            tasks.pop(index - 1)
            print(f"Task {index} removed.")

def load_tasks(filename):
    try:
        with open(filename, 'r') as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):  # json.JSONDecodeError - covers the corrupted file case from the brief. If the file exists but contains garbage, json.load throws that instead of FileNotFoundError
        return []
        

def save_tasks(tasks, filename):
    with open(filename, 'w') as file:
        json.dump(tasks, file, indent=4)


filename = "tasks.json"
tasks = load_tasks(filename)
print("Welcome to the To-Do List CLI! Commands: add, remove, list, quit")
while True:
    user_input = input("> ").split(" ", 1)

    if user_input[0].lower() == "quit":
        break
    elif user_input[0].lower() == "add":
        try:
            task = user_input[1]  # Get the task description from the input
            add_task(tasks, task)
            save_tasks(tasks, filename)
        except IndexError:
            print("Please provide a task description.")
    elif user_input[0].lower() == "remove":
        try:
            index = int(user_input[1])
            remove_task(tasks, index)
            save_tasks(tasks, filename)
        except (ValueError, IndexError):
            print("Please enter a valid task number.")
            print("Remove syntax: remove <task number>")
    elif user_input[0].lower() == "list":
        list_tasks(tasks)
    else:
        print(f"{user_input[0]} is an invalid input. Please try again or quit the program.")