# This file will handle the main flow of the program.

# Import necessary modules
import pandas as pd
import csv
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
        print(f"Entry added successfully: {new_entry}")

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


          
def add():
    CSV.initialize_csv()
    date = get_date("Enter the date (dd-mm-yyyy) or press Enter for today's date: ", allow_default=True)
    amount = get_amount()
    category = get_category()
    description = get_description()
    CSV.add_entry(date, amount, category, description)

