import pandas as pd

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