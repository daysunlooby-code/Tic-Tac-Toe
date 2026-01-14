def check_tie(board):
for row in board:
for cell in row:
if isinstance(cell, int):
return False
return True


