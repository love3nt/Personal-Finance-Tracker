# This file will handle the main flow of the program.

# Import necessary modules
import pandas as pd
import csv
import os
import time
from datetime import datetime
from data_entry import get_date, get_amount, get_category, get_description

# Initialize the CSV class to handle CSV file operations
class CSV:
    CSV_FILE = 'finance_data.csv'
    COLUMN_NAMES = ['Date', 'Amount', 'Category', 'Description']
    FORMAT = "%d-%m-%Y"

    @classmethod
    def initialize_csv(cls):
        try: 
            pd.read_csv(cls.CSV_FILE)
        except FileNotFoundError:
            # If the file does not exist, create it with the appropriate headers
            df = pd.DataFrame(columns=cls.COLUMN_NAMES)
            # Export the DataFrame to a CSV file
            df.to_csv(cls.CSV_FILE, index=False)

# Method to add a new entry to the CSV file
    @classmethod
    def add_entry(cls, date, amount, category, description):
        new_entry = {
            'Date': date,
            'Amount': amount,
            'Category': category,
            'Description': description
        }
        
        # Open the CSV file in append mode and write the new entry  
        with open(cls.CSV_FILE, mode='a', newline='') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=cls.COLUMN_NAMES)
            # If the file is empty, write the header
            writer.writerow(new_entry)
       
        os.system('cls')
        print(f"Entry added successfully: {new_entry}")
        time.sleep(3)
        
     
# Method to view entries within a specified date range
    @classmethod
    def view_entries(cls, start_date, end_date):
        df =pd.read_csv(cls.CSV_FILE)
        df["date"] = pd.to_datetime(df["Date"], format=CSV.FORMAT)
        start_date = datetime.strptime(start_date, CSV.FORMAT)
        end_date = datetime.strptime(end_date, CSV.FORMAT)

        mask = (df['date'] >= start_date) & (df['date'] <= end_date)
        filtered_df = df.loc[mask]

        if filtered_df.empty:
            print("No transactions found for the specified date range.")
        else:
            print(
                f"\nTransactions from {start_date.strftime(CSV.FORMAT)} to {end_date.strftime(CSV.FORMAT)}\n"
            )
            print(
                filtered_df.to_string(
                    index=False, formatters={"date": lambda x: x.strftime(CSV.FORMAT)}
                )
            )

            total_income = filtered_df[filtered_df["Category"] == "Income"]["Amount"].sum()
            total_expense = filtered_df[filtered_df["Category"] == "Expense"]["Amount"].sum()
            print("\nSummary:")
            print(f"Total Income: ${total_income:.2f}")
            print(f"Total Expense: ${total_expense:.2f}")
            print(f"Net Balance: ${(total_income - total_expense):.2f}")


# Main function to add a new entry        
def add():
    CSV.initialize_csv()
    date = get_date("\n\nEnter the date (dd-mm-yyyy) or press Enter for today's date: ", allow_default=True)
    amount = get_amount()
    category = get_category()
    description = get_description()
    CSV.add_entry(date, amount, category, description)
    
# Main menu function to navigate through the program
def main_menu():
    os.system('cls')
    print("Initializing Personal Finance Tracker...")
    time.sleep(2)
    os.system('cls')
    
    first_time = True
    while True:
        os.system('cls')
        if first_time:
            print("Welcome to your Personal Finance Tracker!")
            print("This program will help you track your income and expenses.\n")
            first_time = False
        print("Main Menu:\n----------------------")
        print("1. Add Entry")
        print("2. View Transactions & summary within a date range") 
        print("3. Exit\n")
        
        choice = input("Choose an option (1-3): ")
        
        if choice == '1':
            add()
        elif choice == '2':
            start_date = input("Enter start date (dd-mm-yyyy): ")
            end_date = input("Enter end date (dd-mm-yyyy): ")
            CSV.view_entries(start_date, end_date)
        elif choice == '3':
            print("Exiting the program.")
            break
        else:
            os.system('cls')
            print("Invalid choice. Please try again. Making sure to enter a number between 1 and 3.")
            time.sleep(3)


if __name__ == "__main__":
    main_menu()