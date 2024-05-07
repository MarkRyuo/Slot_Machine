MAX_LINES = 6 # CONST NOT CHANGEABLE // Global Variable 
MAX_BET = 100 
MIN_BET = 1


def deposit() :
    while True :
        amount = input(
            "What would you like deposit? $ "
            )
        if amount.isdigit() : #  It returns True if all characters in the string are digits (0-9) otherwise false 
            amount = int(amount)
            if amount > 5 :
                break # Kapag nilagay ay greater than 0 titigil na ang loop
            else :
                print("Amount must be greater than 5.")
        else:
            print("Please enter a number")
    return amount

def get_number_of_lines() :
    while True :
        lines = input(
            f"Enter a number of lines to bet on (0 - {MAX_LINES}): "
        )
        if lines.isdigit() : 
            lines = int(lines)
            if 0 <= lines <= MAX_LINES :
                break 
            else :
                print("Enter a valid lines")
        else:
            print("Please enter a number")
    return lines 

def get_bet() :
    while True :
        amount = input(
            "What would you like to bet? $   "
            )
        if amount.isdigit() : #  It returns True if all characters in the string are digits (0-9) otherwise false 
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break # Kapag nilagay ay greater than 0 titigil na ang loop
            else :
                print("Amount must between.")
        else:
            print("Please enter a number")
    return amount


def main() :
    balance = deposit()
    lines = get_number_of_lines()
    print(balance, lines)


main()



