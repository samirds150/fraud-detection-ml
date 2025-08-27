import streamlit as st
import requests
import json

st.title("💳 Fraud Detection Predictor")

st.markdown("Enter transaction details below:")

# Input fields (simplified version)
amount = st.number_input("Transaction Amount", min_value=1.0, step=1.0)
ip_risk_score = st.slider("IP Risk Score", 0.0, 100.0, 50.0)
mouse_movement_score = st.slider("Mouse Movement Score", 0.0, 1.0, 0.5)
account_age_days = st.number_input("Account Age (days)", min_value=0)
time_of_day = st.slider("Hour of Transaction", 0, 23, 12)
session_duration_sec = st.number_input("Session Duration (sec)", min_value=10)
login_attempts = st.number_input("Login Attempts (last hour)", min_value=0)

# Binary/categorical (just a few for demo)
is_vpn = st.selectbox("Using VPN?", [0, 1])
is_international = st.selectbox("International Transaction?", [0, 1])
device_type = st.selectbox("Device Type", [0, 1, 2])  # assuming encoded
payment_method = st.selectbox("Payment Method", [0, 1, 2])  # encoded

if st.button("Predict Fraud"):
    payload = {
        "amount": amount,
        "ip_risk_score": ip_risk_score,
        "mouse_movement_score": mouse_movement_score,
        "account_age_days": account_age_days,
        "time_of_day": time_of_day,
        "num_prev_transactions": 0,
        "avg_transaction_amount": amount,
        "session_duration_sec": session_duration_sec,
        "login_attempts_last_hour": login_attempts,
        "is_vpn": is_vpn,
        "is_international": is_international,
        "suspicious_activity_flag": 0,
        "is_blacklisted_user": 0,
        "payment_method": payment_method,
        "device_type": device_type,
        "geo_location": 0,
        "region": 0,
        "country": 0,
        "device_os": 0,
        "browser": 0,
        "day_of_week": 0
    }

    response = requests.post("http://127.0.0.1:8001/predict", json=payload)

    if response.status_code == 200:
        result = response.json()
        st.success(f"🧠 Prediction: {'FRAUD' if result['fraud_prediction'] == 1 else 'NOT FRAUD'}")
        st.info(f"Probability of fraud: {round(result['fraud_probability']*100, 2)}%")
    else:
        st.error("Prediction failed. Check the FastAPI server.")
