import textwrap
from datetime import datetime

def menu():
    menu_text = """\n=============== MENU ===============
[d] Deposit
[s] Withdraw
[e] Statement
[h] Transaction History
[nc] New Account
[lc] List Accounts
[nu] New User
[q] Quit
=> """

    return input(textwrap.dedent(menu_text))

# Deposit Function

def make_deposit(balance, value, statement, transactions, /):
    if value > 0:
        balance += value
        statement += f"Deposit:\tR$ {value:.2f}\n"
        print("\n=== Deposit successful! ===")
    else:
        print("\n@@@ Invalid value provided. @@@")
    transactions.append({"date": datetime.now(), "type": "Deposit", "value": value})
    return balance, statement

# Withdraw Function

def make_withdraw(*, balance, value, statement, limit, num_withdrawals, withdrawal_limit, transactions):
    exceeded_balance = value > balance
    exceeded_limit = value > limit
    exceeded_withdrawals = num_withdrawals >= withdrawal_limit
    transactions.append({"date": datetime.now(), "type": "Withdrawal", "value": value})

    if exceeded_balance:
        print("\n@@@ Operation failed! Insufficient balance. @@@")

    elif exceeded_limit:
        print("\n@@@ Operation failed! The withdrawal amount exceeds the limit. @@@")

    elif exceeded_withdrawals:
        print("\n@@@ Operation failed! Maximum number of withdrawals exceeded. @@@")

    elif value > 0:
        balance -= value
        statement += f"Withdrawal:\tR$ {value:.2f}\n"
        num_withdrawals += 1
        print("\n=== Withdrawal successful! ===")
    else:
        print("\n@@@ Invalid value provided. @@@")

    return balance, statement

# Show Statement Function

def show_statement(balance, /, *, statement):
    print("\n================ STATEMENT ================")
    print("No transactions were made." if not statement else statement)
    print(f"\nBalance:\tR$ {balance:.2f}")
    print("==========================================")

# Show Transaction History Function

def show_transaction_history(transactions):
    print("\n========== TRANSACTION HISTORY ==========")
    for transaction in transactions:
        date = transaction["date"].strftime("%d/%m/%Y %H:%M:%S")
        transaction_type = transaction["type"]
        value = transaction["value"]
        print(f"{date} - {transaction_type}: R$ {value:.2f}")
    print("=========================================")

# Create User Function

def create_user(users):
    cpf = input("Enter the CPF (numbers only): ")
    user = filter_user(cpf, users)

    if user:
        print("\n@@@ User with this CPF already exists! @@@")
        return

    name = input("Enter the full name: ")
    birth_date = input("Enter the date of birth (dd-mm-yyyy): ")
    address = input("Enter the address (street, number - neighborhood - city/state abbreviation): ")

    users.append({"name": name, "birth_date": birth_date, "cpf": cpf, "address": address})

    print("=== User created successfully! ===")

# Filter User Function

def filter_user(cpf, users):
    filtered_users = [user for user in users if user["cpf"] == cpf]
    return filtered_users[0] if filtered_users else None

# Create Account Function

def create_account(agency, account_number, users):
    cpf = input("Enter the user's CPF: ")
    user = filter_user(cpf, users)

    if user:
        print("\n=== Account created successfully! ===")
        return {"agency": agency, "account_number": account_number, "user": user}

    print("\n@@@ User not found, account creation process terminated! @@@")

# List Accounts Function

def list_accounts(accounts):
    for account in accounts:
        line = f"""\
            Agency:\t{account['agency']}
            A/C:\t\t{account['account_number']}
            Holder:\t{account['user']['name']}
        """
        print("=" * 100)
        print(textwrap.dedent(line))

# Main Function

def main():
    WITHDRAWAL_LIMIT = 3
    AGENCY = "0001"

    balance = 0
    limit = 500
    statement = ""
    num_withdrawals = 0
    users = []
    accounts = []
    transactions = []

    while True:
        option = menu()

        if option == "d":
            value = float(input("Enter the deposit amount: "))

            balance, statement = make_deposit(balance, value, statement, transactions)

        elif option == "s":
            value = float(input("Enter the withdrawal amount: "))

            balance, statement = make_withdraw(
                balance=balance,
                value=value,
                statement=statement,
                limit=limit,
                num_withdrawals=num_withdrawals,
                withdrawal_limit=WITHDRAWAL_LIMIT,
                transactions=transactions,
            )

        elif option == "e":
            show_statement(balance, statement=statement)

        elif option == "h":
            show_transaction_history(transactions)

        elif option == "nu":
            create_user(users)

        elif option == "nc":
            account_number = len(accounts) + 1
            account = create_account(AGENCY, account_number, users)

            if account:
                accounts.append(account)

        elif option == "lc":
            list_accounts(accounts)

        elif option == "q":
            break

        else:
            print("Invalid operation, please select the desired operation again.")

if __name__ == "__main__":
    main()
