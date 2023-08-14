import tensorflow
from tensorflow import keras
from keras.models import load_model

# Load the model
model = load_model('Sentient AI/sentimentModel.h5')

from tensorflow.keras.preprocessing.sequence import pad_sequences
from keras.preprocessing.text import Tokenizer

# Assuming you have a tokenizer from your training code
import pickle
with open('Sentient AI/tokenizer_pickle', 'rb') as f:
    tokenizer = pickle.load(f)

while True:
    text = input("Enter a text for sentiment analysis (or type 'quit' to exit): ")
    
    if text.lower() == 'quit':
        break

    # Preprocess the text
    sequences = tokenizer.texts_to_sequences([text])
    padded_sequences = pad_sequences(sequences, maxlen=100) # Replace with the actual max length

    # Predict the sentiment
    prediction = model.predict(padded_sequences)
    
    if prediction >= 0.5:
        print("The text is positive", str(prediction[0][0] * 100) + "%")
    else:
        print("The text is negative", str(prediction[0][0] * 100) + "%")
