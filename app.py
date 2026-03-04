import streamlit as st
from matcher import compute_similarity
from skill_extractor import extract_keywords

st.title("AI Resume–Job Matching System")

resume = st.text_area("Paste Resume Text")
job = st.text_area("Paste Job Description")

if st.button("Analyze Match"):
    if resume and job:
        score = compute_similarity(resume, job)
        resume_keywords = extract_keywords(resume)
        job_keywords = extract_keywords(job)

        missing_skills = list(set(job_keywords) - set(resume_keywords))

        st.subheader("Match Score")
        st.write(f"{round(score,2)} %")

        st.subheader("Missing Keywords")
        st.write(missing_skills[:20])

    else:
        st.warning("Please enter both resume and job description.")
