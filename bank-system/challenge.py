from datetime import datetime

# Constants

MENU = """
[d] Deposit
[s] Withdraw
[e] Statement
[h] Transaction History
[q] Quit
=> """

INITIAL_BALANCE = 0
WITHDRAW_LIMIT = 500
WITHDRAW_LIMIT_COUNT = 3

# Global variables

balance = INITIAL_BALANCE
statement = ""
withdraw_count = 0
transactions = []

# Function to Make a Deposit

def make_deposit():
    amount = float(input("Enter the deposit amount: "))
    if amount > 0:
        global balance, statement, transactions
        balance += amount
        statement += "Deposit: ${:.2f}\n".format(amount)
        transactions.append({"date": datetime.now(), "type": "Deposit", "amount": amount})
    else:
        print("Operation failed! The entered value is invalid.")

# Function to Make a Withdrawal

def make_withdrawal():
    global balance, statement, withdraw_count
    amount = float(input("Enter the withdrawal amount: "))
    exceeded_balance = amount > balance
    exceeded_limit = amount > WITHDRAW_LIMIT
    exceeded_withdraw_count = withdraw_count >= WITHDRAW_LIMIT_COUNT
    transactions.append({"date": datetime.now(), "type": "Withdrawal", "amount": amount})

    if exceeded_balance:
        print("Insufficient balance.")
    elif exceeded_limit:
        print("Withdrawal exceeds the limit. Please try again with a smaller amount.")
    elif exceeded_withdraw_count:
        print("Maximum number of withdrawals exceeded.")
    elif amount > 0:
        balance -= amount
        statement += "Withdrawal: ${:.2f}\n".format(amount)
        withdraw_count += 1
    else:
        print("The entered value is invalid.")

# Function to Display the Account Statement

def show_statement():
    print("\n================ STATEMENT ================")
    print("No transactions have been made." if not statement else statement)
    print("Balance: ${:.2f}".format(balance))
    print("============================================")

# Function to Show Transaction History

def show_transaction_history():
    print("\n========== TRANSACTION HISTORY ==========")
    for transaction in transactions:
        date = transaction["date"].strftime("%d/%m/%Y %H:%M:%S")
        type = transaction["type"]
        amount = transaction["amount"]
        print(f"{date} - {type}: ${amount:.2f}")
    print("=========================================")

# Main Loop

while True:
    option = input(MENU)

    if option == "d":
        make_deposit()

    elif option == "s":
        make_withdrawal()

    elif option == "e":
        show_statement()

    elif option == "h":
        show_transaction_history()

    elif option == "q":
        break

    else:
        print("Invalid operation, please select the desired operation again.")
