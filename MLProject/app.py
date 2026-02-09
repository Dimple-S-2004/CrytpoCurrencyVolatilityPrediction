import streamlit as st
import pandas as pd
import joblib
import numpy as np

# ---------------- Page Config ----------------
st.set_page_config(
    page_title="Crypto Volatility Predictor",
    layout="wide"
)

# ---------------- Load Model & Scaler ----------------
# Make sure these files are in the same folder as app.py
model = joblib.load("rf_model.pkl")
scaler = joblib.load("scaler.pkl")

# ---------------- Title ----------------
st.title("🪙 Crypto Volatility Predictor")
st.write("Enter market metrics to predict the 7-day rolling volatility.")

# ---------------- Sidebar Inputs (Manual Entry) ----------------
st.sidebar.header("📊 Market Metrics")

daily_return = st.sidebar.number_input(
    "Daily Return (e.g. 0.05 = 5%)",
    min_value=-1.0,
    max_value=1.0,
    value=0.000,
    step=0.001,
    format="%.3f"
)

hl_spread = st.sidebar.number_input(
    "High-Low Spread",
    min_value=0.0,
    max_value=1.0,
    value=0.020,
    step=0.001,
    format="%.3f"
)

oc_change = st.sidebar.number_input(
    "Open-Close Change",
    min_value=-1.0,
    max_value=1.0,
    value=0.010,
    step=0.001,
    format="%.3f"
)

volume = st.sidebar.number_input(
    "Volume",
    min_value=0,
    value=1_000_000,
    step=100_000,
    format="%d"
)

market_cap = st.sidebar.number_input(
    "Market Cap",
    min_value=1,
    value=50_000_000,
    step=1_000_000,
    format="%d"
)

# Derived feature
liquidity_ratio = round(volume / market_cap, 4)

# ---------------- Prediction ----------------
if st.button("🔮 Predict Volatility"):
    input_df = pd.DataFrame(
        [[
            daily_return,
            hl_spread,
            oc_change,
            volume,
            market_cap,
            liquidity_ratio
        ]],
        columns=[
            "daily_return",
            "hl_spread",
            "oc_change",
            "volume",
            "marketCap",
            "liquidity_ratio"
        ]
    )

    # Scale & Predict
    scaled_data = scaler.transform(input_df)
    prediction = model.predict(scaled_data)[0]

    # ---------------- Result ----------------
    st.metric(
        "Predicted 7-Day Volatility",
        f"{prediction:.3f}"
    )

    if prediction > 0.05:
        st.error("⚠️ High Risk Environment")
    else:
        st.success("✅ Stable Market Condition")

    # ---------------- Feature Importance ----------------
    st.divider()
    st.subheader("📌 What's driving this prediction?")

    importance_df = pd.DataFrame({
        "Metric": [
            "Daily Return",
            "High-Low Spread",
            "Open-Close Change",
            "Volume",
            "Market Cap",
            "Liquidity Ratio"
        ],
        "Influence": np.round(model.feature_importances_, 3)
    }).set_index("Metric")

    st.bar_chart(importance_df)
