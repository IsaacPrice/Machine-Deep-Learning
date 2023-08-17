import pandas as pd
import pickle
from io import StringIO
import chess
import chess.pgn
from score import get_score, select_top_games
from combineData import combine_data, read_rename
from supportFunctions import get_boards_from_movetext, convert_board_to_numeric, dissect_boards

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

# This will run and combine all of the csv files if there are multiple
if len(csv_names) > 1:
    data = combine_data(path, csv_names, movetext_column_names, features)
else: 
    data = read_rename(path, csv_names[0], movetext_column_names, features)

print("Finished getting data")

# Now we will give a score to each game
data = get_score(data)
print("Finished giving scores")

# For now, we will just train the data on the top games. This can be changed later to the movements from the stockfish engine combined with the top games to make the AI better
data = select_top_games(data)
print("Finished selecting top games")

# Parse the movetext into a list of boards
data['Boards'] = data['MoveText'].apply(get_boards_from_movetext)
print("Finished parsing movetext")

# !!! STOCKFISH STUFF GOES HERE !!!

# Get rid of all the columns we don't need anymore
get_rid = ['WhiteRank', 'BlackRank', 'MoveText', 'Termination', 'Result', 'WhiteWinScore', 'BlackWinScore']
data = data.drop(get_rid, axis='columns')
print("Finished getting rid of columns")

# Columns: 
# Index(['WhiteWin', 'BlackWin', 'WinScore','Boards'], dtype='object')

# !!! IF NEEDED ACCURACY, HERE ONLY CHOOSE THE TOP WINSCORES !!!

# Turn the boards into numerical data
data['Boards'] = data['Boards'].apply(convert_board_to_numeric)
print("Finished converting boards to numeric")

# Dissect the boards into X and y values
X = []
y = []

# This will get each X and y values
for i in range(len(data)):
    temp_X, temp_y = dissect_boards(data.iloc[i]['Boards']) # TODO: fix this
    X.append(temp_X)
    y.append(temp_y)

print("Finished dissecting boards")

print(y[0][0])

# Save the X and y values as pickle files
with open('Chess AI/data/pre-processed variables/X.pkl', 'wb') as f:
    pickle.dump(X, f)

with open('Chess AI/data/pre-processed variables/y.pkl', 'wb') as f:
    pickle.dump(y, f)

