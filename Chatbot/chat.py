from flask import Flask, request, jsonify, render_template
import torch
from model import ChatModel
from utils import load_data, preprocess_data, bag_of_words
import random

app = Flask(__name__)

# Load data and model
data = load_data('intents.json')
X, y, all_words, tag_list = preprocess_data(data)

input_size = len(all_words)
hidden_size = 8
output_size = len(tag_list)

model = ChatModel(input_size, hidden_size, output_size)
model.load_state_dict(torch.load("chat_model.pth"))
model.eval()

bot_name = "ChatBot"

def get_response(sentence):
    sentence = sentence.split()
    X = bag_of_words(sentence, all_words)
    X = X.reshape(1, X.shape[0])
    X = torch.from_numpy(X).to(torch.float32)

    output = model(X)
    _, predicted = torch.max(output, dim=1)
    tag = tag_list[predicted.item()]

    probs = torch.softmax(output, dim=1)
    prob = probs[0][predicted.item()]

    if prob.item() > 0.60:
        for intent in data['intents']:
            if tag == intent['tag']:
                return random.choice(intent['responses'])
    else:
        return "I do not understand..."

@app.route("/")
def home():
    return render_template("homepage.html")

@app.route("/get_response", methods=["POST"])
def chat_response():
    user_input = request.form["user_input"]
    response = get_response(user_input)
    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(debug=True)