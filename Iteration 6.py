def check_winner(board, player_symbol):
for row in board:
if all(cell == player_symbol for cell in row):
return True

for col in range(3):
if all(board[row][col] == player_symbol for row in range(3)):
return True

if all(board[i][i] == player_symbol for i in range(3)):
return True

if all(board[i][2 - i] == player_symbol for i in range(3)):
return True

return False
