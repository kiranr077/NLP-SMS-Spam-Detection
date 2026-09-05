# NLP-Based SMS Spam Detection Using TF-IDF and Machine Learning

## 1. Project Overview

This project is an NLP-based SMS Spam Detection system that classifies SMS messages as either **Ham (legitimate)** or **Spam (unwanted)**.

The system uses Natural Language Processing techniques to preprocess SMS text, TF-IDF to convert text into numerical features, and Machine Learning algorithms for classification.

## 2. Problem Statement

Spam messages are unwanted messages that may contain advertisements, fraudulent offers, or misleading information. Manually identifying spam messages is difficult when there are many messages.

This project aims to develop an automated NLP system that can classify SMS messages as Spam or Ham.

## 3. Objectives

- To preprocess SMS text data.
- To remove unnecessary text elements.
- To convert text into numerical features using TF-IDF.
- To train Machine Learning models for SMS classification.
- To evaluate the performance of the models.
- To develop a simple web application for real-time SMS prediction.

## 4. Dataset

**Dataset:** SMS Spam Collection

The dataset contains SMS messages labelled as either:

- Ham
- Spam

The dataset contains 5,572 SMS messages before duplicate removal.

After removing duplicate records, the data was used for model training and testing.

## 5. Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- NLTK
- TF-IDF
- Logistic Regression
- Multinomial Naive Bayes
- Streamlit
- Joblib
- Google Colab

## 6. Methodology

The project follows these steps:

1. Load the SMS dataset.
2. Inspect the dataset.
3. Check for missing values.
4. Remove duplicate records.
5. Convert labels into numerical values.
6. Clean the SMS text.
7. Split the dataset into training and testing data.
8. Convert text into TF-IDF features.
9. Train Machine Learning models.
10. Evaluate the models using classification metrics.
11. Select the better-performing model.
12. Save the trained model and TF-IDF vectorizer.
13. Develop a Streamlit web application.

## 7. Machine Learning Models

Two Machine Learning algorithms were tested:

### Logistic Regression

Accuracy: 95.55%

Precision: 98.85%

Recall: 65.65%

F1 Score: 78.90%

### Multinomial Naive Bayes

Accuracy: 96.32%

Precision: 98.95%

Recall: 71.76%

F1 Score: 83.19%

## 8. Final Model

Multinomial Naive Bayes was selected as the final model because it achieved better performance than Logistic Regression across accuracy, precision, recall, and F1 score.

Final performance:

- Accuracy: **96.32%**
- Precision: **98.95%**
- Recall: **71.76%**
- F1 Score: **83.19%**

## 9. Application

A Streamlit-based web application was developed for testing new SMS messages.

The user enters an SMS message and clicks the **Predict** button. The system then classifies the message as:

- **HAM**
- **SPAM**

## 10. Limitations

- Some SMS messages may still be misclassified.
- The dataset is relatively small compared with real-world messaging data.
- The model is trained mainly on English SMS messages.
- New types of spam messages may not always be detected correctly.

## 11. Future Scope

- Use a larger and more diverse SMS dataset.
- Support multiple languages.
- Experiment with advanced NLP and deep learning models.
- Improve detection of new and evolving spam patterns.
- Deploy the application as a public web service.

## 12. Conclusion

The project successfully demonstrates the use of NLP and Machine Learning for SMS spam detection.

TF-IDF was used to represent SMS messages as numerical features, while Multinomial Naive Bayes provided the best performance among the tested models.

The final system achieved an accuracy of **96.32%** and was integrated into a Streamlit application for real-time SMS classification.
