balance = 1000
def withdraw(balance, b):
                return balance - b
def deposit(balance, b):
                return balance + b
def check_balance(balance):
      print(balance)
menu = ["1. Check Balance", "2. Deposit", "3. Withdraw", "4. Exit"]
while True:
    for task in menu:
        print(task)
    choice = input("Choose option: ")
    if choice == "2":
        while True:
            a = int(input("Enter amount, 0 for quit: "))
            if a == 0:
                break
            balance = deposit(balance, a)
    elif choice == "1":
        check_balance(balance)
    elif choice == "3":
        while True:
            b = int(input("Enter amount, 0 for quit: "))
            if b == 0:
                break
            elif b > balance:
                print("Invalid")
            elif b <= balance:
                balance = withdraw(balance, b)
    elif choice == "4":
        break