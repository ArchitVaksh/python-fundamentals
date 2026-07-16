balance = 1000
while True:
    print("""
    ====== ATM ======

    1. Check Balance
    2. Deposit
    3. Withdraw
    4. Exit""")
    user_input = int(input("Choose an option: "))
    if user_input == 1:
        print(f"Your balance is: Rs {balance}")
    elif user_input == 2:
        deposit = int(input("Enter amount to deposit: "))
        balance = balance + deposit
        print(f"Your balance is: Rs {balance}")
    elif user_input == 3:
        withdraw = int(input("Enter amount to withdraw: "))
        if withdraw <= balance:
            balance = balance - withdraw
            print(f"Your balance is now: Rs {balance}")
        else:
            print("Insufficient Balance")
    elif user_input == 4:
        print("Thank you for using ATM")
        break
    else:
        print("Invalid option. Please try again!")