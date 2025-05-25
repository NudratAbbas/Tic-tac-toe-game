---

### **Code: `tic_tac_toe.py`**
```python
def print_board(board):
    print("\n")
    print(" " + board[0] + " | " + board[1] + " | " + board[2])
    print("-----------")
    print(" " + board[3] + " | " + board[4] + " | " + board[5])
    print("-----------")
    print(" " + board[6] + " | " + board[7] + " | " + board[8])
    print("\n")

def check_win(board, player):
    win_conditions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # horizontal
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # vertical
        [0, 4, 8], [2, 4, 6]              # diagonal
    ]
    for condition in win_conditions:
        if all(board[i] == player for i in condition):
            return True
    return False

def is_draw(board):
    return all(cell in ['X', 'O'] for cell in board)

def tic_tac_toe():
    board = [str(i+1) for i in range(9)]
    current_player = "X"

    print("Welcome to Tic Tac Toe!")
    print_board(board)

    while True:
        move = input(f"Player {current_player}'s turn. Enter a position (1-9): ")

        if not move.isdigit() or int(move) < 1 or int(move) > 9:
            print("Invalid input. Please choose a number between 1 and 9.")
            continue

        pos = int(move) - 1
        if board[pos] in ['X', 'O']:
            print("This position is already taken. Try again.")
            continue

        board[pos] = current_player
        print_board(board)

        if check_win(board, current_player):
            print(f"Congratulations! Player {current_player} wins!")
            break

        if is_draw(board):
            print("It's a draw!")
            break

        current_player = "O" if current_player == "X" else "X"

if __name__ == "__main__":
    tic_tac_toe()
