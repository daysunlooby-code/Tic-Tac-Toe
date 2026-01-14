
def place_move(board, choice, player_symbol):
 for row in range(len(board)):
for col in range(len(board[row])):
 if board[row][col] == choice:
 board[row][col] = player_symbol
return board
