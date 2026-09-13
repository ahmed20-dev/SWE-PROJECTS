import json
import csv
from datetime import datetime
from data_entry import get_amount, get_category, get_date , get_descriptipn



class Transtion:
    JSON_FILE = "finance_date.json"

    @classmethod
    def add_entry(cls, amount, category, description, date ):
        new_entry = {
            "Date": date,
            "Amount": amount,
            "Category": category,
            "Description": description
        }

        with open(cls.JSON_FILE, "w") as file:
                json.dump( new_entry, file)

def menu():
    print("\n==============================")
    print(" Personal Finance TRACKER")
    print("==============================")

    print("1. Add transtion")
    print("2. View summary")
    print("3. Export to CSV file")
    print("4. Exit")

    print("==============================")


def add():
    date = get_date(
        "Enter the date of the transaction (dd-mm-yyyy) or enter for today's date: ",
        allow_default=True,
    )
    amount = get_amount()
    category = get_category()
    description = get_descriptipn()

    Transtion.add_entry(date, amount, category,description )


def main():
    while True:
        menu()
        choice = input("Choice: ")

        if choice == "1":
            add()
        elif choice == "2":
            pass
        elif choice == "3":
            pass
        elif choice == "4":
            print("Exiting.....")
            break
        else:
            print("Invalid choice.")


if __name__== "__main__":
    main()