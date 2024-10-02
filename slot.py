import random

MAXLINES = 3
MAXBET = 100
MINBET = 1

ROWS = 3
COLS = 3

symbol_count = {
    "A" : 2,
    "B" : 4,
    "C" : 6,
    "D" : 8
}
symbol_value = {
    "A" : 5,
    "B" : 4,
    "C" : 3,
    "D" : 2
}
def check_win(coloumns, lines,bet, values):
    winnings = 0
    winning_lines = []
    for line in range(lines):
        symbol = coloumns[0][line]
        for coloumn in coloumns:
            symbol_to_check = coloumn[line]
            if symbol != symbol_to_check:
                break
        else:
            winnings += values[symbol] * bet
            winning_lines.append(line + 1)
    return winnings, winning_lines


def get_slotmachine_spin(rows, cols, symbols):
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        for i in range(symbol_count):
            all_symbols.append(symbol)
    
    coloumns = []
    for col in range(cols):
        coloumn = []
        current_symbols = all_symbols[:] # : = slice operator, creates a copy of the list
        for row in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            coloumn.append(value)
        
        coloumns.append(coloumn)

    return coloumns

def print_slotmachine(coloumns):
    for row in range(len(coloumns[0])):
        for i, coloumn in enumerate(coloumns):
            if i != len(coloumns) - 1:
                print(coloumn[row], end = " | ")
            else:
                print(coloumn[row])

def deposit():
    while True:
        amount = input("How much would you like to deposit? £  ")
        if amount.isdigit():
            amount = int(amount)
            if amount >0:
                break
            else:
                print("Amount must be greater than 0")
        else:
            print("Enter a number")
    return amount

def numlines():
    while True:
        lines = input(f"How many lines do you want to bet on (1-{MAXLINES})?  " )
        if lines.isdigit():
                lines = int(lines)
                if 1 <= lines <= MAXLINES:
                    break
                else:
                    print(f"Lines must be greater than 0 and less than {MAXLINES}")
        else:
            print("Enter a number")
    return lines

def getbet():
    while True:
        bet = input("How much would you like to bet on each line? $  ")
        if bet.isdigit():
            bet = int(bet)
            if MINBET <= bet <= MAXBET:
                break
            else:
                print(f"Bet must be between £{MINBET} and £{MAXBET}")
        else:
            print("Enter a number")
    return bet

def spin(balance):
    lines = numlines()
    while True:
        bet = getbet()
        totalbet = bet * lines
        if totalbet > balance: 
            print(f"You don't have enough balance to place this bet, your current balance is ${balance} ")
        else:
            break

    print(f"You are betting £{bet} on {lines} line(s). Total Bet = £{totalbet}")

    slots = get_slotmachine_spin(ROWS, COLS, symbol_count)
    winnings, winning_lines = check_win(slots,lines, bet,symbol_value)
    print_slotmachine(slots)
    print(f"You won £{winnings}")
    print(f"You won on lines", *winning_lines)

    return winnings - totalbet

def main():  
    balance = deposit()
    while True:
        print(f"Current Balance is £ {balance}")
        answer = input("Press enter to play (q to quit).")
        if answer == "q":
            break
        balance += spin(balance)

    print(f"You left with £{balance}")




main()
