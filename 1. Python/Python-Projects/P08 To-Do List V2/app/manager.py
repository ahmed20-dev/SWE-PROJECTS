from models import Task
from storage import Storage
from validators import Validator


class Manager:
    def __init__(self, tasks):
        self.tasks = tasks

    def view_task(self, tassks):
        if 0 >= len(self.tasks):
            print("There is no tasks yet.")
            return
        else:
            print('-'* 5 + 'Your Tasks' + '-' * 5)
            for task in self.tasks:
                print(f" Id: {task.id} Title: {task.title} description: {task.description} priority: {task.priority} dou date: {task.dou_date} status: {task.status}")



    def add_task(self, task):
        self.tasks.append(task)
        Storage.save_task()
        print('Task added successfully.')

    def update_task(self, task_id):
        for task in self.tasks:
            if task["id"] == task_id:
                pass
    def delete_task(self, task_id):
        for task in self.tasks:
            if task["id"] == task_id:
                del self.tasks[task]
                Storage.save_task()
                print("Student deleted")
                return
        print("Task not found.")

    def mark_task(self):
        pass


