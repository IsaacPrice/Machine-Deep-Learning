import pickle
import tensorflow as tf
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences


# Load the model
with open('Sentient AI/model_pickle', 'rb') as f:
    model = pickle.load(f)

# Create a function to predict the sentiment of a review
def predict_sentiment(text):
    # Create a sequence
    tokenizer = Tokenizer(num_words=10000000, oov_token='<OOV>')
    tokenizer.fit_on_texts([text])
    sequence = tokenizer.texts_to_sequences([text])
    # Pad the sequence
    sequence = pad_sequences(sequence, maxlen=100, truncating='post')
    # Make a prediction
    prediction = model.predict(sequence)[0]
    print(prediction)
    # Return the sentiment
    return 'positive' if prediction[1] > prediction[0] else 'negative'

# Make a while loop to keep asking for reviews
while True:
    # Ask for a review
    text = input('Enter some text: ')
    # Predict the sentiment
    sentiment = predict_sentiment(text)
    # Print the sentiment
    print(sentiment)
    # Ask if the user wants to quit
    quit = input('Do you want to quit? (y/n) ')
    # If the user wants to quit, break the loop
    if quit == 'y':
        break
