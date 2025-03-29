import joblib
import re

loaded_model = joblib.load("mental_health_model.pkl")

loaded_vectorizer = joblib.load("tfidf_vectorizer.pkl")

def predict_message(text):
    text = text.lower()  
    text = re.sub(r'\W', ' ', text).strip()  
    text_tfidf = loaded_vectorizer.transform([text])  
    prediction = loaded_model.predict(text_tfidf)[0]  
    return "Related to Mental Health" if prediction == 1 else "Not Related to Mental Health"

while True:
    text_input = input("Enter a message (or type 'exit()' to quit): ")
    if text_input.lower() == 'exit()':
        break
    print(predict_message(text_input))