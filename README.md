# Finance Tracker

A simple command-line expense tracker written in Python.  
Track your expenses, categorize them, and see summaries to help manage your budget.

## Features

- Add expenses with name, amount, and category
- Save expenses to a CSV file
- Summarize expenses by category
- See total spent, budget left, and daily budget
- Table output for easy viewing

## Requirements

- Python 3.7+
- [tabulate](https://pypi.org/project/tabulate/) library

Install dependencies:
```
pip install tabulate
```

## Usage

1. Run the tracker:
    ```
    python expense_tracker.py
    ```
2. Enter your budget when prompted.
3. Add expenses by entering their name, amount, and selecting a category.
4. View a summary table and budget analysis after each entry.

## File Structure

- `expense_tracker.py` — Main program
- `expenses.py` — Expense class
- `expenses.csv` — Saved expenses

## Example

```
Running expense tracker!
Enter your budget: 500
Getting user expense
Enter expense name: Lunch
Enter expense amount: 12.5
Select a category:
1. Food
2. Home
3. Work
4. Fun
5. Misc
Enter category number [1- 5]: 1
Saving user expense: Expense(name='Lunch', amount=12.5, category='Food') to expenses.csv
Summarising user expense
+--------+---------+----------+
| Name   | Amount  | Category |
+--------+---------+----------+
| Lunch  | $12.50  | Food     |
+--------+---------+----------+
Expenses by category:
Total for Food: $12.50
Good job! You are within your budget of $500.00
Total spent: $12.50
Budget left: $487.50
Remaining days in month: 27
Daily budget: $18.06
```

## License

MIT License
