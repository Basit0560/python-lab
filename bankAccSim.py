balance = 0

def deposit(amount):
    global balance
    balance += amount

def withdraw(amount):
    global balance
    if amount <= balance:
        balance -= amount
    else:
        print("Insufficient balance")

deposit(5000)
withdraw(2000)
print("Balance:", balance)