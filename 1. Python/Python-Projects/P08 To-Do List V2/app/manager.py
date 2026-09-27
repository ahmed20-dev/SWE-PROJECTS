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
        task_id = int(task_id)

        for task in self.tasks:
            if task.id == task_id:
                self.tasks.remove(task)
                self.storage.save_task(self.tasks)
                print("Task deleted")
                return
            
        print("Task not found.")

    def mark_task(self):
        pass


