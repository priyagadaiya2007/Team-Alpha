# -------------------------------
# ATM Transaction System
# -------------------------------

customer_name = "Rahul Sharma"
atm_pin = "1234"
balance = 20000

print("=" * 40)
print("        WELCOME TO ATM")
print("=" * 40)

name = input("Enter Customer Name: ")
pin = input("Enter ATM PIN: ")

if name == customer_name and pin == atm_pin:

    print(f"\nWelcome, {customer_name}!")

    while True:
        print("\n========== MENU ==========")
        print("1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Exit")

        choice = input("Enter Your Choice: ")

        if choice == "1":
            print(f"\nCurrent Balance: ₹{balance}")

        elif choice == "2":
            amount = float(input("Enter Deposit Amount: ₹"))

            if amount > 0:
                balance += amount
                print("Deposit Successful!")
                print(f"Updated Balance: ₹{balance}")
            else:
                print("Invalid Amount!")

        elif choice == "3":
            amount = float(input("Enter Withdrawal Amount: ₹"))

            if amount > 5000:
                print("Sorry! You cannot withdraw more than ₹5000 in one transaction.")

            elif amount > balance:
                print("Insufficient Balance!")

            elif amount <= 0:
                print("Invalid Amount!")

            else:
                balance -= amount
                print("Please Collect Your Cash.")
                print(f"Remaining Balance: ₹{balance}")

        elif choice == "4":
            print("\nThank you for using our ATM.")
            break

        else:
            print("Invalid Choice!")

else:
    print("\nInvalid Customer Name or ATM PIN!")
