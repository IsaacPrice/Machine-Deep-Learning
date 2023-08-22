import pandas as pd

# This will take the file data and turn it into what is needed, as long as the score if the user only wants the top games

def rename_columns(df, mapping):
    # Reverse the mapping dictionary
    reverse_mapping = {old_name: new_name for new_name, old_names in mapping.items() for old_name in old_names}
    
    # Rename the columns using pandas rename method
    df.rename(columns=reverse_mapping, inplace=True)

# This will read the csv file and extract the movetext from it
def extract_features(path, csv_name, movetext_column_name, features):
    # Read the csv file
    data = pd.read_csv(path + csv_name)

    # Extract the movetext from the csv file, depending on what name it is called
    movetext = data[movetext_column_name]
    whiteRank = data[features['WhiteRank']]
    blackRank = data[features['BlackRank']]
    termination = data[features['Termination']]
    result = data[features['Result']]

    return pd.concat([whiteRank, blackRank, movetext, termination, result], axis='columns')

# This will take the path and all the file names, and combine them into a single file
def combine_data(path, csv_names, movetext_column_names, features):
    # Initialize a list to store all of the data
    data = []

    # Iterate through the csv files
    for i in range(len(csv_names)):
        # Extract the movetext from the csv file
        movetext = extract_features(path, csv_names[i], features)

        # Add the movetext to the data list
        data.append(movetext)

    # Combine the data into a single list
    data = pd.concat(data)

    # Rename the column to be called 'movetext'
    data = data.rename(columns={movetext_column_names[0]: 'movetext'})

    # Rename the Rankings to their repective values in the dictionary
    data = data.rename(columns={features['WhiteRank']: 'WhiteRank'})
    data = data.rename(columns={features['BlackRank']: 'BlackRank'})

    # Return the data
    return data

# This will read the file and ensure that the columns are named correctly
def read_rename(path, filename, movetext_column_name, features):
    data = extract_features(path, filename, movetext_column_name, features)

    # Rename the columns to be called 'WhiteRank' and 'BlackRank'
    rename_columns(data, features)

    return data

# This is the section that was taken from Score.py

# Function for the termination score
def termination_score(termination):
    if termination == "Normal":
        score = 1
    else:
        score = 0.5
    
    return score

# Function to make the y values 1 for white wins and 0 for black wins
def result_score(result):
    if result == "1-0":
        score = 1
    else:
        score = 0
        
    return score

# Function to get which player won and by how much
def get_win_score(white_win_score, black_win_score):
    if white_win_score > black_win_score:
        win_score = white_win_score - black_win_score
    else:
        win_score = black_win_score - white_win_score
        
    return win_score

# This will take the data as a pandas dataframe, and 
def get_score(data, percentages={'Rank': 0.5, 'Termination': 0.5}):
    # Scale all of the rankings for both the white and black using normalization from sklearn
    from sklearn.preprocessing import MinMaxScaler
    scaler = MinMaxScaler()

    # Scale the rankings
    data[['WhiteRank', 'BlackRank']] = scaler.fit_transform(data[['WhiteRank', 'BlackRank']])

    # Function to get the termination score
    data['Termination'] = data['Termination'].apply(termination_score)

    # Run the result score function on the result column
    y = data['Result'].apply(result_score)

    # This will take the wins, and adds them to the X dataframe if it won
    data['WhiteWin'] = y
    data['BlackWin'] = 1 - y

    # Calculate the win score by using the percentages from the dictionary
    data['WhiteWinScore'] = data['WhiteRank'] * percentages['Rank'] + data['Termination'] * percentages['Termination'] + data['WhiteWin']
    data['BlackWinScore'] = data['BlackRank'] * percentages['Rank'] + data['Termination'] * percentages['Termination'] + data['BlackWin']


    # Run the get win score function on the win scores
    data['WinScore'] = data.apply(lambda data: get_win_score(data['WhiteWinScore'], data['BlackWinScore']), axis='columns')

    # MinMaxScale the win scores
    data[['WhiteWinScore', 'BlackWinScore', 'WinScore']] = scaler.fit_transform(data[['WhiteWinScore', 'BlackWinScore', 'WinScore']])
    
    return data

# This will select the top percentage of games and return them
def select_top_games(data, percentage=0.1):
    # Get the number of games to select
    num_games = int(len(data) * percentage)

    # Get the top games
    top_games = data.nlargest(num_games, 'WinScore')

    return top_games


# Lets re-oragnize this code:
# First, we will read the data, combine them if needed, and rename the columns
def get_data(path, csv_names, movetext_column_names, features):
    # This will run and combine all of the csv files if there are multiple
    if len(csv_names) > 1:
        data = combine_data(path, csv_names, movetext_column_names, features)
    else: 
        data = read_rename(path, csv_names[0], movetext_column_names, features)

    return data

# Second, we will turn the movetext into a list of moves
# Theres already a function that does that in the Main

# Third, we will flip the board so that it will look normal when it is printed onto the screen
def rotate_board(board):
    return [[board[j][i] for j in range(len(board))] for i in reversed(range(len(board[0])))]

# Fourth, if the user wants only the top percent of moves, we will give each score a value, and then select the top percent of games


# Fifth, we will change the data such that it will trash all of the moves that are not made by the winner