import csv
from datetime import datetime
def read_transactions():
    try:
        with open('transactions.csv', mode='r') as file:
            reader = csv.reader(file, delimiter='|')
            transactions = [row for row in reader]
        return transactions
    except FileNotFoundError:
        return []
    
def save_transaction(transaction):
     with open('transactions.csv', mode='a', newline='') as file:
        writer = csv.writer(file, delimiter='|')
        writer.writerow(transaction)

def home_screen():
    print("Home Screen")
    print("[D] Add Deposit")
    print("[P] Make Payment (Debit)")
    print("[L] Ledger")
    print("[X] Exit")
    choice = input("Choose an option: ").upper()
    return choice

def ledger_screen():
    print("Ledger Screen")
    print("[A] All Entries")
    print("[D] Deposits")
    print("[P] Payments")
    print("[H] Home")
    choice = input("Choose an option: ").upper()
    return choice

def display_ledger(transactions, filter_type=None):
    if filter_type == 'A':
        filtered_transactions = transactions
    elif filter_type == 'D':
        filtered_transactions = [t for t in transactions if float(t[4]) > 0]
    elif filter_type == 'P':
        filtered_transactions = [t for t in transactions if float(t[4]) < 0]
    else:
        filtered_transactions = []

    if filtered_transactions:
        for t in filtered_transactions:
            print(f"Date: {t[0]}, Time: {t[1]}, Description: {t[2]}, Vendor: {t[3]}, Amount: {t[4]}")
    else:
        print("No transactions to display.")

def add_deposit():
    description = input("Enter deposit description: ")
    vendor = input("Enter vendor: ")
    amount = float(input("Enter deposit amount: "))
    now = datetime.now()
    transaction = [now.strftime('%Y-%m-%d'), now.strftime('%H:%M:%S'), description, vendor, str(amount)]
    save_transaction(transaction)
    print("Deposit added successfully!")

def make_payment():
    description = input("Enter payment description: ")
    vendor = input("Enter vendor: ")
    amount = float(input("Enter payment amount: "))
    now = datetime.now()
    transaction = [now.strftime('%Y-%m-%d'), now.strftime('%H:%M:%S'), description, vendor, str(-amount)]
    save_transaction(transaction)
    print("Payment added successfully!")
def main():
    while True:
        choice = home_screen()

        if choice == 'D':
            add_deposit()
        elif choice == 'P':
            make_payment()
        elif choice == 'L':
            while True:
                transactions = read_transactions()
                ledger_choice = ledger_screen()
                
                if ledger_choice == 'A':
                    display_ledger(transactions, 'A')
                elif ledger_choice == 'D':
                    display_ledger(transactions, 'D')
                elif ledger_choice == 'P':
                    display_ledger(transactions, 'P')
                elif ledger_choice == 'H':
                    break
        elif choice == 'X':
            print("Exiting application...")
            break
        else:
            print("Invalid choice, please try again.")
if __name__ == "__main__":
    main()


