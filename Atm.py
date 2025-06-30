balance = 6670
def check_balance():
    print("Your balance is:", balance)
def deposit(amount):
    global balance
    balance += amount
    print("Deposited:", amount)
def withdraw(amount):
    global balance
    if amount > balance:
        print("Not enough balance")
    else:
        balance -= amount
        print("Withdrawn:", amount)
check_balance()
deposit(1500)
withdraw(2170)
check_balance()