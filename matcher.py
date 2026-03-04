from sentence_transformers import SentenceTransformer, util

model = SentenceTransformer('all-MiniLM-L6-v2')

def compute_similarity(resume_text, job_text):
    embeddings = model.encode([resume_text, job_text])
    similarity = util.cos_sim(embeddings[0], embeddings[1])
    return float(similarity[0][0]) * 100
