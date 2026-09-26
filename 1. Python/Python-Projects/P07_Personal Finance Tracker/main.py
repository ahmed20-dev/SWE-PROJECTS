import json
import csv
from datetime import datetime
from data_entry import get_amount, get_category, get_date , get_descriptipn



class Transaction:
    JSON_FILE = "finance_date.json"
    CSV_FILE = "finance_date.csv"

    # saving data to Json file
    @classmethod
    def add_entry(cls,data):
        with open(cls.JSON_FILE, "w") as file:
                json.dump(data, file)

    # loading data from Json file
    @classmethod
    def load_data(cls):
        try:
            with open(cls.JSON_FILE, "r") as file:
                return json.load(file)

        except FileNotFoundError:
            return []

        except ValueError as e:
            print(e)
            return []
    @classmethod
    def to_csv(cls):
        data = Transaction.load_data()
        with open(cls.CSV_FILE, "w", newline= "") as file:
            writer = csv.DictWriter(
                file,
                fieldnames=[
                    "Date",
                    "Amount",
                    "Category",
                    "Description",
                ]
            )
            writer.writeheader()
            for transaction in data:
                writer.writerow(transaction)
            



def menu():
    print("\n==============================")
    print(" Personal Finance TRACKER")
    print("==============================")

    print("1. Add transtion")
    print("2. View summary")
    print("3. Export to CSV file")
    print("4. Exit")

    print("==============================")

# adding a new transtion from the user
def add(data):
    date = get_date(
        "Enter the date of the transaction (dd-mm-yyyy) or enter for today's date: ",
        allow_default=True,
    )
    amount = get_amount()
    category = get_category()
    description = get_descriptipn()
    new_entry = {
        "Date": date,
        "Amount": amount,
        "Category": category,
        "Description": description
        }
    data.append(new_entry)
    Transaction.add_entry(data)
    print("Entry added successfully.")

# Sumarise transactions into ( totol_income, total_expense, net_saving)

def get_summary(data):
    if not data:
        print("There is no data yet.")
        return
    # get total income
    total_income = 0
    for transaction in data:
        if transaction["Category"] == "Income":
            total_income += transaction["Amount"]

    # get total expense
    total_expense = 0
    for transaction in data:
        if transaction["Category"] == "Expense":
            total_expense += transaction["Amount"]
       
    # get Balance
    balance = total_income - total_expense

    print("\n==============================")
    print(" Personal Finance Summary")
    print("==============================")
    print(f"Total Income: ${total_income}")
    print(f"Total Expense: ${total_expense}")
    print(f"Balance: ${balance}")

# export from csv file 

def export_csv():
    Transaction.to_csv()
    try:
        with open(Transaction.CSV_FILE, "r") as file:
           reader = csv.DictReader(file)
           print("Date,Amount,Category,Description")
           
           for row in reader:
               print(f"{row['Date']},{row['Amount']},{row['Category']},{row['Description']}")

    except FileNotFoundError:
        print("File not found.")            

def main():
    data = Transaction.load_data()
    while True:
        menu()
        choice = input("Choice: ")

        if choice == "1":
            add(data)
        elif choice == "2":
            get_summary(data)
        elif choice == "3":
            export_csv()
        elif choice == "4":
            print("Exiting.....")
            break
        else:
            print("Invalid choice.")


if __name__== "__main__":
    main()