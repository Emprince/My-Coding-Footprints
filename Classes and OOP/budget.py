import sys
class Budget:
    def __init__(self):
        pass

    # adds to total budget balance
    def add_balance(self):
        total_budget = int(input("Enter amount to add: "))
        print(">>>Updating Balance")
        category_balance['Total_balance'] += total_budget
        print(">>>Balance updated successfully<<<")
        print(f">>>Your balance is {category_balance['Total_balance']} ")

    # adds to specified category
    def deposit(self,budget_category):
        while True:
            add_money = int(input(f"How much do you want to add to {budget_category} Budget: "))

            # checks if the amount deposited is not higher than total balance
            if add_money <= category_balance['Total_balance']:
                category_balance[budget_category] = add_money
                print(f">>>Depositing {add_money} in {budget_category} Budget<<<")
                category_balance['Total_balance'] -= add_money
                print(">>>Deposit successful")
                print(f">>>Your total balance is remaining {category_balance['Total_balance']} ")
                break
            else:
                print(">>>You can't deposit amount higher than your Total Balance!\n")
                continue

    # withdraws from specific category
    def withdraw(self,budget_category):
        while True:
            withdraw_money = int(input(f"How much do you want to withdraw from {budget_category} Budget: "))
            if withdraw_money <= category_balance[budget_category]:
                category_balance[budget_category] -= withdraw_money
                print(f">>>Withdrawing {withdraw_money} from {budget_category} Budget<<<")
                category_balance['Total_balance'] += withdraw_money
                print(">>>Withdrawal successful")
                print(f">>>Your total balance is remaining {category_balance['Total_balance']} ")
                break
            else:
                print(">>>You can't withdraw amount higher than your Budget Balance!\n")
                continue

    # asks for two categories and transfers between them,user has to enter category name as input
    def transfer(self):
        while True:
            # just an attempt at error handling
            try:
                user_reply1 = input("Which category do you want to transfer from(e.g food): ")
                user_reply2 = input("Which category do you want to tansfer into(e.g food): ")
                if user_reply1.title() in category and user_reply2.title() in category:
                    amount = int(input("Enter amount to transfer: "))
                    category_balance[user_reply2.title()] += amount
                    print(">>>Updating Budget Balance<<<")
                    print(f">>>Your {user_reply2.title()}'s balance is now {category_balance[user_reply2.title()]}  ")
                    category_balance[user_reply1.title()] -= amount
                    print(f">>>Your {user_reply1.title()}'s balance is remaining {category_balance[user_reply1.title()]} ")
                    break
                else:
                    print(">>>Category not in Budget List")
                    continue
                
            except ValueError:
                print(">>>Invalid Input!,Try again!")
                continue

    # adds money to specified category
    def budget_balance(self,budget_category):
        print(f">>>Your {budget_category}'s balance is {category_balance[budget_category]} ")


###################################### Bunch of Functions ########################################
#ouputs the content of a list(category and options list)
def output_list(lists):
    counter = 1
    for option in lists:    
        print(f"{counter}.{option}")
        counter += 1

# asks the user to quit or go back
def return_button():
    while True:
        ask =  input(("Go back to Homepage?, Enter 'y' for yes or 'q' for no: "))
        if ask == 'q' or 'q'.upper():
            sys.exit
            break
        elif ask == 'y' or 'y'.upper():
            home_page()
        else:
            print(">>>Invalid Input!, Try again!")
            continue


# output the respective pages
def deposit_page():
    print("\n***************Deposit Page***********")
    print(">>>Budget Categories: ")
    # lists out the budget categories
    output_list(category)

    while True:
        user_choice = int(input("Enter an option to deposit in the category: "))
        user_list = []
        for i in range(len(category)+1):
            user_list.append(i) 
        if user_choice == 0:
            print(">>>Invalid option, Try again!")
            continue
        elif user_choice in user_list:              #finds out the category and works on it
            my_budget.deposit(category[user_choice-1])
            break
        else:
            print(">>>Invalid options, Try again!")
            continue

def withdraw_page():
    print("\n***************Withdrawal Page***********")
    print(">>>Budget Categories: ")
    # lists out the budget categories
    output_list(category)

    while True:
        user_choice = int(input("Enter an option to deposit in the category: "))
        user_list = []
        for i in range(len(category)+1):
            user_list.append(i) 
        if user_choice == 0:
            print(">>>Invalid option, Try again!")
            continue
        elif user_choice in user_list:              #finds out the category and works on it
            my_budget.withdraw(category[user_choice-1])
            break
        else:
            print(">>>Invalid options, Try again!")
            continue

def balance_page():
    print("\n***************Balance Page***********")
    print(">>>Budget Categories: ")
    # lists out the budget categories
    output_list(category)

    while True:
        user_choice = int(input(">>>Enter an option to check balance: "))
        user_list = []
        for i in range(len(category)+1):
            user_list.append(i) 
        if user_choice == 0:
            print(">>>Invalid option, Try again!")
            continue
        elif user_choice in user_list:              #finds out the category and works on it
            my_budget.budget_balance(category[user_choice-1])
            break
        else:
            print(">>>Invalid options, Try again!")
            continue

def home_page():
    print("\n***************Budget Operations Page***********")
    print(f">>>Your total balance is {category_balance['Total_balance']} ")
    # prints out the options and ask user to choose 
    output_list(options)
    user_reply = int(input('\n>>>Enter an option: '))
    if user_reply == 1:
        my_budget.add_balance()
        return_button()

    elif user_reply == 2:
        deposit_page()
        return_button()
        
    elif user_reply == 3:
        withdraw_page()
        return_button()
                
    elif user_reply == 4:
        print("\n***************Transfer Page***********")
        print(">>>Budget Categories: ")

        # lists out the budget categories and do the transfer operation
        output_list(category)
        my_budget.transfer()
        return_button()

    elif user_reply == 5:
        balance_page()
        return_button()

    elif user_reply == 6:
        user_reply = input("Enter Budget Category(e.g food): ")
        category.append(user_reply.title())
        print(category)
        return_button()

    elif user_reply == 7:
        print(">>>Budget list: ")
        print(category)
        return_button()

    elif user_reply == 8:
        sys.exit()
    else:
        print(">>>Invalid Input!")
        sys.exit()

################################################ Main Code ####################################################

category = ['Food', 'Clothing', 'Entertainment']
options = ['Add Balance', 'Deposit', 'Withdraw', 'Transfer', 'Balance', 'Add Budget', 'Budget List', 'Quit']
category_balance = {'Total_balance': 2000,
                    'Food': 1000,
                    'Clothing': 200,
                    'Entertainment': 0 
                    }
my_budget = Budget()
home_page()
