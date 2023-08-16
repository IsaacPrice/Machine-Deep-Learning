import pickle
import pandas as pd
from io import StringIO
import chess
import chess.pgn
'''
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
'''

# This will read the data of the chess games and train a model to predict the best move

# Read the data (cut the data down to 1000 lines for testing purposes)
data = pd.read_csv('Chess AI/data/temp.csv')

# Extract the userful data into X and y
X = data['AN']
# Load the pickle that has the y values
y = pickle.load(open('Chess AI/data/y_values.pkl', 'rb'))

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

# This will apply the function to the X values
X = X.apply(get_boards_from_movetext)

print(X.head())

# X now contains the board states for each move, and we need to change the X to contain board states with previous moves and Y to contain the next move

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

# Create a new list of X and y values
new_X = []
new_y = []

# Iterate through the X and y values and add them to the new lists
for i in range(len(X)):
    temp_X, temp_y = dissect_boards(X[i])
    new_X.append(new_X)
    new_y.append(new_y)

print(new_X.head())
print(new_y.head())

'''
# Now we need to pad the X values to make them all the same size
from tensorflow.keras.preprocessing.sequence import pad_sequences

# Pad the X values
new_X = pad_sequences(new_X, padding='post')

# Print the new dataframes
print(new_X.head())
print(new_y.head())

# Create the model
model = keras.Sequential()

from tensorflow.keras.layers import Conv2D, MaxPooling2D
from tensorflow.keras.layers import Flatten, Dense

'''