
def deposit() :
    while true :
        amount = input("What would you like deposit? $ ")
        if amount.isdigit() :
            amount = int(amount)
            if amount > 0 :
                break
            else :
                print("Amount must be greater than 0.")
