def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_winner(board):
    # Проверка по строкам
    for row in board:
        if row.count(row[0]) == len(row) and row[0] != " ":
            return row[0]

    # Проверка по столбцам
    for col in range(len(board[0])):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != " ":
            return board[0][col]

    # Проверка по диагоналям
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
        return board[0][2]

    return None  # Нет победителя

def tic_tac_toe():
    board = [[" "]*3 for _ in range(3)]
    player = "X"
    moves = 0
    winner = None

    while moves < 9 and not winner:
        print_board(board)
        try:
            row = int(input(f"Enter row (0, 1, 2) for player {player}: "))
            col = int(input(f"Enter column (0, 1, 2) for player {player}: "))
        except ValueError:
            print("Please enter valid integers!")
            continue

        if 0 <= row <= 2 and 0 <= col <= 2:
            if board[row][col] == " ":
                board[row][col] = player
                moves += 1
                winner = check_winner(board)
                if winner:
                    break
                # Смена игрока
                player = "O" if player == "X" else "X"
            else:
                print("That spot is already taken! Try again.")
        else:
            print("Row and column must be 0, 1, or 2!")

    print_board(board)
    if winner:
        print(f"Player {winner} wins!")
    else:
        print("It's a tie!")

tic_tac_toe()
