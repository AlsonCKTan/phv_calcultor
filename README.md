# PHV Daily Profit/Loss Calculator

A simple Streamlit app for Private Hire Vehicle (PHV) drivers to calculate daily profit or loss, hourly rate, and visualize income vs expenses.

## Features
- Input daily income and expenses
- Calculate profit/loss
- Calculate hourly rate
- Display bar chart for income vs expenses

## How to Deploy on Streamlit Cloud
1. Fork or upload this repository to your GitHub account.
2. Go to https://streamlit.io/cloud and sign in.
3. Click **New App** → select your repository and branch.
4. Set the main file as `phv_calculator_app.py`.
5. Deploy and get your public URL.

## Requirements
- Python 3.7+
- Streamlit
- Pandas
- Matplotlib

## Run Locally
```bash
pip install -r requirements.txt
streamlit run phv_calculator_app.py
