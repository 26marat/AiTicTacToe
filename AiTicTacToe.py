"""

    This function initializes a playing board with the values being set to 'None' by default

    Returns: A multi-dimensional list representing the playing board

"""
def new_board() -> list[list[None]]:
  
  board = [
  [None, None, None],
  [None, None, None],
  [None, None, None]]

  return board

"""

    in: Takes in a multi-dimensional lists which is used to represent the playing board

    Prints out the current playing board to the user along with coordinates to help the user visualize where to make their move

    Returns: None

"""
def print_board(board: list[list]) -> None:
  print("\n  0  1  2")
  print("  -------")
  print(f"0|{board[0][0]}  {board[0][1]}  {board[0][2]}|")
  print(f"1|{board[1][0]}  {board[1][1]}  {board[1][2]}|")
  print(f"2|{board[2][0]}  {board[2][1]}  {board[2][2]}|")
  print("  -------\n")


"""

    Currently used for testing purposes

    Returns: None

"""
def main() -> None:
  board = new_board()
  
  # Test code for the print_board function
  board[0][0] = 'X'
  board[0][1] = 'X'
  board[0][2] = 'O'
  board[1][0] = 'X'
  board[1][1] = 'X'
  board[1][2] = 'O'
  board[2][0] = 'X'
  board[2][1] = 'X'
  board[2][2] = 'O'
  print_board(board)

main()

# # Loop through turns until the game is over
# loop forever:
#   # TODO: hmm I'm not sure how best to do this
#   # right now. No problem, I'll come back later.
#   current_player = ???

#   # Print the current state of the board
#   render(board)

#   # Get the move that the current player is going
#   # to make.
#   move_co_ords = get_move()

#   # Make the move that we calculated above
#   make_move(board, move_co_ords, current_player)

#   # Work out if there's a winner
#   winner = get_winner(board)

#   # If there is a winner, crown them the champion
#   # and exit the loop.
#   if winner is not None:
#     print "WINNER IS %s!!" % winner
#     break

#   # If there is no winner and the board is full,
#   # exit the loop.
#   if is_board_full(board):
#     print "IT'S A DRAW!!"
#     break

#   # Repeat until the game is over
