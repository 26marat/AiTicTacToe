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
  print("  ---------")
  for row in range(3):
        print(f"{row}|", end="")
        for col in range(3):
            # Print an empty space instead of None
            print(f" {board[row][col] if board[row][col] is not None else ' '} ", end="")
        print("|")
  print("  ---------\n")


def get_move(board: list[list[str]]) -> tuple[int, int]:
  """
  
  in: Takes in a multi-dimensional lists which is used to represent the playing board

  Accepts user input for an x and y coordinate that will be stored in a tuple for updating the playing board

  Returns: A tuple of two integers that represents the coordinates of the user's move
  
  """

  while True:
        try:
            
            x_cord = int(input("What is your move's X-coordinate? "))
            y_cord = int(input("What is your move's Y-coordinate? "))
            
            # Check if coordinates are within valid range
            if not (0 <= x_cord <= 2 and 0 <= y_cord <= 2):
                print("\nInvalid coordinates. Please enter values between 0 and 2.\n")
                continue
            
            # Check if the position is already taken
            if board[x_cord][y_cord] is not None:
                print("\nThat cell is already occupied. Choose a different one.\n")
                continue
            
            return (x_cord, y_cord)
        
        except ValueError:
            # Handle invalid input that can't be converted to an integer
            print("\nInvalid input. Please enter an integer between 0 and 2.\n")


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

def get_winner(board: list[list[str]]) -> str:
  """
  
  in: Takes in a multi-dimensional list represting the playing board

  This function checks for possible combinations of 3 'X' or 'O' in a row and declares a winner if there is

  Returns: The id of the player that won ('X' or 'O') or None if there is no winner yet
  
  """

  # Since this is a 3x3 board we will use brute force to check
  # Of course, for a larger board we would develop an algorithm to check, but this works well for now
  lines = [
    board[0], board[1], board[2], # Rows 1,2,3

    [board[0][0], board[1][0], board[2][0]], # Cols 1,2,3
    [board[0][1], board[1][1], board[2][1]],
    [board[0][2], board[1][2], board[2][2]],

    [board[0][0], board[1][1], board[2][2]], # Diagonals 1,2
    [board[0][2], board[1][1], board[2][0]]
  ]

  winnerA = ['X', 'X', 'X']
  winnerB = ['O', 'O', 'O']

  # Loop through the possible lines and return a winner if possible
  for line in lines:

    if line == winnerA:
      return 'X'
    
    elif line == winnerB:
      return 'O'

  return None

def is_board_full(board: list[list[str]]) -> bool:
  """
  
  in: Takes in a multi-dimensional list represting the playing board

  This function loops over the squares in each column of the board and checks if they are empty (None)

  Returns: False if empty (None) values are present, or True if each value is either an 'X' or an 'O'
  
  """

  for column in board:
     for square in column:
        if square is None:
           return False
        
  return True


def main() -> None:
  """

    Currently used for testing purposes

    Returns: None

  """

  # Loop until the game is over
  board = new_board()
  current_turn = 0
  while True:

    # Print out the board and get coordinates
    print_board(board)
    coords = get_move(board)

    # Alternate turns between player using 'X' and player using 'O'
    # Player with 'X' makes the first move
    if current_turn % 2 == 0:
      make_move(board, coords, 'X')
    else:
      make_move(board, coords, 'O')

    winner = get_winner(board)
    if winner is not None:
      print_board(board)
      print(f"\nGAME OVER! Player with ID '{winner}' has won.")
      break

    if is_board_full(board):
      print_board(board)
      print(f"GAME OVER! The game is a DRAW.")
      break

    current_turn += 1 # Alternate turn



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
