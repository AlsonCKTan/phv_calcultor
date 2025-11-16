import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="PHV Daily Profit/Loss Calculator", layout="centered")

st.title("🚗 PHV Daily Profit/Loss Calculator")

# Inputs
st.header("Enter Your Daily Details")
total_income = st.number_input("Total income (fares, tips, incentives):", min_value=0.0, step=0.01)
fuel_cost = st.number_input("Fuel cost:", min_value=0.0, step=0.01)
platform_commission = st.number_input("Platform commission:", min_value=0.0, step=0.01)
parking_fees = st.number_input("Parking fees:", min_value=0.0, step=0.01)
erp_toll_charges = st.number_input("ERP/Toll charges:", min_value=0.0, step=0.01)
car_rental_or_loan = st.number_input("Car rental/loan:", min_value=0.0, step=0.01)
other_costs = st.number_input("Other costs:", min_value=0.0, step=0.01)
hours_worked = st.number_input("Total hours worked:", min_value=0.0, step=0.1)

# Calculate
total_expenses = fuel_cost + platform_commission + parking_fees + erp_toll_charges + car_rental_or_loan + other_costs
profit_or_loss = total_income - total_expenses
hourly_rate = profit_or_loss / hours_worked if hours_worked > 0 else 0

# Display result
st.subheader("Daily Summary")
st.write(f"**Total Income:** ${total_income:.2f}")
st.write(f"**Total Expenses:** ${total_expenses:.2f}")
if profit_or_loss >= 0:
    st.success(f"Profit: ${profit_or_loss:.2f}")
else:
    st.error(f"Loss: ${abs(profit_or_loss):.2f}")
st.write(f"**Hourly Rate:** ${hourly_rate:.2f}/hour")

# Chart
st.header("Visual Summary")
data = pd.DataFrame({
    'Category': ['Income', 'Expenses'],
    'Amount': [total_income, total_expenses]
})
fig, ax = plt.subplots()
ax.bar(data['Category'], data['Amount'], color=['green', 'red'])
ax.set_ylabel('Amount ($)')
ax.set_title('Income vs Expenses')
st.pyplot(fig)