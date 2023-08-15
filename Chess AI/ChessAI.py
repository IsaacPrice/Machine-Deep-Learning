import pandas as pd
from io import StringIO
import chess
import chess.pgn

# This will read the data of the chess games and train a model to predict the best move

# Read the data (cut the data down to 1000 lines for testing purposes)
data = pd.read_csv('Chess AI/temp.csv')

# Extract the userful data into X and y
useful_data = ['TimeControl', 'Termination', 'AN']
X = data[useful_data]
y = data['Result']

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

X = X.assign(Boards = X['AN'].apply(get_boards_from_movetext))
X = X.drop('AN', axis='columns')

# Calculate how trustworthy the win is based on rank, termination, and how long the game lasted % to how much is avalible
def calculate_win_score(white_rank, black_rank, time, termination, result):