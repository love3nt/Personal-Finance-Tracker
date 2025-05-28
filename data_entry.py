# Will collect data from the user, validate it, and then pass it to the database module for storage.

from datetime import datetime

date_format = "%d-%m-%Y"
CATEGORIES = {
    'I': 'Income',
    'E': 'Expense'
}

# Get user input for date, with an option to allow the user to hit enter for today's date.
def get_date(prompt, allow_default=False):
    date_str = input(prompt)
    if allow_default and not date_str:
        return datetime.today().strftime(date_format)
    
    # If the user provides a date, validate it.
    try:
        valid_date = datetime.strptime(date_str, date_format)
        return valid_date.strftime(date_format)
    except ValueError:
        print(f"Invalid date format. Please use '{date_format}'.")
        return get_date(prompt, allow_default)
    
# Get user input for amount.    
def get_amount():
    try:
        amount = float(input("Enter the amount: "))
        if amount <= 0:
            raise ValueError("Amount must be greater than zero and non-negative.")
        return amount
    except ValueError as e:
        print(e)
        return get_amount()


# Get user input for category.
def get_category():
    category = input("Enter the category ('I' Income or 'E' Expense):")
    category = category.upper()

    if category in CATEGORIES:
        return CATEGORIES[category]

    print(f"Invalid category '{category}'. Please enter 'I' for Income or 'E' for Expense.")
    return get_category()

# Get user input for description.
def get_description():
    description = input("Enter a description (optional): ")
    return description