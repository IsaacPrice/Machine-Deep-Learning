import pandas as pd
import pickle
from io import StringIO
import chess
import chess.pgn
from getScore import get_score
from combineData import combine_data
from processFeatures import process_features

# This program will run all of the files for the preprocessing of the data all at once

path = 'Chess AI/data/files/'
csv_names = ['temp.csv']
movetext_column_names = ['AN'] # Each csv file calls the movetext column something different, so this will be a list of all of the names

# This will run and combine all of the csv files if there are multiple
if len(csv_names) > 1:
    data = combine_data(path, csv_names, movetext_column_names)
else: 
    data = pd.read_csv(path + csv_names[0])



# Here is where we figure out how good or bad a move is. This can get complicated, as there is a stockfish rating per move, but there is also data about the rankings of each players and the result of the game. We will use the stockfish rating for now, but we can change it later
