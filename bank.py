
#library for generating random numbers(used in generating random account numbers)
from random import randint


#Dictionary which stores all the user accounts
accounts = {}

# It's where the total money is stored
vault = 0


def deposit(vault, accounts): #Function fo all deposit functions

    try:
        
        acc = int(input("Enter account number: "))

    except ValueError:

        print("\nInvalid value: use numbers 0-9.")

        return vault

    if acc in accounts:

        try:

            dep = int(input("Enter deposit amount: "))

        except ValueError:
            print("Invalid amount, use digits 0-9.")

            return vault


        passwrd = input("Enter account password: ")

        if passwrd == accounts[acc]["password"]: #Checks if password is correct


            vault += dep  # Updated the vault
            accounts[acc]["balance"] += dep   # Updated the user's acount balance

            print(f"\nYour amount of Ksh{dep} has been deposited successfully.\n")
        else: 

            print("Incorrect password.")

    else:
        print("\nAccount doesn't exist.")


    return vault


def withdraw(vault, accounts): #Function for withdrawing

    try:

        acc = int(input("Enter your account number: "))

    except ValueError:

        print("Incorrect account number. Use digits 0-9.")

        return vault

    if acc in accounts:  #Condition for checking account and witdrawing amounts
        pin = input("Enter your password: ")

        if pin == accounts[acc]["password"]:

            try:
                withd = int(input("Enter withdraw amount: "))
            except ValueError:
                print("Incorrect amount, use digits.")

                return vault


            if accounts[acc]["balance"] >= withd:

                print(f"\nWithdrawal of Ksh {withd} successful.\n")


                accounts[acc]["balance"] -= withd
                vault -= withd


                return vault


            elif accounts[acc]["balance"] < withd:

                print(f"Amount Ksh{withd} is greater than bank balance.\n")

                return vault
        else:
            print("Your password is incorrect.")

            return vault

    else:
        print("\nAccount doesn't exist.")

        return vault



def create_account(vault, accounts):  #Function for creating

    print("--------ACCOUNT CREATION--------")

    while True:  # Loop for entering name
        name_1 = input("Enter your first name: ")

        if name_1.strip().isalpha():   # Checks if the names contain any numbers
            break
        else:
            print("Name must contain letters only.")

    while True:
        name_2 = input("Enter your second name: ")

        if name_2.strip().isalpha():  # Checks if the names contain any numbers
            break
        else:
            print("Name must contain letters only.")


    while True: # Loop for entering ID number

        try:

            id = int(input("Enter your ID number(exactly 5 digits): "))

            if 10000 <= id <= 99999:   #Checks id ID number is > or <  five characters
                break

            else:
                print("ID number must be exactly 5 digits.")


        except ValueError:
            print("ID number must contain numbers only.")



    password = input("Enter a strong password: ")


    while True: # Loop for entering deposit

        try:

            balance = int(input("Enter your first deposit: "))

            if balance > 0:
                break

            else:
                print("Deposit must be greater than 0.")

        except ValueError:
            print("Ivalid value. Use digits 0-9.")


    while True:  # Generation of random account numbers

        acc_num = randint(1000, 5000)

        if acc_num not in accounts:   # Checks whether account number generated already exists
            break


    # Generation of a user account
    accounts[acc_num] = {

            "name": name_1 + " " + name_2,           
            "id": id,
            "password": password, 
            "balance": balance

            }


    vault += balance   # Amount in vault is updated


    print("\n Account created successfully.")
    print(f"\n Your account number is {acc_num}.")


    return vault




def check_balance(accounts): # Function for checking balance

    try:   # Error handling of ValueErrors(incorrect account numbers:digits)

        acc = int(input("Enter account number: "))

    except ValueError:

        print("Account number should be writted in digits 0-9.")

        return 

    if acc in accounts:
        passwrd = input("Enter your password: ")

        if passwrd == accounts[acc]["password"]:

            print(f"\nYour balance is Ksh {accounts[acc]["balance"]}.")

        else:
            print("\nYour password is incorrect.")

    else:
        print("\nYour account doesn't exist.")

    

# Loop whick runs the program
while True:

    print("""
        -------BANK-------\n
        1. Deposit
        2. Withdraw
        3. Check balance
        4. Create account
        5. Exit\n
        """)

    choice = input("Enter your choice: ")



    if choice == "1":
        vault = deposit(vault, accounts)
    elif choice == "2":
        vault = withdraw(vault, accounts)
    elif choice == "3":
        check_balance(accounts)
    elif choice == "4":
        create_account(vault, accounts)
    elif choice == "5":
        break;
    else:
        print("Invalid choice")


