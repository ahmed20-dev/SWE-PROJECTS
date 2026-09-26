
class Validator:
    def __init__(self, tasks):
        self.tasks = tasks


    def validate_id(self,task_id ):
        try: 
            task_id = int(task_id)
            if task_id <= 0:
                raise ValueError("ID must be greater than 0.")
            if any(task["ID"] == id for task in self.tasks):
                raise ValueError("This Id already exist.")

        except ValueError as e:
            print(e)
                    
    def validate_title(self,title):
        if not title.strip():
            raise ValueError("Title cannot be empty")

        if any(task["title"] == title for task in self.tasks):
            print('This Task title already used')
        
    def validate_priority(self, priority):
        if priority not in ["low", "medium", "high"]:
            raise ValueError("Invalid priority")
        
    def validate_status(self, status):
        if status not in ["pending", "completed"]:
            raise ValueError("Invalid status")

