from icecream import ic
from typing import List, Dict, Tuple
import random

MAX_LINES = 3
MAX_BET = 100
MIN_BET = 10
ROWS = 3
COLS = 3

SYMBOL_COUNT = {
    "A" : 2,
    "B" : 4,
    "C" : 6,
    "D" : 8
}

SYMBOL_VALUES = {
    "A" : 5,
    "B" : 4,
    "C" : 3,
    "D" : 2
}

def check_winnings(columns: List[List[str]], lines: int, bet: int, values: Dict[str, int]) -> Tuple[int, List[int]]:
    """
    Check for winnings in the slot machine spin.

    Parameters:
    - columns (List[List[str]]): A 2D list representing the slot machine grid with symbols.
    - lines (int): The number of lines to bet on.
    - bet (int): The amount to bet on each line.
    - values (Dict[str, int]): A dictionary mapping symbols to their respective values.

    Returns:
    Tuple[int, List[int]]: A tuple containing the total winnings and a list of winning lines.
    """

    winnings = 0
    winning_lines = []

    for line in range(lines):
        symbol = columns[0][line]

        for column in columns:
            symbol_to_check = column[line]

            if symbol != symbol_to_check:
                break
        else:
            winnings += values[symbol] * bet
            winning_lines.append(line + 1)
    
    return winnings, winning_lines

def get_slot_machine_spin(rows: int, cols: int, symbols: Dict[str, int]) -> List[List[str]] :
    """
    Generate a slot machine spin result.

    Parameters:
    - rows (int): Number of rows in the slot machine grid.
    - cols (int): Number of columns in the slot machine grid.
    - symbols (Dict[str, int]): A dictionary mapping symbols to their respective counts.

    Returns:
    List[List[str]]: A 2D list representing the slot machine grid with symbols.
    """

    all_symbols = [symbol for symbol, SYMBOL_COUNT in symbols.items() for _ in range(SYMBOL_COUNT)]
    current_symbols = all_symbols[:]
    columns = [[current_symbols.pop(random.randint(0, len(current_symbols) - 1)) for _ in range(cols)] for _ in range(rows)]
    
    print_slot_machine(columns) 
    return columns

def print_slot_machine(columns: List[List[str]]) -> None:
    """
    Prints the slot machine in grid form

    Parameters:
    -columns (List[List[str]]): A 2D list representing the slot machine grid with symbols.
    """

    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            end_char = " | " if i != len(columns) - 1 else "\n"
            print(column[row], end=end_char)
        print()


def deposit() -> int:
    """
    Prompt the user to deposit an amount.

    Returns:
    int: The amount deposited by the user.
    """

    while True:
        amount = input("Enter the amount you want to deposit: $")

        if amount.isdigit():
            amount = int(amount)

            if amount > 0:
                break
            else:
                print("Please enter a value > 0")
        else: 
            print("Please enter an integer")

    return amount

def get_no_of_lines() -> int:
    """
    Prompt the user to enter the number of lines to bet on.

    Returns:
    int: The number of lines to bet on.
    """

    while True:
        lines = input(f"Enter the number of lines to bet on (1 - {MAX_LINES}):")
        
        if lines.isdigit():
            lines = int(lines)

            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("Please enter a valid number of lines.")
        else: 
            print("Please enter an integer")

    return lines

def get_bet() -> int:
    """
    Prompt the user to enter the amount to bet on each line.

    Returns:
    int: The amount to bet on each line.
    """

    while True:
        amt = input("Enter the amount to bet on each line: $")

        if amt.isdigit():
            amt = int(amt)

            if MIN_BET <= amt <= MAX_BET:
                break
            else:
                print(f"Amount must be between ${MIN_BET} and ${MAX_BET}.")
        else: 
            print("Please enter an integer")

    return amt

def spin(balance: int) -> int:
    """
    Execute a spin on the slot machine.

    Parameters:
    - balance (int): The current balance of the player.

    Returns:
    int: The new balance after the spin.
    """

    lines = get_no_of_lines()

    while True:
        bet = get_bet()
        total_bet = bet * lines

        if total_bet > balance:
            print(f"You do not have sufficent balance to place the bet.\n BALANCE : ${balance} \n REQUIRED AMOUNT : ${total_bet}")
        else:
            break

    print(f"\n You are betting: \n AMOUNT : ${bet} \n LINES : {lines} \n TOTAL BET : ${total_bet} \n")
    slots = get_slot_machine_spin(ROWS, COLS, SYMBOL_COUNT)
    winnings, winning_lines = check_winnings(slots, lines, bet, SYMBOL_VALUES)
    print(f"You won ${winnings}.")
    print("You won on lines: ", *winning_lines)
    return winnings - total_bet

def main() -> None:
    """
    Main function to run the slot machine game.
    """

    balance = deposit()
    while True:
        print(f"CURRENT BALANCE : ${balance}")
        answer = input("Press enter to play (q to quit):")
        if answer == "q":
            break
        balance += spin(balance)
    
    print(f"You left with: ${balance}")
   

if __name__ == "__main__":
    main()