import random
import time
import sys

digit_list = [x for x in range(1,10)]
sudoku_board = [[0 for _ in range(9)] for _ in range(9)]

def print_to_console(board, row, col, remaining_list, choice=""):
    print("\033[4;1H")
    print_sudoku_board(board)
    print(f"\n[+] position: ({row}, {col})")
    print(" " * 50, end="")
    sys.stdout.write("\b" * 50)
    sys.stdout.flush()
    print(f"[+] choice list: {remaining_list}")
    print(f"[+] choice: {choice}")

def print_sudoku_board(board):
    print("=" * 25)
    for row in range(9):
        print("|", end=" ")
        for col in range(9):
            print(board[row][col], end=" ")
            if col % 3 == 2:
                print("|", end=" ")
        print()
        if row % 3 == 2:
            print("=" * 25)

def check_board(board, row, col) -> bool:
    # check in horizontal row
    row_list = board[row]
    # print(f"[+] row list: {row_list}")
    if row_list.count(board[row][col]) > 1 :
        return False
    # check in vertical col
    col_list = [board[i][col] for i in range(9)]
    # print(f"[+] col list: {col_list}")
    if col_list.count(board[row][col]) > 1:
        return False
    # check in sub matrice
    sub_row = (row//3)*3
    sub_col = (col//3)*3
    sub_matrice = [digit for i in range(sub_row, sub_row+3) for digit in board[i][sub_col:sub_col+3]]
    # print(f"[+] sub matrice: {sub_matrice}")
    if sub_matrice.count(board[row][col]) > 1:
        return False
    print("[+] constraints satisfied")
    return True

def valid_board(remaining_list, board, row, col):
    time.sleep(0.1)
    if not (0 <= row < 9 and 0 <= col < 9):
        return
    picked_digit = []
    while len(picked_digit) < len(remaining_list):
        choice = random.choice(remaining_list)
        while choice in picked_digit:
            choice = random.choice(remaining_list)
        picked_digit.append(choice)
        board[row][col] = choice
        print_to_console(board, row, col, remaining_list, choice)
        if check_board(board, row, col):
            remaining_list.remove(choice)
            if col == 8 and not remaining_list:
                valid_board(digit_list.copy(), board, row+1, 0)
            else:
                valid_board(remaining_list, board, row, col+1)
        # print(f"[+] picked digits: {picked_digit}")
        if len(remaining_list) > 0 and board[row][col] not in remaining_list:
            remaining_list.append(board[row][col])
        # print(f"[+] remaining list: {remaining_list}")
    # print(f"[-] backtracking from position ({row}, {col})")
    board[row][col] = 0
    # print_sudoku_board(board)
    # print_to_console(board, row, col, remaining_list)
    
    # if col == 0:
    #     valid_board(board, row-1, 8)
    # else:
    #     valid_board(board, row, col-1)

def generate_random_board():
    valid_board(digit_list.copy(), sudoku_board, 0, 0)

print_sudoku_board(sudoku_board)
print(f"\n[+] position: (, )")
print(f"[+] choice list: ")
print(f"[+] choice: ")
generate_random_board()