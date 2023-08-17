import pandas as pd

# This will take all of the games of chess, extract only the needed features, and combine them into a single large file

# This will read the csv file and extract the movetext from it
def extract_movetext(path, csv_name, movetext_column_name):
    # Read the csv file
    data = pd.read_csv(path + csv_name)

    # Extract the movetext from the csv file, depending on what name it is called
    movetext = data[movetext_column_name]

    return data

# This will take the path and all the file names, and combine them into a single file
def combine_data(path, csv_names, movetext_column_names):
    # Initialize a list to store all of the data
    data = []

    # Iterate through the csv files
    for i in range(len(csv_names)):
        # Extract the movetext from the csv file
        movetext = extract_movetext(path, csv_names[i])

        # Add the movetext to the data list
        data.append(movetext)

    # Combine the data into a single list
    data = pd.concat(data)

    # Rename the column to be called 'movetext'
    data = data.rename(columns={movetext_column_names[0]: 'movetext'})

    # Return the data
    return data