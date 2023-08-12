import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.models import Sequential
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
import openpyxl
import pandas as pd

# This program will read the labeled data from the file labaledText.xlxx and train a model to predict the sentiment of a comment

# Read the data
data = pd.read_excel('Sentient AI/labeledText.xlsx')

# Get rid of the File Name column
data = data.drop(['File Name'], axis=1)

# Change the labels to 0, 0.5, 1 for negative, neutral, positive and making the labels floats
data['KEY'] = data['LABEL'].replace(['negative', 'neutral', 'positive'], [0, 0.5, 1])

# Get rid of any hastags from the comments
data['Caption'] = data['Caption'].str.replace('#', '')

# Change any words with the @ in it to 'user' to remove any usernames
def replace_at_mentions(text):
    return ' '.join(['user' if '@' in word else word for word in text.split()])

data['Caption'] = data['Caption'].apply(replace_at_mentions)
print (data.head())

# Tokenize the data
tokenizer = Tokenizer(num_words=10000000, oov_token='<OOV>')
tokenizer.fit_on_texts(data['Caption'])

# Get the word index
word_index = tokenizer.word_index

# Split the data into X_train, X_test, y_train, y_test
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(data['Caption'], data['KEY'], test_size=0.2, random_state=42)

# Create the training data
training_sequences = tokenizer.texts_to_sequences(X_train)
training_padded = pad_sequences(training_sequences, maxlen=100, padding='post', truncating='post')

testing_sequences = tokenizer.texts_to_sequences(X_test)
testing_padded = pad_sequences(testing_sequences, maxlen=100, padding='post', truncating='post')

# Create the labels
training_labels = y_train.to_numpy()

# Create the model
model = Sequential()
model.add(keras.layers.Embedding(10000000, 16, input_length=100))
model.add(keras.layers.GlobalAveragePooling1D())
model.add(keras.layers.Dense(16, activation='relu'))
model.add(keras.layers.Dense(3, activation='softmax'))

model.compile(loss='sparse_categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

# Train the model
history = model.fit(training_padded, training_labels, epochs=30, verbose=1)

# Save the model
model.save('Sentient AI/sentimentModel.h5')