

import pandas as pd

# Load the data
data_path  = 'C:\\Users\\user\\OneDrive\\Documents\\diabetes data.csv'

df = pd.read_csv(data_path)

# Display the first few rows to confirm it loaded correctly
df.head()
def calculate_risk(age, bmi, glucose, bp):
    # Basic criteria for demonstration - you can adjust these thresholds
    risk_score = 0

    if age > 45:
        risk_score += 1
    if bmi > 25:
        risk_score += 1
    if glucose > 140:
        risk_score += 2
    if bp > 130:
        risk_score += 1

    # Determine the risk level based on the score
    if risk_score >= 3:
        return "High Risk"
    elif risk_score == 2:
        return "Moderate Risk"
    else:
        return "Low Risk"
    # Simulate user input values
age = 50        # Set age
bmi = 28        # Set BMI
glucose = 150   # Set glucose level
bp = 135        # Set blood pressure
# Calculate and display the risk level
risk_level = calculate_risk(age, bmi, glucose, bp)
print(f"Diabetes Risk Level: {risk_level}")
# Calculate and display the risk level
risk_level = calculate_risk(age, bmi, glucose, bp)
print(f"Diabetes Risk Level: {risk_level}")
print("""
### Explanation:
- **High Risk**: Indicates a higher chance of diabetes based on input parameters.
- **Moderate Risk**: Indicates a moderate chance; some parameters are in higher ranges.
- **Low Risk**: Indicates a lower chance based on the input values.
""")
streamlit run risk_calculator1.py