import re
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer

nltk.download('punkt', quiet=True)
nltk.download('stopwords', quiet=True)
nltk.download('wordnet', quiet=True)

def clean_text(text):
    """Clean text by lowercasing, removing punctuation, numbers, and extra whitespace."""
    text = text.lower()
    text = re.sub(r'[^a-zA-Z\s]', '', text)  # keep only letters and whitespace
    text = re.sub(r'\s+', ' ', text).strip()
    return text

def tokenize(text):
    """Tokenize text into words."""
    return word_tokenize(text)

def remove_stopwords(tokens):
    """Remove stopwords from token list."""
    stop_words = set(stopwords.words('english'))
    return [token for token in tokens if token not in stop_words]

def lemmatize(tokens):
    """Lemmatize tokens."""
    lemmatizer = WordNetLemmatizer()
    return [lemmatizer.lemmatize(token) for token in tokens]

def preprocess(text):
    """Full preprocessing pipeline: clean, tokenize, remove stopwords, lemmatize."""
    text = clean_text(text)
    tokens = tokenize(text)
    tokens = remove_stopwords(tokens)
    tokens = lemmatize(tokens)
    return tokens
