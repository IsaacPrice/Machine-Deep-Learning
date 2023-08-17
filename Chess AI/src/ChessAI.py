import pickle
import pandas as pd
from io import StringIO
import chess
import chess.pgn
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers

# This will read the data of the chess games and train a model to predict the best move

# Read the data (cut the data down to 1000 lines for testing purposes)
data = pd.read_csv('Chess AI/data/temp.csv')

# Extract the userful data into X and y
X = data['AN']
# Load the pickle that has the y values
y = pickle.load(open('Chess AI/data/y_values.pkl', 'rb'))

'''
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

# Save to pickle file
pickle.dump(X, open('Chess AI/data/X_values.pkl', 'wb'))
'''

# Load the pickle file
X = pickle.load(open('Chess AI/data/X_values.pkl', 'rb'))

# X now contains the board states for each move, and we need to change the X to contain board states with previous moves and Y to contain the next move


# Create a new list of X and y values
X = []
y = []

# Iterate through the X and y values and add them to the new lists
for i in range(len(X)):
    temp_X, temp_y = dissect_boards(X[i])
    X.append(X)
    y.append(y)
    print(i)

print(new_X[1][0][0])
print(new_y[1])


# Now we need to pad the X values to make them all the same size
from tensorflow.keras.preprocessing.sequence import pad_sequences

# Pad the X values
padding_board = [[0] * 8 for _ in range(8)]

# Pad the sequences
def pad_sequence(sequence, target_length=5):
    while len(sequence) < target_length:
        sequence.insert(0, padding_board)
    return sequence

# Create the model
model = keras.Sequential()

from tensorflow.keras.layers import Conv2D, MaxPooling2D
from tensorflow.keras.layers import Flatten, Dense
from tensorflow.keras.layers import Masking

# Mask the padding
model.add(Masking(mask_value=0.)) # Assuming you used 0 for padding

# Add the layers
model.add(Conv2D(64, (3, 3), activation='relu', input_shape=(5, 8, 8)))
model.add(MaxPooling2D((2, 2)))
model.add(Conv2D(64, (3, 3), activation='relu'))
model.add(Flatten())
model.add(Dense(64, activation='relu'))
model.add(Dense(64, activation='relu'))
model.add(Dense(64, activation='relu'))
model.add(Dense(64, activation='relu'))

# Compile the model
model.compile(optimizer='adam', loss='mse', metrics=['accuracy'])

# Fit the model
model.fit(new_X, new_y, epochs=10)

# Save the model
model.save('Chess AI/data/model.h5')