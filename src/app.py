import streamlit as st
import pandas as pd
import numpy as np
import joblib

# Load model & feature names
model = joblib.load("ddos_rf_model.pkl")
features = joblib.load("feature_names.pkl")

st.set_page_config(page_title="DDoS Detection", layout="centered")

st.title("🚨 DDoS Attack Detection System")
st.write("Upload network traffic data to check if it is **normal** or **malicious**.")

uploaded_file = st.file_uploader("Upload CSV file", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)

    st.subheader("Preview of uploaded data")
    st.dataframe(df.head())

    # Clean data
    df.replace([np.inf, -np.inf], np.nan, inplace=True)
    df.dropna(inplace=True)
    df.columns = df.columns.str.strip()

    # Keep only required features
    df = df[features]

    if st.button("Analyze Traffic"):
        predictions = model.predict(df)

        attack_count = sum(predictions)
        total = len(predictions)

        st.subheader("🔍 Analysis Result")

        if attack_count > 0:
            st.error(f"⚠️ DDoS ATTACK detected in {attack_count}/{total} flows")
        else:
            st.success("✅ Traffic looks BENIGN (No attack detected)")

        st.write("Prediction summary:")
        st.write(pd.Series(predictions).value_counts())