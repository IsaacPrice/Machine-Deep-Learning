import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers

# Load the X and y values from the pickle files
import pickle

with open('Chess AI/data/pre-processed variables/X.pkl', 'rb') as f:
    X = pickle.load(f)

with open('Chess AI/data/pre-processed variables/y.pkl', 'rb') as f:
    y = pickle.load(f)

# Now we need to pad the X values to make them all the same size
from tensorflow.keras.preprocessing.sequence import pad_sequences

# Pad the X values
padding_board = [[0] * 8 for _ in range(8)]

# Pad the sequences
def pad_sequence(sequence, target_length=5):
    while len(sequence) < target_length:
        sequence.insert(0, padding_board)
    return sequence

# Pad the X values
X['Boards'] = X['Boards'].apply(pad_sequence)


# Create the model
model = keras.Sequential()

from tensorflow.keras.layers import Conv2D, MaxPooling2D
from tensorflow.keras.layers import Flatten, Dense
from tensorflow.keras.layers import Masking

# Mask the padding
model.add(Masking(mask_value=0.)) # Assuming you used 0 for padding

# Add the layers
model.add(Conv2D(64, (3, 3), activation='relu', input_shape=(5, 8, 8)))
model.add(MaxPooling2D((2, 2)))
model.add(Conv2D(64, (3, 3), activation='relu'))
model.add(Flatten())
model.add(Dense(64, activation='relu'))
model.add(Dense(64, activation='relu'))
model.add(Dense(64, activation='relu'))
model.add(Dense(64, activation='relu'))

# Compile the model
model.compile(optimizer='adam', loss='mse', metrics=['accuracy'])

# Fit the model
model.fit(X, y, epochs=10)

# Save the model
model.save('Chess AI/data/model.h5')