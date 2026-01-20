def score_resume(resume_text, jd_text, similarity_score, missing_skills):
    """Score the resume based on various factors."""
    score = 0

    # Base score from similarity
    score += similarity_score

    # Deduct points for each missing skill
    score -= len(missing_skills) * 2  # Deduct 2 points for each missing skill

    # Ensure score is within 0 to 100
    score = max(0, min(100, score))

    return score
