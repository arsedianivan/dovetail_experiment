from fastapi import FastAPI
from scraper import fetch_data
from analysis import analyze_data
from ml_model import segment_data

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Welcome to the AI-Powered Market Research API"}

@app.get("/")
def read_root():
    return {"message": "Welcome to the AI-Powered Market Research API"}

@app.get("/fetch")
def fetch_data_route(url: str):
    data = fetch_data(url)
    return {"data": data}

@app.post("/analyze")
def analyze_data_route(data: dict):
    summary = analyze_data(data)
    return {"summary": summary}

@app.get("/")
def read_root():
    return {"message": "Welcome to the AI-Powered Market Research API"}

@app.get("/fetch")
def fetch_data_route(url: str):
    data = fetch_data(url)
    return {"data": data}

@app.post("/analyze")
def analyze_data_route(data: dict):
    summary = analyze_data(data)
    return {"summary": summary}

@app.post("/segment")
def segment_data_route(data: dict):
    segments = segment_data(data)
    return {"segments": segments}
