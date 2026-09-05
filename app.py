
import streamlit as st
import joblib
import re
import string

# Load model and TF-IDF vectorizer
model = joblib.load("spam_model.pkl")
tfidf = joblib.load("tfidf_vectorizer.pkl")

# Text cleaning function
def clean_text(text):
    text = text.lower()
    text = re.sub(r'http\S+|www\S+', '', text)
    text = re.sub(r'\d+', '', text)
    text = text.translate(str.maketrans('', '', string.punctuation))
    text = re.sub(r'\s+', ' ', text).strip()
    return text

# Stopword removal
from nltk.corpus import stopwords
stop_words = set(stopwords.words('english'))

def remove_stopwords(text):
    words = text.split()
    words = [word for word in words if word not in stop_words]
    return ' '.join(words)

# Application title
st.title("SMS Spam Detector")

# User input
message = st.text_area("Enter your SMS message:")

# Prediction button
if st.button("Predict"):
    if message.strip() == "":
        st.warning("Please enter an SMS message.")
    else:
        cleaned_message = clean_text(message)
        cleaned_message = remove_stopwords(cleaned_message)

        message_tfidf = tfidf.transform([cleaned_message])
        prediction = model.predict(message_tfidf)

        if prediction[0] == 1:
            st.error("SPAM")
        else:
            st.success("HAM")
