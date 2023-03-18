tic_tac_list = \
[[0, 0, 1],
  [0, 1, 2],
  [2, 1, 0]]

def is_solved(board):
  check_zeros = []
  for i in range(3):
   for j in range(3):
     check_zeros.append(board[i][j])
   if len(board[i]) == board[i].count(board[i][0]) and board[i][0] != 0:
     return board[i][0]
   elif board[0][i] == board[1][i] == board[2][i] and board[0][i] != 0:
    return board[0][i]
   elif i+2 < 3 and board[i][i] != 0 and board[i][i] == board[i+1][i+1] == board[i+2][i+2]:
    return board[0][0]
   elif i+2 < 3 and board[i][i+2] != 0 and board[i][i+2] == board[i+1][i+1] == board[i+2][i]:
    return board[0][2]
  if 0 in check_zeros:
    return -1
  return 0

print(is_solved(tic_tac_list))