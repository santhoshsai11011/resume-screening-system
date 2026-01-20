from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import pickle
import os
from .preprocessing import preprocess
from .skill_extraction import extract_skills

def calculate_similarity(text1, text2, vectorizer=None):
    """Calculate similarity between two texts using TF-IDF and cosine similarity."""
    if vectorizer is None:
        vectorizer = TfidfVectorizer()
        vectors = vectorizer.fit_transform([text1, text2])
    else:
        vectors = vectorizer.transform([text1, text2])
    return cosine_similarity(vectors[0], vectors[1])[0][0]

def match_resume_to_jd(resume_text, jd_text, model_path='models/vectorizer.pkl'):
    """Match resume to job description and return similarity score and missing skills."""
    # Load vectorizer if available
    vectorizer = None
    if os.path.exists(model_path):
        with open(model_path, 'rb') as f:
            vectorizer = pickle.load(f)
    
    # Calculate overall similarity
    similarity_score = calculate_similarity(resume_text, jd_text, vectorizer)
    
    # Extract skills from both
    resume_skills = set(extract_skills(resume_text))
    jd_skills = set(extract_skills(jd_text))
    
    # Find missing skills
    missing_skills = jd_skills - resume_skills
    
    return {
        'similarity_score': round(similarity_score * 100, 2),  # as percentage
        'missing_skills': list(missing_skills),
        'resume_skills': list(resume_skills),
        'jd_skills': list(jd_skills)
    }
