import pandas as pd
from io import StringIO
import chess.pgn
import chess

# This will read the data of the chess games and train a model to predict the best move

# Read the data (cut the data down to 1000 lines for testing purposes)
data = pd.read_csv('Chess AI/temp.csv')

# Extract the userful data into X and y
useful_data = ['TimeControl', 'Termination', 'AN']
X = data[useful_data]
y = data['Result']

print(X.head(3))
print(y.head(3))

# This will take the movetext and turn it into a list of chess boards after the movement
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

