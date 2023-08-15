# This program will take the first 1000 lines from chess_games.csv and add them to another file temp.csv

# Open the files
chess_games = open('Chess AI/chess_games.csv', 'r')
temp = open('Chess AI/temp.csv', 'w')

# Read the first 1000 lines
for i in range(1000):
    temp.write(chess_games.readline())
