"""
Chandan Nir - 21/04/25 - 

This program simulates a Banking Application. It allows the users to:
- Signup or log into an existing account
- Choose between a chequing or savings account
- Deposit or Withdraw money
- View current balances
- View transaction history
- Transfer Funds between accounts
- Saves the users credenntials, and balance to the user.txt
- Saves the users transaction history into user_transacitons.txt

"""
import datetime
import os 
import time


# Used to exit the main loop when the user chooses to quit
quit = False

# Stores user credentials (username: password)
users = {
    "Chandan": "nir"
}

# Stores each user's chequing and savings balances
user_balances = {
    "Chandan" : {
        "chequing" : 1000.0,
        "savings" : 500.0
    }
}

# Stores a history of all transactions (per user and account)
transaction_history = {
    "Chandan":{
        "chequing" : [],
        "savings" : []
    }
}


# Loads the info from the file
def load_users_from_file():
    if not os.path.exists("user.txt"):
        return
    with open("user.txt", "r") as f:
        for line in f:
            parts = line.strip().split(",")
            if len(parts) == 4:
                user, passwords, chequing, savings = parts
                users[user] = passwords
                user_balances[user] ={
                    "chequing" : float(chequing),
                    "savings" : float(savings)
                }
                transaction_history[user]={
                    "chequing": [],
                    "savings":[]
                }
            
load_users_from_file()

# Stores users, balances, and history to .txt
def save_users_file():
    with open("user.txt", "w") as f:
        for user in users:
            chequing = user_balances[user]["chequing"]
            savings = user_balances[user]["savings"]
            password = users[user]
            f.write(f"{user},{password},{chequing},{savings}\n")

# Clears the UI
def clear_screen():
    os.system('clear')

# Prints out the text slowly, one char at a time 
def type_out(text, delay=0.05):
    for char in text:
        print(char, end="", flush=True)
        time.sleep(delay)
    print()

# Same as input(), but uses type_out()
def typed_input(prompt):
    type_out(prompt)
    return input("> ")

# Prompts the user to choose between 'chequing' or 'savings' account
def choose_account():
    while True:
        acct = input("Which account? (chequing/savings): ").lower()
        if acct in ["chequing","savings"]:
            return acct
        type_out("Please choose 'chequing' or 'savings'.")

# Used for signup
def signup():
    clear_screen()
    type_out("Welcome to the Signup Screen.")
    while True:
        new_user = input("Enter a Username: ")
        
        # Prevents dupes of usernames
        if new_user in users:
            type_out("Username already exists. Please try a different one.")
            continue
        new_password = input("Enter a Password: ")
        check_pass = input("Confirm Password: ")
        
        # Checks if passwords match
        if new_password != check_pass:
            type_out("Passwords do not match!")
            continue
        
        # Saves the credentials
        users[new_user] = new_password
        user_balances[new_user] = {"chequing": 1000.0, "savings": 500.0}
        transaction_history[new_user] = {"chequing": [], "savings": []}
        save_users_file()
        type_out("Signup Successful. Please Login in.")
        typed_input("Click Enter to continue: ")
        clear_screen()
        return

# Used for login
def login():
    clear_screen()
    while True:
        type_out("Welcome to the Login Screen.")
        user = input("Enter your Username: ")
        password = input("Enter your Password: ")
        
        # Checks if credentials match
        if user in users and users[user] == password:
            type_out(f"Welcome Back {user}!")
            print("""
                     ___________________________________
                     |#######====================#######|
                     |#(1)*UNITED STATES OF AMERICA*(1)#|
                     |#**          /===\   ********  **#|
                     |*# {G}      | (") |             #*|
                     |#*  ******  | /v\ |    O N E    *#|
                     |#(1)         \===/            (1)#|
                     |##=========ONE DOLLAR===========##|
                     ------------------------------------""")
            typed_input("Click Enter to continue: ")
            return user
            
        else:
            print("Incorrect username or password. Please try again.")
            return_to_signup = input("Go to Signup? ").lower()
            if return_to_signup == "yes":
                signup()

# Displays the initial screen with login/signup prompt 
def start_screen():
    clear_screen()
    type_out("Hello! Welcome to Bankify.")
    while True:
        account_login = typed_input("Login or Signup: ").lower()
        if account_login == "login":
            return login()
        elif account_login == "signup":
            signup()
        else: 
            print("Please choose Login or Signup.")

# Displays current balances
def view_bal(user_data):
    type_out(f"Chequing Balance: ${user_data['chequing']:.2f}")
    type_out(f"Savings Balance: ${user_data['savings']:.2f}")

