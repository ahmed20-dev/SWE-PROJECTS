from validators import Validator
from manager import Manager
from storage import Storage
from datetime import datetime
import json

storage = Storage()
tasks = storage.load_task()
validator = Validator(tasks)

def menu():
    print('==== To-Do List manager ====')
    print("1.View Tasks")
    print("2. Add task")
    print("3. Update task")
    print("4. Delete task")
    print("5. Exit")

def add_task():
    task_id = int(input("Enter task ID: "))
    validator.validate_id(id)

    title = input("Enter task title: ")
    validator.validate_title(title)

    description = input("Enter task description (Optional): ")

    priority = input("choice task priority: ")
    validator.validate_priority(priority)

    # dou_date = input("Enter task dou date: ")
    # Validator.validate_date()

    status = input("is this task already completed? (Y/N)")
    validator.validate_status(status)

    task = {
        'ID': task_id,
        'Title' : title,
        'Description': description,
        'Priority' : priority,
        'Status' : status
    }
    

    
    
add_task()

# def main():
#     while True:
#         menu()
#         choice = input("Your choice: ")

#         if choice()

        




