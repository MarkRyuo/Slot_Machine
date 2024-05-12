import random 

# Global Variables 
MAX_LINES = 6 # CONST NOT CHANGEABLE // Global Variable 
MAX_BET = 100 
MIN_BET = 1

ROWS = 3
COLS = 3

symbol_count = {
    "A" : 2,
    "B" : 4,
    "C" : 6,
    "D" : 8
}
symbol_values = {
    "A" : 5,
    "B" : 4,
    "C" : 3,
    "D" : 1
}

def check_winnings(columns, lines, bet, values) :
    winnings = 0 
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns :
            symbol_to_check = column[line]
            if symbol != symbol_to_check :
                break
            else :
                winnings += values[symbol] * bet
                 
    return winnings 


#Understand logic here
def get_slot_machine_spin(rows, cols, symbols) :
    all_symbols = []
    for symbol, symbol_count in symbols.items() :
        for i in range(symbol_count):
            all_symbols.append(symbol)
    
    columns = []
    for col in range(cols) :
        column = []
        current_symbols = all_symbols[:]
        for row in range(rows) :
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)

        columns.append(column)
    return columns 

def print_slot_machine(columns) :
    for row in range(len(columns[0])) :
        for i, column in enumerate(columns):
            if i != len(columns) - 1 :
                print(column[row], end =" | ") 
            else:
                print(column[row], end ="")
            
        print()



def deposit() :
    while True :
        amount = input(
            "What would you like deposit? $"
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
            f"Enter a number of lines to bet on (1 - {MAX_LINES}): "
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
            "What would you like to bet? $"
            )
        if amount.isdigit() : #  It returns True if all characters in the string are digits (0-9) otherwise false 
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break # Kapag nilagay ay greater than 0 titigil na ang loop
            else :
                print(f"Amount must between ${MIN_BET} - ${MAX_BET}")
        else:
            print("Please enter a number")
    return amount


def main() :
    balance = deposit()
    lines = get_number_of_lines()
    
    while True :
        bet = get_bet()
        total_bet = bet * lines

        if total_bet > balance :
            print(
                f"You do not have enough to bet that amount, Your current balance is: ${balance}"
            )
        else :
            break
        
    print(f"You are betting ${bet} on {lines}. The total bet is equal to ${total_bet}")
    print(balance, lines)

    slots = get_slot_machine_spin(ROWS, COLS, symbol_count)
    print_slot_machine(slots)

main()