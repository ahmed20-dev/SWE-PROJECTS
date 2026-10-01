from models import Task
from storage import Storage


class Manager:
    def __init__(self, tasks, storage):
        self.tasks = tasks
        self.storage = storage


    def view_task(self):
        if 0 >= len(self.tasks):
            print("There is no tasks yet.")
            return
        else:
            print('-'* 5 + 'Your Tasks' + '-' * 5)
            for task in self.tasks:
                print(f" Id: {task.id} Title: {task.title} description: {task.description} priority: {task.priority} status: {task.status}")



    def add_task(self, task):
        self.tasks.append(task)
        self.storage.save_task(self.tasks)
        print('Task added successfully.')

    def update_task(self, task_id, title, description, priority, status):
        for task in self.tasks:
            if task.id == task_id:
                task.title = title
                task.description = description
                task.priority = priority
                task.status = status

                self.storage.save_task(self.tasks)
                print("Task updated successfully.")
                return

        print("Task not found.")
    
            
    def delete_task(self, task_id,):
        try:
            task_id = int(task_id)
        except ValueError:
            print("ID must be an exist ID.")
            return
        
        for task in self.tasks:
            if task.id == task_id:
                self.tasks.remove(task)
                self.storage.save_task(self.tasks)
                print("Task deleted")
                return
            
        print("Task not found.")

    def mark_task(self, task_id):
        try:
            task_id = int(task_id)
        except ValueError:
                print("ID must be an exist ID.")
                return
        
        for task in self.tasks:
            if task.id == task_id:
                if task.status != "completed":
                    task.status = "completed"
                    self.storage.save_task(self.tasks)
                    print("Task marked as a completed.")
                    return
                print("This task already marked")
                return
        print("Task not found.")

    # Filter tasks by status

    def filter_status(self):
        print("\n== Completed tasks ==")
        for task in self.tasks:
            if task.status == "completed":
                print(f" Id: {task.id} Title: {task.title} description: {task.description} priority: {task.priority} status: {task.status}")

        print("\n== Uncompleted tasks ==")
        for task in self.tasks:
            if task.status == "pending":
                print(f" Id: {task.id} Title: {task.title} description: {task.description} priority: {task.priority} status: {task.status}")

    #Filter tasks by priority
    def filter_priority(self):
        print("\n== High priority tasks ==")
        for task in self.tasks:
            if task.priority == "high":
                print(f" Id: {task.id} Title: {task.title} description: {task.description} priority: {task.priority} status: {task.status}")

        print("\n== medium priority tasks ==")
        for task in self.tasks:
            if task.priority == "medium":
                print(f" Id: {task.id} Title: {task.title} description: {task.description} priority: {task.priority} status: {task.status}")

        print("\n== low priority tasks ==")
        for task in self.tasks:
            if task.priority == "low":
                print(f" Id: {task.id} Title: {task.title} description: {task.description} priority: {task.priority} status: {task.status}")


                

                


        


