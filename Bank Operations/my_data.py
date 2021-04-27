import random
import os



# contains all fucntions that interact with the database

# lists out the user records 
users_list = os.listdir("database")

# generate account number
def acc_no():
    account_no = random.randrange(1000000000,9999999999)
    return account_no

user_db_path = "database/"


# checks if the user exists
def check_user(account_no):
    try:
        f = open(f"{user_db_path}/{account_no}.txt", "r")
            
    except FileExistsError:
        return False

    else:
        f.close()
        return True

def login_validation(account_no, password):
    try:
        f = open(f"{user_db_path}/{account_no}.txt", "r")  

    except FileNotFoundError:
        return False
    
    else:
        details = f.readlines()
        
        if password == details[4].strip():
            f.close()
            return True
            

        else:
            return False
        

def get_username(account_no):
    f = open(f"{user_db_path}/{account_no}.txt", "r")
    line = f.readlines()
    s_name = line[0]
    l_name = line[1]
    username = f"{s_name.strip().title()} {l_name.strip().title()}"
    f.close()
    return username


# create a user record
def create(account_no, user_details):
    account_not_exist = True
    while account_not_exist:
        try:
            f = open(f"{user_db_path}/{account_no}.txt", "x")
            
        except FileExistsError:
            acc_no()
            account_not_exist = False
        else:
            
            for detail in user_details:
                f.writelines(f"{detail} \n")
            f.close()
        

# read a file    
def read(account_no):
    check_user(account_no)
    f = open(f"{user_db_path}/{account_no}.txt", "r")
    print(f.readlines())
    f.close()


# update a file
# updates the password
def update(account_no, new_password):
    f = open(f"{user_db_path}/{account_no}.txt", "r")
    updated_line = f.readlines()
    updated_line[4] = f"{new_password}"

    f = open(f"{user_db_path}/{account_no}.txt", "w")
    f.writelines(updated_line)
    f.close()


# delete a file
def delete(account_no):
    try:
        os.remove(f"{user_db_path}/{account_no}.txt")  

    except FileNotFoundError:
        print(">>>User does not exist")
    
    else:
        print(">>>User removed successfully")
