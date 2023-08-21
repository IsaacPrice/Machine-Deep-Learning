import pandas as pd

# Importing the dataset
data = pd.read_csv('prediction AI/temp.csv')

# Get the text 
text = data['text']

# This function will take a text and return a list of sentences
def get_sentences(text):
    sentences = []
    for sentence in text:
        sentences.append(sentence.split())
    return sentences

# This function will take a sentence and return a list of the previous 3 words, along with the next word
def get_word_sequences(sentence):
    sequences = []
    for i in range(3, len(sentence)):
        sequences.append((sentence[i-3:i], sentence[i]))
    return sequences

print(text)
# Turns each blog post into a list of sentences
text = text.apply(get_sentences)

print(text)

from collections import Counter
word_counts = Counter()
for sentences in text:
    for sentence in sentences:
        for word in sentence.split():
            word_counts[word] += 1

# This will show the most 100 common words
word_counts.most_common(100)

