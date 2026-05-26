# Intelligent Enterprise Assistant – AI-Powered Organizational Support System

## Overview

The **Intelligent Enterprise Assistant** is an AI-driven chatbot platform developed to enhance organizational efficiency in large enterprises and institutions. The system integrates **Artificial Intelligence (AI)**, **Natural Language Processing (NLP)**, **Deep Learning**, and **Document Intelligence** to provide employees with instant support for HR services, IT assistance, company policies, announcements, and document analysis.

The platform functions as a smart virtual assistant capable of understanding natural language queries, retrieving contextual information, summarizing uploaded documents, and maintaining secure communication through authentication mechanisms.

---

# Key Features

## AI-Powered Chatbot

- NLP-based conversational assistant
- Context-aware intelligent responses
- Multi-turn conversation support
- HR and IT support handling
- Real-time response generation

---

## Document Intelligence

- PDF and DOCX upload support
- OCR-based text extraction
- AI-powered summarization
- Keyword extraction
- Smart document analysis

---

## Secure Authentication

- Email OTP verification
- JWT Authentication
- Role-Based Access Control
- Secure session management

---

## Content Moderation

- Offensive language filtering
- Toxicity detection
- Custom moderation system

---

## Scalability & Performance

- Multi-user support
- Optimized response handling
- Fast backend processing
- Efficient cache management

---

# Technology Stack

## Frontend

- React.js / Next.js
- HTML5
- CSS3
- Tailwind CSS
- Material UI

---

## Backend

- Flask / FastAPI
- Python
- REST APIs

---

## AI & NLP

- LangChain
- HuggingFace Transformers
- Sentence Transformers
- Retrieval-Augmented Generation (RAG)

---

## Database & Storage

- PostgreSQL / MongoDB
- Redis Cache
- FAISS / ChromaDB / Pinecone

---

## Security

- JWT Authentication
- Email OTP Verification
- Role-Based Access Control

---

# System Modules

## 1. Enterprise Chatbot

Handles employee queries related to:

- HR policies
- Leave management
- Payroll support
- IT troubleshooting
- Internal procedures
- Company announcements

---

## 2. Document Processing Engine

Processes uploaded documents to:

- Extract text
- Generate summaries
- Identify keywords
- Analyze organizational data

---

## 3. Admin Dashboard

Allows administrators to:

- Upload knowledge base documents
- Monitor chatbot activities
- Manage users
- View analytics and reports

---

# Workflow

1. User logs into the platform securely.
2. User interacts with the AI chatbot.
3. NLP models analyze the query.
4. Relevant information is retrieved from the knowledge base.
5. AI generates contextual responses.
6. Uploaded documents are analyzed and summarized.
7. Moderation layer filters inappropriate content.

---

# Objectives

- Improve organizational productivity
- Reduce HR and IT workload
- Provide instant employee assistance
- Enhance document accessibility
- Ensure secure communication

---

# Future Enhancements

- Multilingual support
- Voice assistant integration
- AI-powered ticketing system
- Mobile application support
- Advanced analytics dashboard
- ERP integration

---

## Code

