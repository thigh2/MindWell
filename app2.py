import streamlit as st
import joblib
import numpy as np

# Load the trained model and scaler
model = joblib.load('heart_disease_model.pkl')
scaler = joblib.load('scaler.pkl')

# Define the app
st.title("Heart Disease Prediction App")
st.write("""
This app predicts the likelihood of heart disease based on user input. 
Please provide the following information:
""")

# Create input fields
age = st.number_input("Age", min_value=1, max_value=120, step=1, value=25)
sex = st.selectbox("Sex", options=[("Male", 1), ("Female", 0)], format_func=lambda x: x[0])[1]
blood_pressure = st.number_input("Resting Blood Pressure (mm Hg)", min_value=50, max_value=250, step=1, value=120)
cholesterol = st.number_input("Cholesterol (mg/dl)", min_value=100, max_value=600, step=1, value=200)
heart_rate = st.number_input("Max Heart Rate Achieved (bpm)", min_value=50, max_value=220, step=1, value=150)  # Parenthesis properly closed here

# Prediction logic
if st.button("Predict"):
    try:
        # Prepare the input data
        input_data = np.array([age, sex, blood_pressure, cholesterol, heart_rate]).reshape(1, -1)
        input_data_scaled = scaler.transform(input_data)

        # Make the prediction
        prediction = model.predict(input_data_scaled)
        result = "Heart Disease Detected" if prediction[0] == 1 else "No Heart Disease Detected"

        # Display the result
        st.success(f"Prediction: {result}")
    except Exception as e:
        st.error(f"An error occurred: {str(e)}")
