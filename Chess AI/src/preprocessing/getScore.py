import pandas as pd

# Read the data
data = pd.read_csv('Chess AI/data/files/temp.csv')

# Extract the userful data into X and y
X = data[['WhiteElo', 'BlackElo',  'Termination', 'WhiteRatingDiff', 'BlackRatingDiff']]
y = data['Result']

# Scale all of the rankings for both the white and black using normalization from sklearn
from sklearn.preprocessing import MinMaxScaler
scaler = MinMaxScaler()

# Scale the rankings
X[['WhiteElo', 'BlackElo']] = scaler.fit_transform(X[['WhiteElo', 'BlackElo']])

# Scale the rating differences
X[['WhiteRatingDiff', 'BlackRatingDiff']] = scaler.fit_transform(X[['WhiteRatingDiff', 'BlackRatingDiff']])

# Function for the termination score
def termination_score(termination):
    if termination == "Normal":
        score = 1
    else:
        score = 0.5
    
    return score

# Run the termination score function on the termination column
X['Termination'] = X['Termination'].apply(termination_score)

# Function to make the y values 1 for white wins and 0 for black wins
def result_score(result):
    if result == "1-0":
        score = 1
    else:
        score = 0
    
    return score

# Run the result score function on the result column
y = y.apply(result_score)

# This will take the wins, and adds them to the X dataframe if it won
X['WhiteWin'] = y
X['BlackWin'] = 1 - y

# Calculate the win score by multiplying the rankings by the termination score, and adds 0.5 to the winning score
X['WhiteWinScore'] = X['WhiteElo'] * X['Termination'] * X['WhiteRatingDiff'] * (X['WhiteWin']/2)
X['BlackWinScore'] = X['BlackElo'] * X['Termination'] * X['BlackRatingDiff'] * (X['BlackWin']/2)

# Function to get which player won and by how much
def get_win_score(white_win_score, black_win_score):
    if white_win_score > black_win_score:
        win_score = white_win_score - black_win_score
    else:
        win_score = black_win_score - white_win_score
    
    return win_score

# Run the get win score function on the win scores
X['WinScore'] = X.apply(lambda x: get_win_score(x['WhiteWinScore'], x['BlackWinScore']), axis='columns')

# MinMaxScale the win scores
X[['WhiteWinScore', 'BlackWinScore', 'WinScore']] = scaler.fit_transform(X[['WhiteWinScore', 'BlackWinScore', 'WinScore']])

print(X['WinScore'].nlargest(5))
print(X['WinScore'].nsmallest(5))

# Save the data to a pickle file
import pickle
pickle.dump(X, open('Chess AI/data/pre-processed variables/scores', 'wb'))

