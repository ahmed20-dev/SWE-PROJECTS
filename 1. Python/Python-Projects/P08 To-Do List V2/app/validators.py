
class Validator:
   
   def validate_id(self, id, tasks):
      try: 
          id = int(id)

          if any(task["id"] == id for task in tasks):
            print("This Id already exist.")
            return id
      except ValueError as e:
          print(e)
          return id
                   
   def validate_title(self,title, tasks):
      if not id:
          print("Title can't be empty.")
          return
      if any(task["title"] == title for task in tasks):
          print('This Task already exist')
        
   def validate_priority(self):
       pass
   def validate_date(self):
       pass
   def validate_status(self):
       pass
   