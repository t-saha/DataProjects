# app.py
import streamlit as st
import joblib
import numpy as np

# Load model
model = joblib.load('/Users/titassaha/code/rain_model.pkl')

st.title("Rain Prediction App 🌧️☀️")
st.write("Enter today's weather data:")

# User input
pressure = st.number_input("Pressure (hPa)", min_value=800.0, max_value=1100.0)
temperature = st.number_input("Temperature (°C)", min_value=-50.0, max_value=60.0)
humidity = st.number_input("Humidity (%)", min_value=0.0, max_value=100.0)
cloud = st.number_input("Cloud", min_value = 1, max_value = 100)
sunshine = st.number_input("Sunshine", min_value = 0, max_value =1)
winddirection = st.number_input("Wind Direction (degrees)", min_value=0.0, max_value=360.0)
windspeed = st.number_input("Windspeed (km/h)", min_value=0.0, max_value=200.0)

if st.button("Predict"):
    input_data = np.array([[pressure, temperature, humidity, cloud, sunshine, winddirection, windspeed]])
    prediction = model.predict(input_data)
    result = "🌧️ Rain" if prediction[0] == 1 else "☀️ No Rain"
    st.success(f"Prediction: {result}")
