from flask import Flask, render_template, request, jsonify
import random

# Create Flask app
app = Flask(__name__)

# Chatbot responses
responses = {
    "hello": [
        "Hello!",
        "Hi there!",
        "Hey!"
    ],
    "how are you": [
        "I am fine!",
        "Doing great!",
        "I'm good, thanks!"
    ],
    "what is ai": [
        "AI stands for Artificial Intelligence.",
        "AI helps machines think like humans."
    ],
    "deep learning": [
        "Deep learning is a subset of machine learning.",
        "Deep learning uses neural networks."
    ],
    "machine learning": [
        "Machine learning helps computers learn from data."
    ],
    "bye": [
        "Goodbye!",
        "See you later!"
    ]
}

# Home route
@app.route("/")
def home():
    return render_template("index.html")

# Chat route
@app.route("/chat", methods=["POST"])
def chat():

    user_message = request.json["message"].lower()

    reply = "Sorry, I don't understand."

    for key in responses:
        if key in user_message:
            reply = random.choice(responses[key])
            break

    return jsonify({
        "reply": reply
    })

# Run app
if __name__ == "__main__":
    app.run(debug=True)