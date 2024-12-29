def new_board() -> list[list[None]]:
  """

    This function initializes a playing board with the values being set to 'None' by default

    Returns: A multi-dimensional list representing the playing board

  """
  
  board = [
  [None, None, None],
  [None, None, None],
  [None, None, None]]

  return board


def print_board(board: list[list[str]]) -> None:
  """

    in: Takes in a multi-dimensional lists which is used to represent the playing board

    Prints out the current playing board to the user along with coordinates to help the user visualize where to make their move

    Returns: None

  """
  print("\n  0  1  2")
  print("  -------")
  print(f"0|{board[0][0]}  {board[0][1]}  {board[0][2]}|")
  print(f"1|{board[1][0]}  {board[1][1]}  {board[1][2]}|")
  print(f"2|{board[2][0]}  {board[2][1]}  {board[2][2]}|")
  print("  -------\n")


def get_move() -> tuple[int, int]:
  """
  
  Accepts user input for an x and y coordinate that will be stored in a tuple for updating the playing board

  Returns: A tuple of two integers that represents the coordinates of the user's move
  
  """

# TODO: Add error-handling for the input (valid coordinates only), maybe a new function can do this?
  x_cord = int(input("What is your move's X-coordinate? "))
  y_cord = int(input("What is your move's Y-coordinate? "))

  coordinates = (x_cord, y_cord)
  return coordinates


def make_move(board: list[list[str]], coordinates: tuple[int, int], symbol: str) -> list[list[str]]:
  """
  
  in: Takes in a multi-dimensional list represting the playing board
  in: Takes in a two-element tuple of ints that represent the coordinates of the move to be made
  in: A string of length one that represents the symbol that's used by the player making the move; either 'X' or 'O'

  This function creates a new playing board which is the same as the previous one with the exception of the recent move made by a player

  Returns: A multi-dimensional list representing the updated playing board
  
  """

  new_board = board # Create a copy of the board that will be updated
  new_board[coordinates[0]][coordinates[1]] = symbol # Update the new_board to avoid possible unexpected behaviour associated with mutation

  return new_board



def main() -> None:
  """

    Currently used for testing purposes

    Returns: None

  """

  board = new_board()
  print_board(board)
  
  coords = get_move()
  print(coords)

  print_board(make_move(board, coords, 'X'))

  coords = get_move()
  print(coords)

  print_board(make_move(board, coords, 'O'))

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
