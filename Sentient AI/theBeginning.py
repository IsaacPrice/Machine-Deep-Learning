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

# Change the labels to 0, 1, 2 for negative, neutral, positive
data['LABEL'] = data['LABEL'].replace(['Negative'], 0)
data['LABEL'] = data['LABEL'].replace(['Neutral'], 1)
data['LABEL'] = data['LABEL'].replace(['Positive'], 2)

# Get rid of any hastags from the comments
data['Caption'] = data['Caption'].str.replace('#', '')

# Change any words with the @ in it to 'user' to remove any usernames
def replace_at_mentions(text):
    return ' '.join(['user' if '@' in word else word for word in text.split()])

data['Caption'] = data['Caption'].apply(replace_at_mentions)
print (data.head())

# Tokenize the data
tokenizer = Tokenizer(num_words=10000, oov_token='<OOV>')
tokenizer.fit_on_texts(data['Caption'])

