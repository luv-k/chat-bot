 ---

# 🤖 Chatbot  

A **machine learning-powered chatbot** that classifies messages and provides AI-generated responses. Built using **Python, Tkinter, Groq API, and NLP-based classification**.  

---

## 🌟 Features  
✅ **Message Classification** – Uses an ML model to analyze user messages.  
✅ **AI-Powered Responses** – Integrates **Groq API** for intelligent replies.  
✅ **Interactive Chat Interface** – Built with **Tkinter** for a user-friendly experience.  
✅ **Real-Time Conversations** – Tracks chat history for a continuous chat experience.  
✅ **Secure API Key Handling** – Uses environment variables to keep your API key safe.  

---

## 📦 Installation & Setup  

### 🔧 1. Clone the Repository  
```bash
git clone https://github.com/luv-k/chatbot.git
cd chatbot
```

### 📥 2. Install Dependencies  
Make sure you have Python installed, then install the required libraries:  
```bash
pip install -r requirements.txt
```

### 🔑 3. Secure Your API Key  
Your **Groq API Key** should **not** be hardcoded in your script. Follow these steps to keep it secure:  

1️⃣ **Install `python-dotenv` (if not already installed):**  
```bash
pip install python-dotenv
```  

2️⃣ **Create a `.env` file** in the project directory and add your API key:  
```
GROQ_API_KEY=your_api_key_here
```

3️⃣ **Ensure `.env` is not pushed to GitHub** by adding it to `.gitignore`:  
```
.env
```

---

## 🚀 Running the Chatbot  

### 🎮 GUI Mode (Tkinter)  
Run the chatbot with a graphical interface:  
```bash
python main.py
```

### 🔍 CLI Mode (Command Line)  
Run the chatbot in terminal mode:  
```bash
python use_model.py
```
Then type a message, and the bot will classify it as **"Related"** or **"Not Related"**.  

---

## 📂 Project Structure  
```
📦 chatbot
 ┣ 📜 main.py               # GUI Chatbot with API Integration
 ┣ 📜 use_model.py          # CLI-based Classification using ML Model
 ┣ 📜 model.pkl             # Pretrained Model for Classification
 ┣ 📜 vectorizer.pkl        # Text Vectorizer for NLP Processing
 ┣ 📜 .env.example          # Example file for environment variables
 ┣ 📜 requirements.txt      # List of Dependencies
 ┣ 📜 README.md             # Project Documentation
 ┗ 📜 .gitignore            # Ignore .env and unnecessary files
```

---

## 🧠 What Are the `.pkl` Files?  

The `.pkl` (Pickle) files store **pre-trained machine learning models and NLP components**, allowing the chatbot to classify messages efficiently without retraining the model every time.  

- **`model.pkl` (Message Classification Model)**  
  - A trained machine learning model that classifies messages as **related** or **not related** to mental health topics.  
  - Uses **text processing techniques** and a classifier (e.g., Logistic Regression, SVM, etc.).  
  - Helps determine if the chatbot should provide general or mental health-focused responses.  

- **`vectorizer.pkl` (TF-IDF Vectorizer)**  
  - Converts text messages into numerical features using **TF-IDF (Term Frequency-Inverse Document Frequency)**.  
  - Ensures that the input text is **properly formatted** before classification.  
  - This is an essential part of **Natural Language Processing (NLP)** in the chatbot.  

---

## 📊 More About the Model  

To learn more about how the **ML model was trained**, check out my **Kaggle profile**:  

👉 [Kaggle: brrownnn](https://www.kaggle.com/brrownnn)  

---

## 📌 Notes  
- **Never share your API key** or commit it to GitHub.  
- If your API key gets exposed, **revoke and regenerate** a new one immediately.  
- The chatbot can be improved by **training the model on a larger dataset** or integrating **better AI responses**.  

---

🚀 **Try it out and chat away!** 💬  

---
