from models import Task
from validators import Validator
from manager import Manager
from storage import Storage
from datetime import datetime


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
    print("5. Mark task as a completed")
    print("6. Filter tasks by status")
    print("7. Filter tasks by priority")
    print("8. Exit\n")

def add_task():
    while True:
        try:
            
            task_id = input("Enter task ID: ")
            task_id = validator.validate_id(task_id)
            break

        except ValueError as e:
                print(f"Error: {e}")

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

def update_task():
    manager.view_task()

    task_id = input("Enter the Task ID to update: ")

    try:
        task_id = int(task_id)
    except ValueError:
        print("ID must be a valid number.")
        return

    title = input("Enter task title: ")
    validator.validate_title(title)

    description = input("Enter task description (Optional): ")

    priority = input("Choose task priority: ")
    validator.validate_priority(priority)

    status = input("Is this task pending or completed: ").lower()
    validator.validate_status(status)

    manager.update_task(
        task_id,
        title,
        description,
        priority,
        status
    )

def main(): 
    while True:
        menu()
        choice = input("Your choice: ")

        if choice == '1':
            manager.view_task()
        elif choice == '2':
            add_task()
        elif choice == '3':
            update_task()
        elif choice == '4':
            manager.view_task()
            task_id = input("Enter the task ID to delete: ")
            manager.delete_task(task_id)

        elif choice == "5":
            manager.view_task()
            task_id =  input("Enter the task ID to mark: ")
            manager.mark_task(task_id)

        elif choice == "6":
            manager.filter_status()
        elif choice == "7":
            manager.filter_priority()
        elif choice == '8':
            print('Exiting...')
            break
        else:
            print('Invalid choice.')


if __name__== "__main__":
    main()


        




