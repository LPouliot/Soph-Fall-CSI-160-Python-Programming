# Reviewing how to work with functions
def get_info():
    name = input("Enter your name: ")
    pswd = input("What is your password: ")
    bank_acct = input("What is your bank account number: ")
    showData(name,pswd,bank_acct)

customer = []

def tryAgain():
    print("The process is finished, data saved.")
    x = input('Do you want to add another account? (y/n): ')
    if x == 'y':
        get_info()
    else:
        print("Goodbye")
        exit()
def showData(name, pswd, bank_acct,):
    print("Hello", name,"Thank you for your information.")
    print("We are adding your intel to our dataset.")
    customer.append([name,pswd,bank_acct]) # Nested List
    """
    ## Creates a simple list ##
    
    customer.append(name)
    customer.append(pswd)
    customer.append(bank_acct)
    """
    save_customer_data = tuple(customer) # saves the next list as a tuple
    print("Please confirm we have the right data")
    print("Your full name:", name)
    print("Your password:", pswd)
    print("Bank account number:",bank_acct)
    print(customer)
    print(save_customer_data)
    tryAgain()

get_info()


