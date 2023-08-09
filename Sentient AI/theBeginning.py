import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout, Activation, Flatten, LSTM
import pandas as pd

# This program will read a text prompt (in this case a IMDB review) and try to understand if it is positive or negative

# Load the data
df = pd.read_csv('Sentient AI/IMDB_Dataset.csv')

# Change the sentiment column to 0 or 1
df['sentiment'] = df['sentiment'].apply(lambda x: 1 if x == 'positive' else 0)

# Remove the <br /> tags
df['review'] = df['review'].str.replace('<br />', '')

# Tokenize the data for the review column
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences

# Create the tokenizer
tokenizer = Tokenizer(num_words=10000000, oov_token='<OOV>')
tokenizer.fit_on_texts(df['review'])

# Create the sequences
sequences = tokenizer.texts_to_sequences(df['review'])

# Pad the sequences
padded_sequences = pad_sequences(sequences, maxlen=100, truncating='post')

# Split the data into X and y
X = padded_sequences
y = df['sentiment']

# Split the data into train and test sets using sklearn
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y)

# Create the model
model = Sequential([
    tf.keras.layers.Embedding(10000000, 16, input_length=100),
    tf.keras.layers.LSTM(64, return_sequences=True),
    tf.keras.layers.LSTM(32),
    tf.keras.layers.Dense(64, activation='relu'),
    tf.keras.layers.Dense(2, activation='softmax')
])

# Compile the model
model.compile(loss='sparse_categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

# Train the model
model.fit(X_train, y_train, epochs=10, validation_data=(X_test, y_test))

# Evaluate the model
model.evaluate(X_test, y_test)