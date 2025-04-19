# Preventive Healthcare System

This project is an **AI-powered Predictive Healthcare System** that helps identify individuals at risk of developing chronic diseases such as **diabetes, heart disease, or obesity**. The system provides personalized recommendations for preventive care based on lifestyle and medical data.

## Features
- AI-based health risk prediction for **diabetes**, **heart disease**, and **obesity**.
- User-friendly form for inputting health and lifestyle data.
- Implement risk assessment logic for chronic disease prediction. 
- Uses pre-trained machine learning models to assess the risk levels.
- Integrated with **Streamlit** for interactive web-based applications.

## Prerequisites

Ensure you have the following installed:
- Python 3.7+
- `streamlit`
- `pandas`
- `scikit-learn`
- `requests`
- `Pillow` (for image processing)

Install all the necessary dependencies using the following command:

```bash
pip install -r requirements.txt
```

## Installation & Setup

1. **Clone the repository**:

```bash
git clone https://github.com/aaarif796/AI-Powered-Preventive-Healthcare-System.git
cd AI-Powered-Preventive-Healthcare-System
```

2. **Download or Place Model Files**:

Make sure to have the pre-trained model files:
- `label_encoders.pkl`
- `lr_dt.pkl` (Logistic Regression model for Diabetes)
- `lr_ht.pkl` (Logistic Regression model for Heart Disease)
- `lr_ob.pkl` (Logistic Regression model for Obesity)

Place these files inside the `model` folder.

3. **Add Images**:

Place relevant images in the `images` folder for visual representation.

4. **CSS Styling**:

The application uses a custom CSS file for styling. Ensure you have the `style.css` file in the `style` folder.

## Usage

1. **Run the Application**:

Use Streamlit to launch the app with the following command:

```bash
streamlit run app.py
```

2. **Input Data**:

Fill out the form with your general health and lifestyle details (e.g., age, exercise habits, smoking history, etc.).

3. **Receive Feedback**:

The app will predict your risk level for **diabetes**, **heart disease**, and **obesity** based on the data you provide. It will also offer personalized advice based on the risk level.

## Folder Structure

```
├── images
│   ├── healthcare.webp
├── model
│   ├── label_encoders.pkl
│   ├── lr_dt.pkl
│   ├── lr_ht.pkl
│   ├── lr_ob.pkl
├── style
│   ├── style.css
├── app.py
├── README.md
├── requirements.txt
```

## Model Details

- **label_encoders.pkl**: Used to encode categorical data.
- **lr_dt.pkl**: Logistic Regression model for predicting the risk of diabetes.
- **lr_ht.pkl**: Logistic Regression model for predicting heart disease risk.
- **lr_ob.pkl**: Logistic Regression model for obesity risk.

## Acknowledgments

This application was developed as part of the **TechXcelerate 2024** challenge, focusing on developing a predictive healthcare system using machine learning and AI.

_will be adding two models, XGBoost and Naive Bayes, to the analysis of the diabetes dataset( diabetes data.csv) or enhanced predictive modeling._
>Sprint 2
focusing on developing a predictive healthcare system using machine learning and AI.
>Sprint 2
In this update to the Jupyter Notebook, the heart disease dataset analysis, I integrated two new models, the Gradient Boosting Classifier and the XGBoost Classifier, to enhance the dataset's predictive analysis. These models were trained on the resampled and scaled data, followed by evaluation metrics to compare their performance against previously implemented classifiers.
I created an app to predict the risk of diabetes: Diabetes Risk Calculator.
