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