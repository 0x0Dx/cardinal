from fastapi import FastAPI
from dotenv import load_dotenv
import os

load_dotenv()

app = FastAPI(title="Cardinal")

DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://cardinal:changeme@postgres:5432/cardinal")

@app.get("/")
def root():
  return {"status": "Cardinal is running", "version": "0.1.0"}

@app.get("/health")
def health():
  return {"status": "healthy"}

if __name__ == "__main__":
  import uvicorn
  uvicorn.run(app, host="0.0.0.0", port=8000)
