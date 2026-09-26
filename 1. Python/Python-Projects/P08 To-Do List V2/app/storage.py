import json
from pathlib import Path
from models import Task


class Storage:

    BASE_DIR = Path(__file__).resolve().parent.parent
    JSON_FILE = BASE_DIR / "data" / "tasks.json"

    def save_task(self, tasks):
        data = []

        for task in tasks:
            data.append({
                "id": task.id,
                "title": task.title,
                "description": task.description,
                "priority": task.priority,
                "status": task.status
            })

        with open(self.JSON_FILE, "w") as file:
            json.dump(data, file, indent=4)

    def load_task(self):
        try:
            with open(self.JSON_FILE, "r") as file:
                data = json.load(file)

            tasks = []

            for item in data:
                task = Task(
                    item["id"],
                    item["title"],
                    item["description"],
                    item["priority"],
                    item["due_date"],
                    item["status"]
                )

                tasks.append(task)

            return tasks

        except FileNotFoundError:
            return []

        except ValueError as e:
            print(e)
            return []
        
     

