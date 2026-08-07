from fastapi import FastAPI
from market_data import get_market_data
from sentiment import analyze_sentiment
from ai_model import predictfrom logger import log_message
from security import check_api_keylog_message("Prediction requested")

if not check_api_key():
    return {"error": "Invalid API key"}from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "AI Market Predictor"}

@app.get("/predict")
def prediction():
    return {"signal": "BUY"}