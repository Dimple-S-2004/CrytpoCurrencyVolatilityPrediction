# CrytpoCurrencyVolatilityPrediction

A machine learning-based forecasting tool designed to predict the 7-day rolling volatility of cryptocurrencies. This project utilizes historical market data to help investors and analysts quantify risk through an interactive web interface.

## 🚀 Overview
Predicting volatility is essential for risk management in the highly fluctuating crypto market. This system processes raw OHLC (Open, High, Low, Close) data, engineers advanced financial indicators, and uses a Random Forest Regressor to forecast market "noisiness" over a weekly window.

## ✨ Key Features
* **Predictive Modeling:** Forecasts 7-day rolling standard deviation (volatility) with high precision.
* **Advanced Feature Engineering:** Includes custom-built indicators like Liquidity Ratio, HL Spread, and Open-Close Change.
* **Technical Indicators:** Integrated Average True Range (ATR) and Bollinger Bands for deeper market context.
* **Interactive Deployment:** A user-friendly Streamlit dashboard for real-time inference and "what-if" scenario testing.
* **Explainable AI:** Visualizes Feature Importance to show which market metrics (like volume or price spread) are driving the volatility.

## 📈 Model Performance
Evaluated on the 20% time-based test split (`14,147` records) using a `RandomForestRegressor`:

| Metric | Value |
| :--- | :--- |
| **R² Score (R-squared)** | `0.4615` |
| **Mean Absolute Error (MAE)** | `0.0203` |
| **Mean Squared Error (MSE)** | `0.0012` |

## 🛠️ Tech Stack
* **Language:** Python 3.x
* **Libraries:** Pandas, NumPy, Scikit-learn, Joblib
* **Model:** Random Forest Regressor
* **UI/Deployment:** Streamlit

## 📊 Exploratory Data Analysis (EDA)
During the analysis phase, we discovered:
* **Volatility Clustering:** High volatility periods tend to follow one another, especially during sharp price drops.
* **Spread Correlation:** A strong positive correlation exists between the High-Low Spread and upcoming volatility.
* **Liquidity Impact:** Lower Liquidity Ratios (Volume/Market Cap) often signal higher susceptibility to price swings.

## ⚙️ Installation & Usage
1. **Clone the repository:**
   ```bash
   git clone [https://github.com/Dimple-S-2004/CrytpoCurrencyVolatilityPrediction.git](https://github.com/Dimple-S-2004/CrytpoCurrencyVolatilityPrediction.git)
   cd CrytpoCurrencyVolatilityPrediction/MLProject
