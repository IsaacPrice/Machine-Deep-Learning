import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers

# Load the X and y values from the pickle files
import pickle

with open('Chess AI/data/pre-processed variables/X.pkl', 'rb') as f:
    X = pickle.load(f)

with open('Chess AI/data/pre-processed variables/y.pkl', 'rb') as f:
    y = pickle.load(f)

# Create the model
model = keras.Sequential()

from tensorflow.keras.layers import Conv2D, MaxPooling2D
from tensorflow.keras.layers import Flatten, Dense
from tensorflow.keras.layers import Masking

model = keras.Sequential()
model.add(Dense(256, activation='relu', input_shape=(1, 320))) # Input shape reflects flattened 5 boards
model.add(Dense(128, activation='relu'))
model.add(Dense(64, activation='relu'))
model.add(Dense(64, activation='linear')) # 64 units to match flattened 8x8 target board

# Compile the model
model.compile(optimizer='adam', loss='mse', metrics=['accuracy']) # Mean squared error for a regression problem

# Fit the model
model.fit(X, y, epochs=10)

# Save the model
model.save('Chess AI/data/model.h5')