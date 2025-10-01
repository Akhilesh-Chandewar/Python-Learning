import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import streamlit as st

# Load data
data = pd.read_csv("day_2_salaries.csv")

# Features and target
X = data[["YearsExperience"]]  # independent variable
y = data["Salary"]  # dependent variable

# Train model
model = LinearRegression()
model.fit(X, y)

# Streamlit UI
st.title("📈 Simple Linear Regression: Salary Prediction")
st.write("Enter years of experience to predict salary:")

years_input = st.number_input(
    "Years of Experience", min_value=0, max_value=50, value=5, step=1, key="experience"
)

# Make prediction
if years_input is not None:
    X_new = np.array([[years_input]])
    prediction = model.predict(X_new)[0]
    st.success(
        f"💡 Predicted Salary for {years_input} years of experience: **{prediction:,.2f}**"
    )

# Plotting
st.subheader("Salary vs. Years of Experience")

fig, ax = plt.subplots()
ax.scatter(X, y, color="blue", label="Data points")
ax.plot(X, model.predict(X), color="red", linewidth=2, label="Regression line")
ax.set_xlabel("Years of Experience")
ax.set_ylabel("Salary")
ax.legend()

st.pyplot(fig)
