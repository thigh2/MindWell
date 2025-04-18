import streamlit as st
import pandas as pd

# Load the data (optional if you just need the calculator)
# data_path  = 'C:\\Users\\user\\OneDrive\\Documents\\diabetes data.csv'
# df = pd.read_csv(data_path)
# st.write(df.head())  # Display data if needed

# Title and introduction
st.title("Diabetes Risk Calculator")
st.write("Enter the following information to calculate your risk of diabetes.")

# Input fields
age = st.number_input("Age", min_value=0, max_value=120, value=30)
bmi = st.number_input("BMI", min_value=10.0, max_value=50.0, value=22.0)
glucose = st.number_input("Glucose Level", min_value=0, max_value=300, value=100)
bp = st.number_input("Blood Pressure", min_value=0, max_value=200, value=120)

# Risk calculation function
def calculate_risk(age, bmi, glucose, bp):
    risk_score = 0
    if age > 45:
        risk_score += 1
    if bmi > 25:
        risk_score += 1
    if glucose > 140:
        risk_score += 2
    if bp > 130:
        risk_score += 1

    # Determine risk level based on score
    if risk_score >= 3:
        return "High Risk"
    elif risk_score == 2:
        return "Moderate Risk"
    else:
        return "Low Risk"

# Calculate and display risk level
if st.button("Calculate Risk"):
    risk_level = calculate_risk(age, bmi, glucose, bp)
    st.write(f"Diabetes Risk Level: **{risk_level}**")
    st.write("""
    ### Explanation:
    - **High Risk**: Indicates a higher chance of diabetes based on input parameters.
    - **Moderate Risk**: Indicates a moderate chance; some parameters are in higher ranges.
    - **Low Risk**: Indicates a lower chance based on the input values.
    """)

