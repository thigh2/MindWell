import pickle
from sklearn.preprocessing import LabelEncoder
import pandas as pd
import streamlit as st
import requests
from streamlit_lottie import st_lottie
from PIL import Image


st.set_page_config(page_title="Preventive Healthcare System ", page_icon="", layout="wide")

def load_lottie_url(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

#Use Local CSS


def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>",unsafe_allow_html=True)

local_css("style/style.css")

def load_pickle_model(file_path):
    try:
        with open(file_path, 'rb') as file:
            model = pickle.load(file)
        print(f"Model loaded successfully from {file_path}")
        return model
    except FileNotFoundError:
        print(f"Error: The file {file_path} was not found.")
    except Exception as e:
        print(f"An error occurred while loading the model: {e}")

def get_risk_level(prob):
    if prob < 0.3:
        return "Low"
    elif 0.3 <= prob < 0.7:
        return "Moderate"
    else:
        return "High"

def generate_feedback(diabetes_prob, heart_disease_prob):
    feedback = {}

    # Risk assessment
    feedback['diabetes'] = f"Diabetes Risk: {get_risk_level(diabetes_prob)}. Probability: {diabetes_prob:.2f}"
    feedback['heart_disease'] = f"Heart Disease Risk: {get_risk_level(heart_disease_prob)}. Probability: {heart_disease_prob:.2f}"

    # Suggestions based on risk levels
    if get_risk_level(diabetes_prob) == 'High':
        feedback['diabetes_advice'] = "You are at a high risk for diabetes. Consider regular checkups, maintaining a balanced diet, and exercising regularly."
    elif get_risk_level(diabetes_prob) == 'Moderate':
        feedback['diabetes_advice'] = "You have a moderate risk of diabetes. It's recommended to monitor your sugar intake and stay active."

    if get_risk_level(heart_disease_prob) == 'High':
        feedback['heart_disease_advice'] = "You are at a high risk for heart disease. Regular cardiovascular exercise and a heart-healthy diet are recommended."

    return feedback


# --- Load assets ---
lottie_coding = load_lottie_url("https://lottie.host/d03b4e9d-a139-4df4-8f84-fb4c358891e9/gRBlHPnlpx.json")
img_contact_form = Image.open("images\\healthcare.webp")
# img_lottie_animation = Image.open("images\\pic3.jpeg")


# --- Header section ---
with st.container():
    st.title("Test How Healthy You Are ! ")
    st.title("Let's check with us ")
    st.write("")
    st.write("")

# --- What I Do ---
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    
    with left_column:
        st.header("AI Power Predictive healthcare System ")
        st.write("##")
        st.write("""
            An AI-powered solution that proactively identifies individuals at risk
of developing chronic diseases such as diabetes, heart disease, or obesity.
The system should provide personalized recommendations for preventive
care based on genetic, lifestyle, and medical data.
        """)
        

    with right_column:
        st_lottie(lottie_coding, height=300, key="coding")

#---services---

with st.container():
    st.write("---")
    st.header("Our Services")
    st.write("##")
    image_column, text_column = st.columns((1, 2))
    # image_column,text_column=st.columns((1,2))
    with image_column:
        st.image(img_contact_form)
    with text_column:
        st.subheader("We Specialize In Managing Chronic Diseases and Promoting Healthy Lifestyles")
        st.write(
            """
            Our healthcare services focus on helping you manage and prevent chronic diseases while promoting a healthy lifestyle. Our areas of specialization include:
            - **Diabetes Management**: Comprehensive care to monitor and control blood sugar levels.
            - **Heart Disease Prevention**: Lifestyle recommendations and medical interventions to reduce heart disease risk.
            - **Obesity Management**: Personalized plans to achieve and maintain a healthy weight.
            - **Lifestyle Modifications**: Guidance on exercise, diet, and wellness to promote overall health and well-being.
            """
        )



    
#     with text_column:
#         st.subheader("Integrate lottie animations inside your streamlit app")
#         st.write(
#             """
#              jhxsyfdahF
#              HDJGhfkhFyyfTF
#              IJHDGGFDyJFklgj
#              HDYUGFEUHF
#              JgdfdHKD
#              gwyuqwjkJdgd

#             """
#         )    
#         st.markdown("[Watch Video...](https://youtu.be/TXS0itGoINE)")

# ---container---

# with st.container():
#     st.write("---")
#     st.header("Get in Touch with us")
#     st.write("#")

#     contact_form="""

#     <form action="https://formsubmit.co/nimishajain2206@email.com" method="POST">
#     <input type ="hidden " name ="_captcha" value="">
#      <input type="text" name="name" palceholder ="Your Name"required>
#      <input type="email" name="email" placeholder ="Your Email" required>
#      <textarea name ="message " placeholder ="Your message here" required></textarea>
#      <button type="submit">Send</button>
#     </form>
#                  """
    
#     left_column,right_column=st.columns(2)
#     with left_column:
#         st.markdown(contact_form,unsafe_allow_html=True)
#     with right_column:
#         st.empty()
    

lbl_encoders = load_pickle_model('model\\label_encoders.pkl')
lr_dt = load_pickle_model('model\\lr_dt.pkl')
lr_ht = load_pickle_model('model\\lr_ht.pkl')
lr_ob = load_pickle_model('model\\lr_ob.pkl')

# Define categorical columns
categorical_columns = ['General_Health', 'Checkup', 'Exercise', 'Depression', 
                       'Arthritis', 'Sex', 'Age_Category', 'Smoking_History']

# Define the columns
columns = ['General_Health', 'Checkup', 'Exercise', 'Depression', 'Arthritis', 
           'Sex', 'Age_Category', 'Height_(cm)', 'Weight_(kg)', 'BMI', 
           'Smoking_History', 'Alcohol_Consumption', 'Fruit_Consumption', 
           'Green_Vegetables_Consumption', 'FriedPotato_Consumption']

# Create the form in Streamlit
st.title("Health Data Prediction Form")

with st.form(key="input_form"):
    # Collect input values from the user
    general_health = st.selectbox('General Health', ['Poor', 'Fair', 'Good', 'Very Good', 'Excellent'])
    checkup = st.selectbox('Checkup', ['Within the past year', 'Within the past 2 years', '5 or more years ago', 'Never'])
    exercise = st.selectbox('Exercise', ['Yes', 'No'])
    depression = st.selectbox('Depression', ['Yes', 'No'])
    arthritis = st.selectbox('Arthritis', ['Yes', 'No'])
    sex = st.selectbox('Sex', ['Male', 'Female'])
    age_category = st.selectbox('Age Category', ['18-24', '25-29', '30-34', '35-39', '40-44', '45-49', '50-54', 
                                                 '55-59', '60-64', '65-69', '70-74', '75-79', '80 or older'])
    height = st.number_input('Height (cm)', min_value=100.0, max_value=250.0, step=1.0)
    weight = st.number_input('Weight (kg)', min_value=20.0, max_value=200.0, step=0.1)
    bmi = st.number_input('BMI', min_value=10.0, max_value=60.0, step=0.1)
    smoking_history = st.selectbox('Smoking History', ['Yes', 'No'])
    alcohol_consumption = st.number_input('Alcohol Consumption', min_value=0.0, max_value=100.0, step=0.1)
    fruit_consumption = st.number_input('Fruit Consumption (grams/day)', min_value=0.0, max_value=500.0, step=1.0)
    green_vegetables_consumption = st.number_input('Green Vegetables Consumption (grams/day)', min_value=0.0, max_value=500.0, step=1.0)
    fried_potato_consumption = st.number_input('Fried Potato Consumption (grams/day)', min_value=0.0, max_value=500.0, step=1.0)

    # Submit button
    submit_button = st.form_submit_button(label="Submit")

if submit_button:
    # Define the input values
    input_values = {
        'General_Health': general_health,
        'Checkup': checkup,
        'Exercise': exercise,
        'Depression': depression,
        'Arthritis': arthritis,
        'Sex': sex,
        'Age_Category': age_category,
        'Height_(cm)': height,
        'Weight_(kg)': weight,
        'BMI': bmi,
        'Smoking_History': smoking_history,
        'Alcohol_Consumption': alcohol_consumption,
        'Fruit_Consumption': fruit_consumption,
        'Green_Vegetables_Consumption': green_vegetables_consumption,
        'FriedPotato_Consumption': fried_potato_consumption
    }

    # Create a DataFrame from the input values

    input_df = pd.DataFrame([input_values])

    # Encode categorical columns using the stored LabelEncoders
    for column in categorical_columns:
        if column in input_df.columns:
            input_df[column] = lbl_encoders[column].transform(input_df[column].astype(str))

    # Display the input DataFrame after encoding
    # st.write("Encoded Input DataFrame:")
    # st.write(input_df)

    # Predict using the model
    pred_dt = lr_dt.predict_proba(input_df)[0]
    pred_ht = lr_ht.predict_proba(input_df)[0]
    pred_ob = lr_ob.predict(input_df)
    print(pred_dt)
    print(pred_ht)
    print(pred_ob)

    # Display the prediction result
    st.write(f"Diabetes: {pred_dt[0]}")
    st.write(f"Hearts Decises: {pred_ht[0]}")
    st.write(f"Obesitiy: {pred_ob[0]}")
    st.title("Health Risk Assessment")
    feedback = feedback = generate_feedback(pred_dt[0], pred_ht[0])

    # Display the feedback
    for key, value in feedback.items():
        st.write(value)


