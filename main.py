
def deposit() :
    while True :
        amount = input("What would you like deposit? $ ")
        if amount.isdigit() : #  It returns True if all characters in the string are digits (0-9) otherwise false 
            amount = int(amount)
            if amount > 5 :
                break # Kapag nilagay ay greater than 0 titigil na ang loop
            else :
                print("Amount must be greater than 5.")
        else:
            print("Please enter a number")
    return amount

deposit()



