import streamlit as st
from src.text_extraction import extract_text
from src.preprocessing import preprocess
from src.skill_extraction import extract_skills
from src.model import predict_role
from src.matcher import match_resume_to_jd
from src.scoring import score_resume

st.title("AI-Powered Resume Screening & Job Matching System")

# Upload resume
uploaded_resume = st.file_uploader("Upload Resume (PDF or DOCX)", type=["pdf", "docx"])
jd_text = st.text_area("Paste Job Description")

if uploaded_resume and jd_text:
    # Extract text from resume
    resume_text = extract_text(uploaded_resume)
    
    # Preprocess resume text
    processed_resume = " ".join(preprocess(resume_text))
    
    # Predict role
    predicted_role = predict_role(processed_resume)
    
    # Match resume to job description
    match_results = match_resume_to_jd(resume_text, jd_text)
    
    # Score resume
    resume_score = score_resume(resume_text, jd_text, match_results['similarity_score'], match_results['missing_skills'])
    
    # Display results
    st.subheader("Results")
    st.write(f"Predicted Role: {predicted_role}")
    st.write(f"Match Percentage: {match_results['similarity_score']}%")
    st.write(f"Resume Score: {resume_score}/100")
    st.write("Missing Skills:", ", ".join(match_results['missing_skills']))
    st.write("Resume Skills:", ", ".join(match_results['resume_skills']))
    st.write("JD Skills:", ", ".join(match_results['jd_skills']))
