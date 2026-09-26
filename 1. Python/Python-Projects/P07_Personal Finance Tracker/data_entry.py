from datetime import datetime

date_format = "%d-%m-%Y"
categories = {"I": "Income", "E": "Expense"}

# get date
def get_date(prompt, allow_default= False):
    date_str = input(prompt)
    if allow_default and not date_str:
        return datetime.today().strftime(date_format)
    try:
        valid_date = datetime.strptime(date_str, date_format)
        return valid_date.strftime(date_format)
    except ValueError:
        print("Invalid date frmat. Please enter the date in dd-mm-yyyy format")
        return get_date(prompt, allow_default)


# get amount
def get_amount():
    try:
        amount = float(input("Enter amount: "))
        if amount <= 0:
            raise ValueError("Please enter non-nagetive number or non-zero.")
        return amount
    except ValueError as e:
        print(e)
        return get_amount()

# get category ( Expense or Income)
def get_category():
    
    category = input("Enter the category 'E' for Expense or 'I' for Income: ").upper()
    if category in categories:
        return categories[category]
    print("Invalid category.Please enter 'E' for Expense or 'I' for Income.")
    return get_category()
    

# get Description
def get_descriptipn():
    return input("Enter description (Optional): ")
     


