import streamlit as st
import google.genai as genai

google_api_key = st.secrets["google"]["api_key"]

client = genai.Client(api_key = google_api_key)

st.title("Welcome to the AI Health Assistant")
st.title("BMI Calculator with AI Nutritionist")

st.title("_AI_ is :blue[cool] :sunglasses:")

# Input fields for height and weight
name = st.text_input("Enter Your name", key="name")
ht = st.slider("Enter your height in meters:", min_value=1.0, max_value= 2.5, step=0.1)
wt = st.slider("Enter your weight in kilograms:", min_value=1.0, max_value=300.0, step=0.1)
gender = st.selectbox("Select your gender:", ["Male", "Female"])

# Calculate BMI
if st.button("Calculate BMI"):
    bmi = wt / (ht ** 2)
    st.write(f"Your BMI is: {bmi:.2f}")
    prompt = f"Great {name} and Act like an expert nutritionist, evaluate the {bmi} and share a diet chart"

# Generate content from Gemini
response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents= prompt)

st.write(response.text)
