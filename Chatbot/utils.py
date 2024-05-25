import json
import numpy as np
from sklearn.preprocessing import LabelEncoder
import torch
import torch.nn.functional as F
from nltk.stem.porter import PorterStemmer
import nltk

# Download the required NLTK data
nltk.download('punkt')

# Initialize the stemmer
stemmer = PorterStemmer()

def load_data(json_file):
    with open(json_file, 'r') as f:
        data = json.load(f)
    return data

def preprocess_data(data):
    inputs = []
    labels = []
    all_words = []
    tag_list = []

    for intent in data['intents']:
        tag = intent['tag']
        tag_list.append(tag)
        for pattern in intent['patterns']:
            words = nltk.word_tokenize(pattern)  # Tokenize the pattern
            stemmed_words = [stemmer.stem(word.lower()) for word in words]  # Stem each word
            all_words.extend(stemmed_words)
            inputs.append(stemmed_words)
            labels.append(tag)
    
    all_words = sorted(set(all_words))
    tag_list = sorted(set(tag_list))

    X = []
    y = []
    le = LabelEncoder()
    le.fit(tag_list)

    for i, sentence in enumerate(inputs):
        bag = np.zeros(len(all_words), dtype=np.float32)
        for word in sentence:
            if word in all_words:
                bag[all_words.index(word)] = 1.0
        X.append(bag)
        y.append(le.transform([labels[i]])[0])
    
    X = np.array(X)
    y = np.array(y)

    return X, y, all_words, tag_list

def bag_of_words(tokenized_sentence, words):
    bag = np.zeros(len(words), dtype=np.float32)
    stemmed_sentence = [stemmer.stem(word.lower()) for word in tokenized_sentence]
    for word in stemmed_sentence:
        if word in words:
            bag[words.index(word)] = 1.0
    return bag
