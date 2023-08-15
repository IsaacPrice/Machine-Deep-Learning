import pandas as pd

# This program is meant to take the scores of the games and from a scale of 0 to 1, 0 being the least trustworthy and 1 being the most trustworthy, and then save the scores to a file for the Chess AI to use

# Read the data
data = pd.read_csv('Chess AI/temp.csv')

# Extract the userful data into X and y
X = data[['WhiteElo', 'BlackElo',  'TimeControl', 'Termination', 'WhiteRatingDiff', 'BlackRatingDiff']]
y = data['Result']

