![status](https://img.shields.io/badge/status-WIP-yellow)


# Personal Finance Tracker

A simple and efficient **Python-based personal finance tracker** that lets you log, store, and analyze all your income and expenses in a `.csv` file. Manage your transactions, track spending, and generate summaries for any date range—all from the command line.

---

## 🚀 Features

- **Add Transactions**: Log both income and expenses quickly.
- **View Transactions**: Display a list of all transactions, with filtering options.
- **Date Range Summary**: See totals for income, expenses, and net balance for any selected period.
- **CSV Storage**: All data is safely stored in a `.csv` file for easy access and backup.
- **Simple CLI Interface**: User-friendly prompts and commands.
- **Visualize Your Data**: Using matplotlib, you will be able to graph your expenses straight from the CLI.

---

## 📦 Installation

1. **Clone the repository:**
    ```bash
    git clone https://github.com/love3nt/Personal-Finance-Tracker.git
    cd personal-finance-tracker
    ```

2. **(Optional) Create and activate a virtual environment:**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

3. **Install requirements (if any):**
    ```bash
    pip install -r requirements.txt
    ```

---

## 🛠️ Usage

1. **Run the application:**
    ```bash
    python main.py
    ```

2. **Follow on-screen prompts to:**
    - Add a new transaction
    - View all transactions
    - Generate a summary within a chosen date range

---

## 📁 Data Format

Transactions are stored in a CSV file, e.g. `transactions.csv`, with the following columns:
- **Date** (YYYY-MM-DD)
- **Amount**
- **Category** (Income/Expense)
- **Description** (optional)


Example row:
```
2025-05-27,1100.0,Income,Salary
2025-05-28,250.0,Income,Freelance Work
2025-05-29, 1000.0,Expense,Bills
```

---

## 📝 Planned Features

- Category-based analytics
- Export to Excel or PDF
- Graphs/charts for spending trends
- Budget setting and alerts

---

## 🙌 Acknowledgments

- Python’s built-in CSV and datetime libraries
- Inspiration from the open-source community

---
