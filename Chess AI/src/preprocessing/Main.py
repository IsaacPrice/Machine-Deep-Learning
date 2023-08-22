import pandas as pd
import pickle
from io import StringIO
import chess
import chess.pgn
import numpy as np
from score import get_score, select_top_games
from extractData import *
from progressBar import *
from supportFunctions import get_boards_from_movetext, convert_board_to_numeric, dissect_boards, preprocess_boards, preprocess_target_boards

# This program will run all of the files for the preprocessing of the data all at once

path = 'Chess AI/data/files/'
csv_names = ['temp.csv']
movetext_column_names = ['AN'] # Each csv file calls the movetext column something different, so this will be a list of all of the names
features = { # This will be a dictionary of the features that we want to keep, and all the possible names that they could be called
    'MoveText': ['AN', 'MoveText'],
    'WhiteRank': ['WhiteElo'],
    'BlackRank': ['BlackElo'],
    'Termination': ['Termination'],
    'Result': ['Result']
}
top_percent = 1

# This will run and combine all of the csv files if there are multiple
data = get_data(path, csv_names, movetext_column_names, features)

# Create and move the progress bar
bar = ProgressBar(50, 50)
bar.smooth_update(5)

# Parse the movetext into a list of boards
data['Boards'] = data['MoveText'].apply(get_boards_from_movetext)
bar.smooth_update(25)

# Rotate the boards
data['Boards'] = data['Boards'].apply(rotate_board)

# Get rid of all the columns we don't need anymore
get_rid = ['WhiteRank', 'BlackRank', 'MoveText', 'Termination', 'Result', 'WhiteWinScore', 'BlackWinScore']
data = data.drop(get_rid, axis='columns')
bar.smooth_update(30)



# Turn the boards into numerical data
data['Boards'] = data['Boards'].apply(convert_board_to_numeric)
bar.smooth_update(40)

# Dissect the boards into X and y values
X = []
y = []

# This will get each X and y values
for i in range(len(data)):
    temp_X, temp_y = dissect_boards(data.iloc[i]['Boards'])
    X.append(temp_X)
    y.append(temp_y)

bar.smooth_update(50)

# Now we need to convert the X values to the following format (each needs to be a board):
# [previous 5th move] [previous 4th move] [previous 3rd move] [previous 2nd move] [previous 1st move] [next move]

print()

final_X = []
final_y = []


for i in range(len(X)): # Goes through each games
    for j in range(len(X[i])): # Goes through each previous moves
        temp = (preprocess_boards(X[i][j]))
        final_X.append(temp)
        temp = y[i][j]
        final_y.append(temp)

final_y = preprocess_target_boards(final_y)


final_X = np.array(final_X)

# Save the X and y values as pickle files
with open('Chess AI/data/pre-processed variables/X.pkl', 'wb') as f:
    pickle.dump(final_X, f)

with open('Chess AI/data/pre-processed variables/y.pkl', 'wb') as f:
    pickle.dump(final_y, f)
