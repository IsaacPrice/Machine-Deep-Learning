import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.models import Sequential
import pandas as pd

# This will read the data of the chess games and train a model to predict the best move

# Read the data
data = pd.read_csv('Chess AI/chess_games.csv')

# Extract the userful data into X and y
useful_data = ['TimeControl', 'Termination', 'AN']
X = data[useful_data]
y = data['Result']

print(X.head(3))
print(y.head(3))

# Parse the moves into a list
def parse_moves(moves):
    moves = moves.split()
    print(moves, moves.type())