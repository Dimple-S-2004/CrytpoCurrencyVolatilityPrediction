📈 Cryptocurrency Volatility Prediction System

This project predicts short-term cryptocurrency volatility using historical market data and machine learning.
It is designed to help understand market risk and price instability.

🔍 Project Objective

To build a machine learning system that:

Analyzes historical cryptocurrency data

Predicts 7-day rolling volatility

Visualizes predictions through a Streamlit dashboard

📊 Dataset Description

The dataset contains daily market data for multiple cryptocurrencies, including:

Open, High, Low, Close prices (OHLC)

Trading Volume

Market Capitalization

Date and cryptocurrency name

(Dataset is not included due to size constraints.)

⚙️ Workflow

Data Loading – Load OHLC, volume, and market cap data

Data Preprocessing – Handle missing values and infinite values

Feature Engineering

Daily returns

7-day rolling volatility (target)

Liquidity ratio (Volume / Market Cap)

Price spreads

Technical indicators (Bollinger Bands, ATR)

Model Training

Random Forest Regressor

80% training, 20% testing (time-based split)

Model Evaluation

MAE

RMSE

R² Score

Deployment

Interactive Streamlit application (local)

🤖 Machine Learning Model

Algorithm: Random Forest Regressor

Problem Type: Regression

Target Variable: 7-day rolling volatility

📈 Model Evaluation Metrics

Mean Absolute Error (MAE)

Root Mean Squared Error (RMSE)

R² Score

🖥️ Streamlit Application

Features:

Cryptocurrency selection dropdown

Actual vs Predicted volatility plot

Model performance metrics


🚀 How to Run the Project
pip install -r requirements.txt
streamlit run app.py

📝 Notes

Dataset is excluded due to file size limits

Pre-trained model files are included

The project is intended for academic and learning purposes

