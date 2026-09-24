from validators import Validator
from manager import Manager
from storage import Storage
from datetime import datetime
import json



def menu():
    print('==== To-Do List manager ====')
    print("1.View Tasks")
    print("2. Add task")
    print("3. Update task")
    print("4. Delete task")
    print("5. Exit")

def add_task():
    task_id = input("Enter task ID: ")
    Validator.validate_id()

    title = input("Enter task title: ")
    Validator.validate_title()

    description = input("Enter task description (Optional): ")

    priority = input("choice task priority: ")
    Validator.validate_priority()

    dou_date = input("Enter task dou date: ")
    Validator.validate_date()

    status = input("choice the task status")
    Validator.validate_status()



# def main():
#     while True:
#         menu()
#         choice = input("Your choice: ")

#         if choice()

        




