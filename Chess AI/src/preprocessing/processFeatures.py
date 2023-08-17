import pandas as pd
import pickle
from io import StringIO
import chess
import chess.pgn
from supportFunctions import *

# This program will take in the data as a csv file, and then turn it into data that can be fed into the AI directly. This will be stored as a pickle file.

# This will read the file that should contain all of the data of the moves
data = pd.read_csv('Chess AI/data/files/temp.csv')
data = data['AN'] # Shouln't need this when completed

# This will take all of the move data and turn it into a list of boards after the movements
data = data.apply(get_boards_from_movetext)

# This will take the boards and change them into numerical data
data = data.apply(convert_board_to_numeric)

X = []
y = []

# This will get each X and y values
for i in range(len(data)):
    temp_X, temp_y = dissect_boards(data[i])
    X.append(temp_X)
    y.append(temp_y)

# print some values
print(X[0][0][0])
print(y[0][0])