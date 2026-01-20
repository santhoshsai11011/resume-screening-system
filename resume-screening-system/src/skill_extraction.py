import os
import json
from .preprocessing import preprocess

# Common skills list (can be extended or loaded from file)
SKILLS = [
    "python", "java", "c++", "c#", "javascript", "html", "css", "sql", "nosql",
    "machine learning", "deep learning", "nlp", "computer vision", "data analysis",
    "pandas", "numpy", "scikit-learn", "tensorflow", "pytorch", "keras",
    "flask", "django", "fastapi", "react", "angular", "vue", "node.js",
    "aws", "azure", "gcp", "docker", "kubernetes", "git", "ci/cd",
    "agile", "scrum", "project management", "communication", "leadership",
    "problem solving", "analytical skills", "statistics", "mathematics",
    "excel", "tableau", "power bi", "spark", "hadoop", "linux", "unix",
    "rest api", "graphql", "microservices", "mongodb", "postgresql", "mysql",
    "php", "ruby", "rails", "swift", "kotlin", "android", "ios",
    "ui/ux", "figma", "adobe xd", "photoshop", "illustrator"
]

def extract_skills(text):
    """Extract skills from text using a predefined skills list."""
    tokens = preprocess(text)  # returns lemmatized tokens
    # For multi-word skills, we need to check n-grams. We'll use a simple approach:
    # Convert text to lowercase and check for each skill (including spaces)
    text_lower = text.lower()
    extracted = set()
    for skill in SKILLS:
        if skill in text_lower:
            extracted.add(skill)
    # Also check token matches for single-word skills
    for token in tokens:
        if token in SKILLS:
            extracted.add(token)
    return list(extracted)

def load_skills_from_file(filepath):
    """Load skills from a JSON or text file."""
    if not os.path.exists(filepath):
        return SKILLS
    with open(filepath, 'r') as f:
        if filepath.endswith('.json'):
            return json.load(f)
        else:
            return [line.strip() for line in f if line.strip()]
