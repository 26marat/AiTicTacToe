import random
import copy

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

def random_ai(board: list[list[str]], player: str) -> tuple[int, int]:
  """
  
  in: Takes in a multi-dimensional list represting the playing board
  in: Takes in a string representing the player ('X' or 'O')

  This function gets an AI to examine legal moves available to it, and then make a move

  Returns: A tuple containing the coordinates of the move selected by the AI
  
  """

  legal_moves = get_legal_moves(board)
  selected_move = random.choice(legal_moves)

  return selected_move

def get_legal_moves(board: list[list[str]]) -> list[tuple[int, int]]:
  """
  
  in: Takes in a multi-dimensional list represting the playing board

  This function iterates through the playing board and locates all the legal moves that can be made

  Returns: A list of tuples containing the coordinates of legal moves
  
  """
   
  legal_moves = []

  for row in range(len(board)):
    for col in range(len(board[row])):
      if board[row][col] is None:
         move = (row, col)
         legal_moves.append(move)
    
  return legal_moves
   

def minimax_ai(board: list[list[str]], player: str):
  """
  
  in: Takes in a multi-dimensional list represting the playing board
  in: Takes in a character representing the AI player (always 'O')

  This minimax algorithim iterates through the board, calling on its helper function to find an optimal move
  which is calculated by the score returned by helper

  Returns: Optimal move to be made by the AI
  
  """
  optimal_move = None
  optimal_score = None

  # Player is always 'X' and AI is always 'O'
  opponent = 'X'

  for move in get_legal_moves(board):
    _board = copy.deepcopy(board)  # Make a deep copy of the board to simulate the move
    make_move(_board, move, opponent)  # AI makes the move as 'O'

    score = minimax_score(_board, opponent, player)  # Get the score for this move
    if optimal_score is None or score > optimal_score: # Update the optimal score & move when possible
       optimal_move = move
       optimal_score = score

  return optimal_move


def minimax_score(board: list[list[str]], opponent: str, player: str) -> int:
  """
  
  in: Takes in a multi-dimensional list represting the playing board
  in: Takes in a character representing the HUMAN player (always 'X')
  in: Takes in a character representing the AI player (always 'O')

  This function is used to calculate the score for a move (10 for a winning move, -10 for loss, 0 for a draw),
  all of the human player's possible moves are simulated and score for each is kept track of. Eventually, the max score is taken
  to determine the optimal move

  Returns: Max score for AI's turn, minimum score for human player's turn
  
  """
  winner = get_winner(board)
  
  # If the game is done, return appropriate score
  if winner is not None:
    if winner == player:
        return -10  # AI Loss
    elif winner == opponent:
        return 10  # AI Win
  
  elif is_board_full(board):
     return 0  # Draw
  
  legal_moves = get_legal_moves(board)
  scores = []

  for move in legal_moves:
    _board = copy.deepcopy(board)
    make_move(_board, move, player)  # Current player makes a move
    
    # Recursively evaluate the score for the opponent's turn
    score = minimax_score(_board, opponent, player)
    scores.append(score)

  if opponent == 'O':  # AI's turn (maximize the score)
     return max(scores)
  else:  # Player's turn (minimize the score)
     return min(scores)   


def main() -> None:
  """

    The main function used to simulate the game. The user can slightly modify it to choose how they want the game to be played.

    Returns: None

  """

  # Loop until the game is over
  board = new_board()
  current_turn = 0
  while True:

    # Print out the board and get coordinates
    print_board(board)

    # Alternate turns between player using 'X' and AI using 'O'
    # Player with 'X' makes the first move
    if current_turn % 2 == 0:
      coords = get_move(board)
      make_move(board, coords, 'X')
    else:
      # coords = random_ai(board, 'O')
      coords = minimax_ai(board, 'O')
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
