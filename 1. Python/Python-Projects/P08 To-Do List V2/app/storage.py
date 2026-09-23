import json
# handling data storage with json
class Storage:
    JSON_FILE = "data/tasks.json"

    def save_task(self, tasks):

        with open(self.JSON_FILE, "w") as file:
            json.dump(tasks, file)
        
    def load_task(self):
       try:
           with open(self.JSON_FILE, "r") as file:
               tasks = json.load(file)
               return tasks
       except FileNotFoundError:
           return []
       except ValueError as e:
           print(e)
           return []
        
     

