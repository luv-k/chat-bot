import os
import tkinter as tk
from tkinter import scrolledtext
import requests
import json
import joblib
import re
from dotenv import load_dotenv  # Securely load API keys

# Load environment variables
load_dotenv()

# Get API key from .env file
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
GROQ_MODEL = "llama-3.1-8b-instant"
API_URL = "https://api.groq.com/openai/v1/chat/completions"

# Ensure API key is available
if not GROQ_API_KEY:
    raise ValueError("Missing GROQ_API_KEY. Please set it in the .env file.")

# Load the mental health model and vectorizer
loaded_model = joblib.load("mental_health_model.pkl")
loaded_vectorizer = joblib.load("tfidf_vectorizer.pkl")

# Initialize conversation history
conversation_history = []

def classify_message(text):
    """Classify the user's message as related to mental health or not."""
    text = text.lower()
    text = re.sub(r'\W', ' ', text).strip()
    text_tfidf = loaded_vectorizer.transform([text])
    prediction = loaded_model.predict(text_tfidf)[0]
    return "Related to Mental Health" if prediction == 1 else "Not Related to Mental Health"

def generate_response(user_input):
    """Send user input to the Groq API and get the AI's response."""
    try:
        classification = classify_message(user_input)
        conversation_history.append({"role": "user", "content": user_input})

        headers = {
            "Authorization": f"Bearer {GROQ_API_KEY}",
            "Content-Type": "application/json"
        }
        payload = {
            "model": GROQ_MODEL,
            "messages": conversation_history,
            "stream": False
        }

        response = requests.post(API_URL, json=payload, headers=headers)

        if response.status_code != 200:
            print(f"Error: {response.status_code} - {response.text}")
            return f"{classification}\nSorry, I couldn't process that. Please try again later."

        response_data = response.json()
        ai_response = response_data["choices"][0]["message"]["content"]

        conversation_history.append({"role": "assistant", "content": ai_response})
        return f"{classification}\nAI: {ai_response}"

    except Exception as e:
        print(f"Error: {e}")
        return "Sorry, I couldn't process that. Please try again later."

def send_message():
    """Handle sending a message and displaying the AI's response."""
    message = entry.get()
    if message.strip():
        chat_window.config(state=tk.NORMAL)
        chat_window.insert(tk.END, "You: " + message + "\n")

        ai_response = generate_response(message)
        chat_window.insert(tk.END, ai_response + "\n")

        chat_window.config(state=tk.DISABLED)
        entry.delete(0, tk.END)

# Create the main window
root = tk.Tk()
root.title("Chat App")

# Chat display area
chat_window = scrolledtext.ScrolledText(root, wrap=tk.WORD, state=tk.DISABLED, width=50, height=20)
chat_window.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

# Entry widget for typing messages
entry = tk.Entry(root, width=40)
entry.grid(row=1, column=0, padx=10, pady=10)

# Send button
send_button = tk.Button(root, text="Send", command=send_message)
send_button.grid(row=1, column=1, padx=10, pady=10)

# Run the application
root.mainloop()