# Displays transaction history
def view_history(username):
    type_out("Chequing History:")
    for item in transaction_history[username]["chequing"]:
        print("-", item)
    type_out("Saving History:")
    for item in transaction_history[username]["savings"]:
        print("-", item)
    
# Handles money withdrawal from 'chequing' and 'savings'
def withdrawal(user_data,username):
    clear_screen()
    account = choose_account()
    # Loop keeps going untill the user enter valid amount to withdraw
    while True:
        type_out(f"{account.upper()} Account: ")
        try:
            withdraw = float(input("How much would you like to withdrawal? "))
            
            # Checks if withdraw exceeds the limit
            if withdraw >= 500:
                type_out("Your amount exceeds the limit to Withdrawal, please try again.")
                continue
            if withdraw > user_data[account]:
                type_out("Insufficient funds.")
                continue
            
            # Deducts money and saves the transaction
            user_data[account] -= withdraw
            view_bal(user_data)
            time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            transaction_history[username][account].append(f"[{time}] Withdrew ${withdraw:.2f}")
            typed_input("Click Enter to Exit: ")
            save_users_file()
            return user_data
        except ValueError:
            type_out("Please enter a valid number.")

# Handles depositing money into 'chequing' and 'savings'
def deposit(user_data, username):
    clear_screen()
    account = choose_account()
    # Loop keeps going untill the user enter valid amount to deposit
    while True:
        type_out(f"{account.upper()} Account: ")
        try:
            deposit_amount = float(input("How much would you like to deposit? "))
            if deposit_amount < 0:
                type_out("You can not deposit negative money!")
                continue
            
            # Add money and save transaction
            user_data[account] += deposit_amount
            view_bal(user_data)
            time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            transaction_history[username][account].append(f"[{time}] Deposited ${deposit_amount:.2f}")
            typed_input("Click Enter to Exit: ")
            save_users_file()
            return user_data
        except ValueError:
            type_out("Please enter a valid number.")
    
# Displays all the options
def options():
    clear_screen()
    type_out("Your Options:")
    print("1. Withdrawal \n2. Deposit \n3. Balance \n4. History \n5. Transfer Funds \n6. Return to Start \n7.Quit")
    time.sleep(0.5)

# Allows the user to transfer money between savings and chequing
def transfer_funds(user_data,username):
    clear_screen()
    type_out("Transfer Funds Between Accounts")
    
    while True:
        from_account = choose_account()
        to_account = "chequing" if from_account == "savings" else "savings"
        type_out(f"Your transferring from {from_account.upper()} to {to_account.upper()}")
        try:
            amount = float(input("How much would you like to transfer? "))
            if amount <=0:
                type_out("Please enter a positive amount.")
                continue
            if amount > user_data[from_account]:
                type_out("Insufficient funds in source account.")
                continue
            
            user_data[from_account] -= amount
            user_data[to_account] += amount
            time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            transaction_history[username][from_account].append(f"[{time}] Transferred ${amount:.2f} to {to_account} account")
            transaction_history[username][to_account].append(f"[{time}] Recevied ${amount:.2f} from {from_account} account")
            view_bal(user_data)
            typed_input("Click Enter to Exit: ")
            save_users_file()
            return user_data
        except ValueError:
            type_out("Please enter a valid number.")

    
# Main program loop
def main(quit):
    while not quit:
        username = start_screen()
        if quit: 
            break
        
        # If the user doesn't exist yet, set their balances and history
        if username not in user_balances:
            user_balances[username] = {"chequing": 1000.0, "savings": 500.0}
        if username not in transaction_history:
            transaction_history[username] = {"chequing": [], "savings": []}
        try:
            while True:
                options()
                choice = typed_input("What would you like to do? (1-7): ")
                match choice:
                    case "1":
                        user_balances[username] = withdrawal(user_balances[username], username)
                    case "2":
                        user_balances[username] = deposit(user_balances[username],username)
                    case "3":
                        view_bal(user_balances[username])
                        typed_input("Click Enter to Exit: ")
                    case "4":
                        view_history(username)
                        typed_input("Click Enter to Exit: ")
                    case "5":
                        user_balances[username] = transfer_funds(user_balances[username], username)
                    case "6":
                        break # Takes you back to login/signup screen
                    case "7":
                        print("OK.")
                        time.sleep(3)
                        quit = True
                        break
                    case _:
                        print("Please put a valid choice. (1-7)")
                        time.sleep(2)
                        continue
        except ValueError:
            print("Please put a valid choice. (1-7)")
            
    clear_screen()
    type_out("Thank you, Goodbye")
    
if __name__ == "__main__":
    main(quit)