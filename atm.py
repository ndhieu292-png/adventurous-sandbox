balance = 1000
def withdraw(balance, b):
                return balance - b
def add(balance, b):
                return balance + b
while True:
    menu = ["1. Check Balance", "2. Deposit", "3. Withdraw", "4. Exit"]
    for task in menu:
        print(task)
    choice = input("Choose option: ")
    if choice == "2":
        while True:
            b = int(input("Enter amount, 0 for quit: "))
            if b == 0:
                break
            balance = add(balance, b)
    if choice == "1":
        print(balance)
    if choice == "3":
        while True:
            b = int(input("Enter amount, 0 for quit: "))
            if b == 0:
                break
            elif b > balance:
                print("Invalid")
            elif b <= balance:
                balance = withdraw(balance, b)
    if choice == "4":
        break