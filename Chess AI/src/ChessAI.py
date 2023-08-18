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

# Add the layers
model.add(Conv2D(filters=32, kernel_size=(3,3), activation='relu', input_shape=(5890, 5, 8, 8)))
model.add(Flatten())
model.add(Dense(128, activation='relu'))
model.add(Dense(64, activation='relu'))
model.add(Dense(64, activation='relu'))
model.add(Dense(64, activation='relu'))
model.add(Dense(64, activation='relu'))
model.add(Dense(1, activation='softmax')) # Adjust output_size to match y

# Compile the model
model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

# Fit the model
model.fit(X, y, epochs=10)

# Save the model
model.save('Chess AI/data/model.h5')