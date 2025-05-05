import json
from datetime import datetime

class FinancialPlanner:
    def __init__(self):
        self.transactions = []

    def add_transaction(self, amount, category, description):
        self.transactions.append({
            "amount": amount,
            "category": category,
            "description": description,
            "date": datetime.now().strftime("%Y-%m-%d")
        })

    def show_summary(self):
        income = sum(t["amount"] for t in self.transactions if t["amount"] > 0)
        expenses = sum(-t["amount"] for t in self.transactions if t["amount"] < 0)
        balance = income - expenses
        print(f"\nSummary:")
        print(f"Total Income:   ${income:.2f}")
        print(f"Total Expenses: ${expenses:.2f}")
        print("---------------------------------")
        print(f"Balance:        ${balance:.2f}\n")

    def show_all_transactions(self):
        if not self.transactions:
            print("\nNo transactions found.\n")
            return
        print("\nAll Transactions:")
        for t in self.transactions:
            print(f"{t['date']} | {t['category']} | {t['description']} | ${t['amount']:.2f}")
        print()

    def remove_transaction(self):
        if not self.transactions:
            print("\nNo transactions found.\n")
            return

        print("\nRemove Transaction:")
        for i, t in enumerate(self.transactions):
            print(f"{i + 1}. {t['date']} | {t['category']} | {t['description']} | ${t['amount']:.2f}")

        try:
            choice = int(input("\nSelect Transaction to remove: "))
            if 1 <= choice <= len(self.transactions):
                remove_check = input("\nAre you sure you want to remove this transaction? (y/n): ").strip().lower()
                if remove_check == "y":
                    removed = self.transactions.pop(choice - 1)
                    print(f"\nRemoved Transaction: {removed}")
            else:
                print("\nInvalid Selection\n")
        except ValueError:
            print("\nPlease enter a valid selection. \n")

    def save_to_file(self, filename="financial.txt"):
        with open(filename, "w") as f:
            for t in self.transactions:
                line = f"{t['date']} | {t['category']} | {t['description']} | ${t['amount']:.2f}\n"
                f.write(line)
        print("Data saved successfully.\n")

    def load_from_file(self, filename="financial.txt"):
        try:
            with open(filename, "r") as f:
                self.transactions = []
                for line in f:
                    parts = line.strip().split(" | ")
                    if len(parts) == 4:
                        date, category, description, amount_str = parts
                        amount = float(amount_str.replace("$", ""))
                        self.transactions.append({
                            "date": date,
                            "category": category,
                            "description": description,
                            "amount": amount
                        })
            print("Data loaded successfully from text file.\n")
        except FileNotFoundError:
            print("No data file found.\n")
        except Exception as e:
            print(f"Error loading data: {e}\n")

def main():
    planner = FinancialPlanner()
    planner.load_from_file()

    while True:
        print("$$$$--- Financial Planner Menu ---$$$$")
        planner.show_summary()
        print("1. Add Transactions")
        print("2. Show Transactions")
        print("3. Remove Transaction")
        print("4. Save Data")
        print("5. Load Data")
        print("6. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            transaction_type = input("Choose a transaction type. (1. Income 2. Expense): ")
            if transaction_type == "1":
                amount = float(input("Enter income amount: "))
                category = input("Enter category (e.g., Salary, Gift): ")
                description = input("Enter description: ")
                planner.add_transaction(amount, category, description)
                print("Income added.\n")
            elif transaction_type == "2":
                amount = float(input("Enter expense amount: "))
                category = input("Enter category (e.g., Food, Rent): ")
                description = input("Enter description: ")
                planner.add_transaction(-abs(amount), category, description)
                print("Expense added.\n")
        elif choice == "2":
            planner.show_all_transactions()
        elif choice == "3":
            planner.remove_transaction()
        elif choice == "4":
            planner.save_to_file()
        elif choice == "5":
            planner.load_from_file()
        elif choice == "6":
            confirm = input("Would you like to save before exiting? (y/n): ").strip().lower()
            if confirm == "y":
                planner.save_to_file()
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.\n")

if __name__ == "__main__":
    main()
