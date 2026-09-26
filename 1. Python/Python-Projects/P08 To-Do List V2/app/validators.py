
class Validator:
    def __init__(self, tasks):
        self.tasks = tasks


    def validate_id(self,task_id ):
        try: 
            task_id = int(task_id)
            if any(task["ID"] == id for task in self.tasks):
                print("This Id already exist.")
            return id
        except ValueError as e:
            print(e)
            return id
                    
    def validate_title(self,title):
        if not id:
            print("Title can't be empty.")
            return
        if any(task["title"] == title for task in self.tasks):
            print('This Task already exist')
        
    def validate_priority(self, priority):
        priorities = ['low', 'Medium', 'high']
        if priority in priorities:
            return priority
        else:
            print('Invalid priority.')
    def validate_status(self, status):
        if status == "y":
            status = "Complete"
        else:
            status = "Pending"

        return status

    # def validate_date(self):
    #     pass

