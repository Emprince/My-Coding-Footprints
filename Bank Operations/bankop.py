import sys
import datetime
import my_data
today = datetime.datetime.now()
now = today.strftime("%I:%M%p %A,%B-%m-%y")
flag = True

#retries again if the password dont match
def check_pass():
    while True:

        passw = input("Enter Password: ")
        confirm_passw = input("Confirm your password: ")
        
        if passw == confirm_passw:
            return passw          
        
        else:
            print(">>>Passwords do not match,Try again!")
            continue


#get registration details
def reg():
    global account_no
    print("\n--------Registration Page-------%s" % now)
    
    s_name = input("Enter your Surname: ")
    l_name = input("Enter your Last name: ")
    email = input("Enter your Email: ")
    phone = input("Enter your Phone Number: ")
    password = check_pass()
    account_no = my_data.acc_no()
    user_details = [s_name.lower(), l_name.lower(), email.lower(), phone, password]                   #generates user account number
    
    #adds the details to the database and login
    print(">>>Registering...<<<")

    my_data.create(account_no, user_details)

    print(">>>Registration Successful!")
    print(f">>>Your account Number is {account_no}")
    print(">>>Keep it safe") 

    login()

#Login 
def login():
    print("\n--------Login Page-------%s" % now)

    redo = 0
    
    while True:
        global account_no
        account_no = input("Enter your Account Number: ")
        password = input("Enter your Password: ")

        is_logged_in = my_data.login_validation(account_no, password)

        if is_logged_in:
            print(">>>Logging in...<<<")
            print(">>>Login Successful!")
            home_page()
            break

        else:
            if redo < 2:                                                      #lets user try again
                print(">>>Username or Password incorrect,Try again!")
                redo += 1
                continue
        
            else:
                print(">>>You are out of Chances!")
                print(">>>Forgotten password?")
                ans = input(">>>Enter 1 to reset your password or q to quit: ")
        
                if ans == "1":
                    reset_passw()
        
                else:
                    init()

#logout
def logout():
    print(">>>Logging out...<<<")
    print(">>>Thank you for banking with us")
    init()

#resets your password
def reset_passw():
    # updates the file
    print("\n--------Password Reset Page-------%s" % now)
    
    while True:
        account_no = input("Enter your Account Number: ")

        user_exists = my_data.check_user(account_no)

        if user_exists == True:
            passw_reset = check_pass()

            print(">>>Resetting your password<<<")

            my_data.update(account_no, passw_reset)

            print(">>>Your Password reset is successful")
            
            login()

        else:
            print(">>>Account not found,Try again!")
            continue

               
#Initializes the index page
def init():
    index = {1: "Register",
             2: "Login",
             3: "Forgotten Password",
             4: "Quit"
             }
    
    print("\n--------Index Page-------%s" % now)
    print("********Welcome to Premier Bank**********")
    
    for key,value in index.items():                          #Lists the options available
        print(f"{key}.{value}")
    
    while True:
    
        choice = input("Select an option to continue(e.g 1): ")
    
        if choice == "1":
            reg()
            break
    
        elif choice == "2":
            login()
            break
    
        elif choice == "3":
            reset_passw()

        #Shuts down the system(i only put it there as a way to quit my code without error)
        elif choice == "4":
            sys.exit()
    
        else:
            print(">>>Invalid option selected,Try again!")
            continue

#asks the user if he wants to go back or logout
def que():
    print(">>>Do you want to go back to the Home page?")
    
    que = input("Enter 'y' for yes and 'n' for no: ")
    
    if que == "Y".lower():
        home_page()
    
    else:
        logout()

#Bank operations page
def home_page():
    while True:
        print("\n--------Home Page-------%s" % now)
    
        username = my_data.get_username(account_no)

        print(f">>>Welcome Back {username}!")  #prints out first and last name   
        print(f">>>Your Account Number is {account_no}")     
    
        options = {1: "Withdraw",                                 
            2: "Deposit",
            3: "Complaint",
            4: "Logout",
            }                                                                
    
        for key,value in options.items():
            print(f"{key}.{value}")
    
        select = input("Select an option to continue(e.g 1):  ")
    
        if select == "1": 
            print("\n--------Withdrawal Page-------%s" % now)
            ans = input("How much do you want to withdraw(e.g 10,000): ")
            print(">>>You are trying to withdraw ₦%s" % ans)
            print(">>>Withdrawal in process...<<<")
            print(">>>Take your cash!")            
            que()                                                             #goes back to index page
    
        elif select == "2":
            print("\n--------Cash Deposit Page-------%s" % now)
            dep = input("How much would you like to deposit(e.g 10,000): ")
            print(">>>Adding ₦%s to your account...<<<" % dep)
            print(">>>Your current balance is ₦%s" % dep)
            que()
    
        elif select == "3":
            print("\n--------Complaint Page-------%s" % now)
            report = input("What is your report: ")
            print(">>>Submitting your report...<<")
            print(">>>Thanks for your feedback!")
            que()
    
        elif select == "4":
            logout()
    
        else:
            print(">>>Invalid option selected,Try again!")
            continue   


##########################################Starts up the system##############################################
init()
