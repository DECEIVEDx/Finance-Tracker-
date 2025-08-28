
import os
from expenses import Expense
import calendar
import datetime
from tabulate import tabulate


def main():
    print(f"Running expense tracker!")
    budget = float(input("Enter your budget: "))
    script_dir = os.path.dirname(os.path.abspath(__file__))
    expense_file_path = os.path.join(script_dir, "expenses.csv")
    # Get user to input expense
    expense = get_user_expense()  
    
    # Write their expense to file
    save_expense_to_file(expense, expense_file_path)
    # Read file and summarise expenses
    summarise_expenses(expense_file_path, budget)

    pass

def get_user_expense():
    print(f"Getting user expense")
    expense_name = input("Enter expense name: ")
    expense_amount = float(input("Enter expense amount: "))
    expense_categories = [
        "Food",
        "Home",
        "Work",
        "Fun",
        "Misc",
    ]

    while True:
        print("Select a category: ")
        for i, category_name in enumerate(expense_categories):
            print(f"{i +1}. {category_name}")

        value_range = f"[1- {len(expense_categories)}]"
        try:
            selected_index = int(input(f"Enter category number {value_range}: ")) - 1
        except ValueError:
            print(f"Invalid input, please enter a number {value_range}")
            continue

        if selected_index in range(len(expense_categories)):
            select_category = expense_categories[selected_index]
            new_expense = Expense(
                name = expense_name, amount = expense_amount, category = select_category
                )
            return new_expense
        else:
            print(f"Invalid input, please enter a number {value_range}")


        

def save_expense_to_file(expense: Expense, expense_file_path):
    print(f"Saving user expense: {expense} to {expense_file_path}")
    with open(expense_file_path, "a") as f:
        f.write(f"{expense.name},{expense.amount},{expense.category}\n")



def summarise_expenses(expense_file_path, budget):
    print(f"Summarising user expense")
    expenses: list[Expense] = []
    with open(expense_file_path, "r") as f:
        lines = f.readlines()
        for line in lines:
            parts = line.strip().split(",")
            if len(parts) != 3:
                continue  # skip malformed lines
            expense_name, expense_amount, expense_category = parts
            line_expense = Expense(
                name=expense_name,
                amount=float(expense_amount),
                category=expense_category
            )
            expenses.append(line_expense)
    table = [[e.name, f"${e.amount:.2f}", e.category] for e in expenses]
    
    amount_by_category = {}
    for expense in expenses:
        key = expense.category
        if key in amount_by_category:
            amount_by_category[key] += expense.amount
        else:
            amount_by_category[key] = expense.amount
    

    show_table = input("Show summary table? (y/n): ").lower()
    if show_table == "y":
        print(tabulate(table, headers=["Name", "Amount", "Category"], tablefmt="grid"))
    
    show_graphs = input("Show graphs? (y/n): ").lower()
    if show_graphs == "y" and amount_by_category:
        # Bar chart
        import matplotlib.pyplot as plt
        categories = list(amount_by_category.keys())
        amounts = list(amount_by_category.values())
        plt.figure(figsize=(8, 5))
        plt.bar(categories, amounts, color='skyblue')
        plt.title('Expenses by Category')
        plt.xlabel('Category')
        plt.ylabel('Amount ($)')
        plt.tight_layout()
        plt.show()

        # Pie chart
        plt.figure(figsize=(6, 6))
        plt.pie(amounts, labels=categories, autopct='%1.1f%%', startangle=140)
        plt.title('Expense Distribution')
        plt.tight_layout()
        plt.show()


    print("Expenses by category:")
    for key, amount in amount_by_category.items():
        print(f"Total for {key}: ${amount:.2f}")

    total_spent = sum(expense.amount for expense in expenses)
    if total_spent > budget:
        print(f"Warning: You have exceeded your budget of ${budget:.2f} by ${total_spent - budget:.2f}")
    else:
        print(f"Good job! You are within your budget of ${budget:.2f}")
    print(f"Total spent: ${total_spent:.2f}")
    budget_left = budget - total_spent
    print(f"Budget left: ${budget_left:.2f}")
    now = datetime.datetime.now()
    days_in_month = calendar.monthrange(now.year, now.month)[1]
    # Calulate remaining days in month
    remaining_days = days_in_month - now.day
    print(f"Remaining days in month: {remaining_days}")
    daily_budget = budget_left / remaining_days if remaining_days > 0 else 0
    print(f"Daily budget: ${daily_budget:.2f}")

if __name__ == "__main__":
    main()