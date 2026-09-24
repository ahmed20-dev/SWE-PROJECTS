from storage import Storage

tasks = Storage.load_task()

def validate_id(id):
    try: 
        id = int(id)

        if any(task["ID"] == id for task in tasks):
            print("This Id already exist.")
        return id
    except ValueError as e:
        print(e)
        return id
                
def validate_title(title):
    if not id:
        print("Title can't be empty.")
        return
    if any(task["title"] == title for task in tasks):
        print('This Task already exist')
    
def validate_priority(priority):
    priorities = ['low', 'Medium', 'high']
    if priority in priorities:
        return priority
    else:
        print('Invalid priority.')
def validate_status(status):
    if status == "y":
        status = "Complete"
    else:
        status = "Pending"

    return status

# def validate_date(self):
#     pass