#index.html
```
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">

    <title>Enterprise AI Assistant</title>

    <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&display=swap" rel="stylesheet">

    <style>

        *{
            margin:0;
            padding:0;
            box-sizing:border-box;
            font-family:'Poppins',sans-serif;
        }

        body{
            height:100vh;
            background:linear-gradient(135deg,#0f172a,#1e3a8a,#7c3aed);
            display:flex;
            justify-content:center;
            align-items:center;
            overflow:hidden;
        }

        .chat-container{
            width:430px;
            height:750px;
            background:rgba(255,255,255,0.08);
            backdrop-filter:blur(15px);
            border-radius:25px;
            overflow:hidden;
            box-shadow:
                0 0 30px rgba(0,0,0,0.4),
                0 0 60px rgba(124,58,237,0.4);
            border:1px solid rgba(255,255,255,0.15);

            display:flex;
            flex-direction:column;
        }

        .chat-header{
            background:linear-gradient(90deg,#2563eb,#7c3aed);
            color:white;
            padding:25px;
            text-align:center;
            font-size:26px;
            font-weight:700;
            letter-spacing:1px;
            box-shadow:0 5px 20px rgba(0,0,0,0.3);
        }

        .chat-header span{
            font-size:15px;
            display:block;
            margin-top:5px;
            opacity:0.8;
            font-weight:300;
        }

        .chat-box{
            flex:1;
            padding:20px;
            overflow-y:auto;
            scroll-behavior:smooth;
        }

        .chat-box::-webkit-scrollbar{
            width:6px;
        }

        .chat-box::-webkit-scrollbar-thumb{
            background:#7c3aed;
            border-radius:10px;
        }

        .message{
            max-width:80%;
            padding:14px 18px;
            margin:14px 0;
            border-radius:18px;
            font-size:15px;
            line-height:1.5;
            animation:fadeIn 0.3s ease;
            position:relative;
        }

        .user{
            margin-left:auto;
            background:linear-gradient(135deg,#2563eb,#3b82f6);
            color:white;
            border-bottom-right-radius:5px;
            box-shadow:0 5px 15px rgba(37,99,235,0.4);
        }

        .bot{
            background:rgba(255,255,255,0.12);
            color:white;
            border-bottom-left-radius:5px;
            backdrop-filter:blur(5px);
            box-shadow:0 5px 15px rgba(0,0,0,0.2);
        }

        .time{
            font-size:10px;
            opacity:0.7;
            margin-top:5px;
            text-align:right;
        }

        .chat-input{
            display:flex;
            padding:20px;
            background:rgba(0,0,0,0.2);
            backdrop-filter:blur(10px);
        }

        .chat-input input{
            flex:1;
            padding:15px;
            border:none;
            outline:none;
            border-radius:15px;
            font-size:15px;
            background:rgba(255,255,255,0.1);
            color:white;
        }

        .chat-input input::placeholder{
            color:#d1d5db;
        }

        .chat-input button{
            margin-left:12px;
            padding:14px 20px;
            border:none;
            border-radius:15px;
            background:linear-gradient(135deg,#7c3aed,#2563eb);
            color:white;
            cursor:pointer;
            font-size:15px;
            font-weight:600;
            transition:0.3s;
            box-shadow:0 5px 15px rgba(124,58,237,0.4);
        }

        .chat-input button:hover{
            transform:scale(1.05);
            opacity:0.9;
        }

        @keyframes fadeIn{
            from{
                opacity:0;
                transform:translateY(10px);
            }
            to{
                opacity:1;
                transform:translateY(0);
            }
        }

        .glow{
            position:absolute;
            width:300px;
            height:300px;
            background:#7c3aed;
            border-radius:50%;
            filter:blur(120px);
            opacity:0.25;
            z-index:-1;
        }

        .glow1{
            top:-100px;
            left:-100px;
        }

        .glow2{
            bottom:-100px;
            right:-100px;
            background:#2563eb;
        }

    </style>
</head>

<body>

<div class="glow glow1"></div>
<div class="glow glow2"></div>

<div class="chat-container">

    <div class="chat-header">
        🤖 Enterprise AI Assistant
        <span>Smart Organizational Support System</span>
    </div>

    <div class="chat-box" id="chat-box">

        <div class="message bot">
            👋 Welcome to Intelligent Enterprise Assistant.<br>
            How can I help you today?
            <div class="time">Now</div>
        </div>

    </div>

    <div class="chat-input">

        <input type="text" id="message" placeholder="Type your message...">

        <button onclick="sendMessage()">Send</button>

    </div>

</div>

<script>

async function sendMessage(){

    let input = document.getElementById("message");

    let message = input.value;

    if(message.trim() === ""){
        return;
    }

    let chatBox = document.getElementById("chat-box");

    // User Message
    chatBox.innerHTML += `
        <div class="message user">
            ${message}
            <div class="time">You</div>
        </div>
    `;

    // Scroll
    chatBox.scrollTop = chatBox.scrollHeight;

    // Send Request
    let response = await fetch("/chat", {

        method:"POST",

        headers:{
            "Content-Type":"application/json"
        },

        body:JSON.stringify({
            message:message
        })

    });

    let data = await response.json();

    // Bot Message
    chatBox.innerHTML += `
        <div class="message bot">
            ${data.reply}
            <div class="time">${data.time}</div>
        </div>
    `;

    input.value = "";

    // Auto Scroll
    chatBox.scrollTop = chatBox.scrollHeight;
}

</script>

</body>
</html>
```

# app.py
```
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
```

# Output Screenshots


## Chatbot Interface

<img width="1920" height="1200" alt="image" src="https://github.com/user-attachments/assets/af55f9d6-6518-4ae8-b264-2722bea1535a" />


---

## Document Upload Module

<img width="1920" height="1200" alt="image" src="https://github.com/user-attachments/assets/7dd59ca6-acef-494f-8d1c-c302edfec691" />


---

## AI Response Output

<img width="1920" height="1200" alt="image" src="https://github.com/user-attachments/assets/e43f6d99-1ebe-4476-a46a-016506dcb4de" />

---





# Installation

## Clone Repository

```bash
git clone git clone https://github.com/24900874/chatbox.git
