
def deposit() :
    while True :
        amount = input("What would you like deposit? $ ")
        if amount.isdigit() : # isdigit is checking 
            amount = int(amount)
            if amount > 0 :
                break # Kapag nilagay ay greater than 0 titigil na ang loop
            else :
                print("Amount must be greater than 0.")
        else:
            print("Please enter a number")
    return amount

deposit()
