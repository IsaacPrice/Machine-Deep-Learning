import pandas as pd
import tensorflow as tf
from tensorflow import keras
from keras.models import Sequential
from keras.layers import Dense, LSTM, Dropout

# Importing the dataset
data = pd.read_csv('temp.csv')

# Taking the 