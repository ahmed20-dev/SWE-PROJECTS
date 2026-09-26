from models import Task
from validators import Validator
from manager import Manager
from storage import Storage
from datetime import datetime
import json

storage = Storage()
tasks = storage.load_task()

manager = Manager(tasks, storage)
validator = Validator(tasks)

def menu():
    print('==== To-Do List manager ====')
    print("\n1.View Tasks")
    print("2. Add task")
    print("3. Update task")
    print("4. Delete task")
    print("5. Exit\n")

def add_task():
    task_id = input("Enter task ID: ")
    validator.validate_id(task_id)

    title = input("Enter task title: ")
    validator.validate_title(title)

    description = input("Enter task description (Optional): ")

    priority = input("choice task priority: ")
    validator.validate_priority(priority)

    status = input("is this task pending or completed: ").lower()
    validator.validate_status(status)

    task = Task(
        task_id,
        title,
        description,
        priority,
        status
    )
    manager.add_task(task)


def main(): 
    while True:
        menu()
        choice = input("Your choice: ")

        if choice == '1':
            manager.view_task(tasks)
        elif choice == '2':
            add_task()
        elif choice == '3':
            pass
        elif choice == '4':
            manager.delete_task()
        elif choice == '5':
            print('Exiting...')
        else:
            print('Invalid choice.')


if __name__== "__main__":
    main()


        




