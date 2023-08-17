import pandas as pd
import chess
import chess.pgn
from io import StringIO

# This function will take the movement string and turn it into a list of the boards after every move
def get_boards_from_movetext(chess_data_string):
    # Convert the string to a file-like object
    pgn = StringIO(chess_data_string)

    # Read the game from the PGN data
    game = chess.pgn.read_game(pgn)

    # Initialize the board
    board = chess.Board()

    # Initialize a list to store all the board states
    boards = []

    # Iterate through the moves, push each move to the board, and store the board state
    for move in game.mainline_moves():
        board.push(move)
        # Convert the current board state to a 2D array and append it to the list
        board_array = [[str(board.piece_at(chess.square(rank, file))) for file in range(8)] for rank in range(8)]
        boards.append(board_array)

    return boards


# This is the dictionary for each letter to convert each thingie to
piece_mapping = {
    'P': .1,  # White pawn
    'p': -.1, # Black pawn
    'N': .2,  # White knight
    'n': -.2, # Black knight
    'B': .3,  # White bishop
    'b': -.3, # Black bishop
    'R': .4,  # White rook
    'r': -.4, # Black rook
    'Q': .5,  # White queen
    'q': -.5, # Black queen
    'K': .6,  # White king
    'k': -.6, # Black king
    'None': 0 # Empty square
}
# This function will turn the board into numeric data
def convert_board_to_numeric(boards):
    new_boards = []

    for board in boards:
        new_board = []
        for row in board:
            new_row = []
            for piece in row:
                if piece is None:
                    new_row.append(0)
                else:
                    new_row.append(piece_mapping[str(piece)])
            new_board.append(new_row)
        new_boards.append(new_board)
    
    return new_boards


# This function will take the board of moves, and then will return a list of the board states with the previous moves, with a seperate value of the next move
def dissect_boards(board_list):
    # Initialize a list to store the dissected boards
    X = [] # This will contain a the lists, which each has the last 5 moves
    y = [] # This will contain the next move

    temp_X = [] # This will contain the last 5 moves
    temp_y = 0 # This will contain the next move

    # Iterate through the boards
    for i in range(len(board_list)):
        temp_X = []
        temp_y = 0 

        # This will loop through the last 5 moves and add them to the list as long as it exists
        for j in range(5):
            if i - j >= 0:
                temp_X.append(board_list[i - j])
            else: 
                pass # We actually won't add anything to the list, and will be padded later on
        
        # This will add the next move to the y list
        if i + 1 < len(board_list):
            temp_y = board_list[i + 1]
        else:
            # This means that the game is over, and we will assingn the last move to the y value
            temp_y = board_list[i]

            # Add the temp lists to the main lists
            X.append(temp_X)
            y.append(temp_y)

            # Return the lists
            return X, y

        # Add the temp lists to the main lists
        X.append(temp_X)
        y.append(temp_y)


# Function