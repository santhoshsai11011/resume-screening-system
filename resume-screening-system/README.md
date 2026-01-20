# AI-Powered Resume Screening & Job Matching System

This project aims to build a machine learning system to screen resumes and match them with job descriptions. It extracts text from PDF and DOCX resumes, preprocesses the text, extracts skills, classifies resumes into job roles, matches resumes with job descriptions, detects missing skills, and scores resumes. The system includes a Streamlit web interface.

## Project Goals

- Extract text from PDF and DOCX resumes
- Clean and preprocess text using NLP
- Extract skills from resumes
- Classify resumes into job roles using ML
- Match resume with job description using similarity
- Detect missing skills compared to JD
- Generate resume score (out of 100)
- Rank multiple resumes against a JD
- Provide explainable outputs
- Have a clean Streamlit UI

## Project Structure

The project is organized as follows:

```
resume-screening-system/
├── data/               # Sample resumes and job descriptions
├── notebooks/          # Jupyter notebooks for experimentation
├── src/                # Source code modules
├── app/                # Streamlit application
├── models/             # Saved models
├── requirements.txt    # Dependencies
├── README.md           # Project documentation
└── .gitignore          # Ignored files
```

## Next Steps

This is the initial project structure. The development will proceed in phases, each adding new functionality.
