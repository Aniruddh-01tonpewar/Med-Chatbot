import os

HF_TOKEN = os.getenv("HF_TOKEN")
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

HUGGINGFACE_REPO_ID="mistralai/Mistral-7B-Instruct-v0.3"
DATA_PATH = "data/"
DB_FAISS_PATH = "vectorestore/db_faiss"

CHUNK_SIZE = 500
CHUNK_OVERLAP = 50