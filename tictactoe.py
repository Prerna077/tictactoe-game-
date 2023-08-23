import random

EMPTY = ' '
PLAYER = 'X'
AI = 'O'

def print_board(board):
    for row in board:
        print(' | '.join(row))
        print('-' * 9)

def evaluate(board):
    # Check rows, columns, and diagonals for a win
    for row in board:
        if row.count(PLAYER) == 3:
            return -10
        elif row.count(AI) == 3:
            return 10
    for col in range(3):
        if [board[row][col] for row in range(3)].count(PLAYER) == 3:
            return -10
        elif [board[row][col] for row in range(3)].count(AI) == 3:
            return 10
    if board[0][0] == board[1][1] == board[2][2] == PLAYER:
        return -10
    if board[0][0] == board[1][1] == board[2][2] == AI:
        return 10
    if board[0][2] == board[1][1] == board[2][0] == PLAYER:
        return -10
    if board[0][2] == board[1][1] == board[2][0] == AI:
        return 10
    return 0

def is_full(board):
    return all(cell != EMPTY for row in board for cell in row)

def minimax(board, depth, is_maximizing, alpha, beta):
    score = evaluate(board)

    if score == 10:
        return score - depth
    if score == -10:
        return score + depth
    if is_full(board):
        return 0

    if is_maximizing:
        max_eval = -float('inf')
        for row in range(3):
            for col in range(3):
                if board[row][col] == EMPTY:
                    board[row][col] = AI
                    eval = minimax(board, depth + 1, False, alpha, beta)
                    board[row][col] = EMPTY
                    max_eval = max(max_eval, eval)
                    alpha = max(alpha, eval)
                    if beta <= alpha:
                        break
        return max_eval
    else:
        min_eval = float('inf')
        for row in range(3):
            for col in range(3):
                if board[row][col] == EMPTY:
                    board[row][col] = PLAYER
                    eval = minimax(board, depth + 1, True, alpha, beta)
                    board[row][col] = EMPTY
                    min_eval = min(min_eval, eval)
                    beta = min(beta, eval)
                    if beta <= alpha:
                        break
        return min_eval

def get_best_move(board):
    best_move = (-1, -1)
    best_eval = -float('inf')
    alpha = -float('inf')
    beta = float('inf')

    for row in range(3):
        for col in range(3):
            if board[row][col] == EMPTY:
                board[row][col] = AI
                eval = minimax(board, 0, False, alpha, beta)
                board[row][col] = EMPTY

                if eval > best_eval:
                    best_eval = eval
                    best_move = (row, col)
    return best_move

def main():
    board = [[EMPTY, EMPTY, EMPTY] for _ in range(3)]
    print("Welcome to Tic-Tac-Toe!")
    print_board(board)

    while True:
        row, col = get_best_move(board)
        board[row][col] = AI
        print("\nAI's move:")
        print_board(board)

        if evaluate(board) == 10:
            print("AI wins!")
            break
        elif is_full(board):
            print("It's a draw!")
            break

        player_row = int(input("\nEnter row (0, 1, or 2): "))
        player_col = int(input("Enter column (0, 1, or 2): "))
        
        if board[player_row][player_col] == EMPTY:
            board[player_row][player_col] = PLAYER
        else:
            print("Cell is already occupied. Try again.")
            continue

        print("\nYour move:")
        print_board(board)

        if evaluate(board) == -10:
            print("Player wins!")
            break
        elif is_full(board):
            print("It's a draw!")
            break

if __name__ == "__main__":
    main()
