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
 ┣ 📜 main.py                 # GUI Chatbot with API Integration
 ┣ 📜 use_model.py            # CLI-based Classification using ML Model
 ┣ 📜 binaryclassification.ipynb  # Jupyter Notebook for training the classification model
 ┣ 📜 mental_health.csv        # Dataset used for training the classification model
 ┣ 📜 model.pkl               # Trained Machine Learning model for message classification
 ┣ 📜 vectorizer.pkl          # TF-IDF Vectorizer for text preprocessing
 ┣ 📜 .env.example            # Example file for environment variables
 ┣ 📜 requirements.txt        # List of dependencies
 ┣ 📜 README.md               # Project Documentation
 ┗ 📜 .gitignore              # Ignore .env and unnecessary files
```

---

## 🧠 What Each File Does  

### 🔹 **Core Chatbot Files**  
- **`main.py`** – Runs the chatbot with a **GUI (Tkinter)** and integrates **Groq API** for AI-generated responses.  
- **`use_model.py`** – Provides a **command-line interface** to classify messages as **related** or **not related** using the trained model.  

### 🔹 **Machine Learning & Model Training**  
- **`binaryclassification.ipynb`** – Jupyter Notebook that trains the classification model. This includes **data preprocessing, feature extraction, model training, and evaluation**.  
- **`mental_health.csv`** – Dataset used to train the classification model. It contains labeled text samples that help the model learn to differentiate between mental health-related and general messages.  
- **`model.pkl`** – The trained machine learning model that predicts whether a message is **related or not related** to mental health.  
- **`vectorizer.pkl`** – A **TF-IDF Vectorizer** that converts text into numerical features before classification.  

### 🔹 **Setup & Configuration**  
- **`.env.example`** – Example file showing how to store your **Groq API key** securely.  
- **`requirements.txt`** – Contains all the dependencies required to run the chatbot. Install them using:  
  ```bash
  pip install -r requirements.txt
  ```
- **`.gitignore`** – Ensures sensitive files like `.env` are **not pushed** to GitHub.  

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
