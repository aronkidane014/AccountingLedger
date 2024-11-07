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