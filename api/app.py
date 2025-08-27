from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import pandas as pd
import datetime
import os

LOG_PATH = "data/processed/prediction_log.csv"





# Load the model
model = joblib.load("data/processed/rf_model_fraud.joblib")

# Define input schema
class Transaction(BaseModel):
    amount: float
    ip_risk_score: float
    mouse_movement_score: float
    account_age_days: int
    time_of_day: int
    num_prev_transactions: int
    avg_transaction_amount: float
    session_duration_sec: int
    login_attempts_last_hour: int
    is_vpn: int
    is_international: int
    suspicious_activity_flag: int
    is_blacklisted_user: int
    payment_method: int
    device_type: int
    geo_location: int
    region: int
    country: int
    device_os: int
    browser: int
    day_of_week: int

# Initialize API
app = FastAPI()
@app.get("/")
def read_root():
    return {"message": "Fraud Detection API is live"}

@app.post("/predict")
def predict_fraud(data: Transaction):

    os.makedirs("data/processed", exist_ok=True)

    df = pd.DataFrame([data.dict()])

    # Ensure all expected features exist
    expected_features = model.feature_names_in_
    for col in expected_features:
        if col not in df.columns:
            df[col] = 0  # default filler value 

    # Reorder columns to match training order
    df = df[expected_features]

    # Predict
    prediction = model.predict(df)[0]
    probability = model.predict_proba(df)[0][1]  # probability of fraud

    # Log entry
    log_entry = df.copy()
    log_entry['fraud_prediction'] = prediction
    log_entry['fraud_probability'] = probability
    log_entry['timestamp'] = datetime.datetime.now()

    if not os.path.exists(LOG_PATH):
        log_entry.to_csv(LOG_PATH, index=False)
    else:
        log_entry.to_csv(LOG_PATH, mode='a', header=False, index=False)

    return {"fraud_prediction": int(prediction), "fraud_probability": float(probability)}



