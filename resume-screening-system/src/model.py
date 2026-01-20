import pandas as pd
import pickle
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report
import os

def train_model(data_path, model_save_dir='models'):
    """Train a resume classification model and save it."""
    df = pd.read_csv(data_path)
    X = df['text']
    y = df['role']

    # Split data
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Vectorize text
    vectorizer = TfidfVectorizer(stop_words='english', max_features=5000)
    X_train_vec = vectorizer.fit_transform(X_train)
    X_test_vec = vectorizer.transform(X_test)

    # Train classifier
    clf = LogisticRegression(max_iter=1000)
    clf.fit(X_train_vec, y_train)

    # Evaluate
    y_pred = clf.predict(X_test_vec)
    print("Accuracy:", accuracy_score(y_test, y_pred))
    print(classification_report(y_test, y_pred))

    # Save model and vectorizer
    os.makedirs(model_save_dir, exist_ok=True)
    with open(os.path.join(model_save_dir, 'classifier.pkl'), 'wb') as f:
        pickle.dump(clf, f)
    with open(os.path.join(model_save_dir, 'vectorizer.pkl'), 'wb') as f:
        pickle.dump(vectorizer, f)

    return clf, vectorizer

def load_model(model_path, vectorizer_path):
    """Load the trained model and vectorizer."""
    with open(model_path, 'rb') as f:
        clf = pickle.load(f)
    with open(vectorizer_path, 'rb') as f:
        vectorizer = pickle.load(f)
    return clf, vectorizer

def predict_role(text, model_path='models/classifier.pkl', vectorizer_path='models/vectorizer.pkl'):
    """Predict job role from resume text."""
    clf, vectorizer = load_model(model_path, vectorizer_path)
    vec = vectorizer.transform([text])
    return clf.predict(vec)[0]
