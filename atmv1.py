accounts = []
def create_account(username, password):
    account = {"username": username,"password": password,"balance": 0,"history": []}
    return account
def deposit(account, amount):
    account["balance"] += amount
    account["history"].append("Deposited: " + str(amount))
def withdraw(account, amount):
    if account["balance"] >= amount:
        account["balance"] -= amount
        print("Your new balance: ", account["balance"])
        account["history"].append(f"withdrawed: {amount}")
        return True
    else:
        print("Insufficient balance")
        return False
def transfer(account, amount, receiver):
    success = withdraw(account, amount)
    if success:
        receiver["balance"] += amount
        receiver["history"].append("Received: " + str(amount))
        account["history"].append(f"Transfered: {amount} to {receiver['username']}")
    else:
        print("Invalid")
menu = ["1. Create account", "2. Login", "3. Logout"]
while True:
    for item in menu:
        print(item)
    item = input("Choose: ")
    if item == "1":
        username = input("Enter your username: ")
        password = input("Enter your password: ")
        new_account = create_account(username, password)
        accounts.append(new_account)
        print("Your account has been created!")
    elif item == "2":
        username = input("username: ")
        account_found = False
        for account in accounts:
            if username == account["username"]:
                account_found = True
                password = input("password: ")
                if password == account["password"]:
                    print("Success")
                    while True:
                        menu = ["1. Deposit", "2. Withdraw", "3. Transfer", "4. Exit"]
                        for item in menu:
                            print(item)
                        choice = input("Choose your option: ")
                        if choice == "1":
                            amount = int(input("Enter number: "))
                            deposit(account, amount)
                        elif choice == "2":
                            while True:
                                print(account["balance"])
                                amount = int(input("Enter number, 0 for quit: "))
                                if amount == 0:
                                    break
                                withdraw(account, amount)
                        elif choice == "3":
                            while True:
                                receiver_username = input("username, q for quit: ")
                                if receiver_username == "q":
                                    break
                                elif receiver_username == account["username"]:
                                    print("Invalid")
                                    continue
                                receiver_found = False
                                for receiver in accounts:
                                    if receiver_username == receiver["username"]:
                                        receiver_found = True
                                        amount = int(input("Enter number, 0 for quit: "))
                                        if amount == 0:
                                            break
                                        transfer(account, amount, receiver)
                                        break
                                if receiver_found == False:
                                    print("Receiver not found")
                        elif choice == "4":
                            break         
                else:
                    print("Wrong password")
        if account_found == False:
            print("Invalid username")
    elif item == "3":
        print("Log out")
        break