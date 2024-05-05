
def deposit() :
    while true :
        amount = input("What would you like deposit? $ ")
        if amount.isdigit() :
            amount = int(amount)
