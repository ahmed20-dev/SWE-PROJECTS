
class Validator:
    def __init__(self, tasks):
        self.tasks = tasks


    def validate_id(self, task_id):
        task_id = int(task_id)

        if task_id <= 0:
            raise ValueError("ID must be greater than 0.")

        for task in self.tasks:
            if task.id == task_id:
                raise ValueError("This ID already exists.")

        return task_id
                        
    def validate_title(self,title):
        if not title.strip():
            raise ValueError("Title cannot be empty")

        for task in self.tasks:
            if task.title == title:
                raise ValueError("This task title already used.")
        return title
        
    def validate_priority(self, priority):
        if priority not in ["low", "medium", "high"]:
            raise ValueError("Invalid priority")
        return priority
        
    def validate_status(self, status):
        if status not in ["pending", "completed"]:
            raise ValueError("Invalid status")
        return property

