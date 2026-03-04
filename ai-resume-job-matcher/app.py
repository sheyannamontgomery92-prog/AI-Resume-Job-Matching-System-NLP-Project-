│
├── app.py
├── matcher.py
├── skill_extractor.py
├── requirements.txt
├── sample_resume.txt
├── sample_job.txt
└── README.md

requirements.text
streamlit
sentence-transformers
spacy
scikit-learn
nltk

from sentence_transformers import SentenceTransformer, util

model = SentenceTransformer('all-MiniLM-L6-v2')

def compute_similarity(resume_text, job_text):
    embeddings = model.encode([resume_text, job_text])
    similarity = util.cos_sim(embeddings[0], embeddings[1])
    return float(similarity[0][0]) * 100

    import spacy

nlp = spacy.load("en_core_web_sm")

def extract_keywords(text):
    doc = nlp(text)
    keywords = []

    for token in doc:
        if token.pos_ in ["NOUN", "PROPN"]:
            keywords.append(token.text.lower())

    return list(set(keywords))

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

        # AI Resume–Job Matching System

An NLP-based application that matches resumes to job descriptions using semantic similarity and keyword extraction.

## Features

- Sentence Transformer similarity scoring
- Keyword extraction with spaCy
- Match percentage output
- Missing skills identification
- Streamlit web interface

## Tech Stack

- Python
- Sentence Transformers
- spaCy
- Streamlit
- Scikit-learn

## Installation

pip install -r requirements.txt

python -m spacy download en_core_web_sm

## Run

streamlit run app.py

## Use Cases

- Resume optimization
- Job match analysis
- AI-powered recruitment tools
