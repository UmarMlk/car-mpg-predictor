import streamlit as st
import pickle
import numpy as np
import pandas as pd

# 1. Model Load Karein
# Ensure karein ke aapki pkl file ka naam wahi ho jo aapne step 1 mein rakha tha
try:
    with open('car_model.pkl', 'rb') as file:
        model = pickle.load(file)
except FileNotFoundError:
    st.error("Model file 'car_model.pkl' nahi mili. Pehle model save karein!")

st.set_page_config(page_title="Car MPG Predictor", page_icon="🚗")

st.title('🚗 Car Mileage (MPG) Predictor')
st.markdown("Is app ke zariye aap car ki specifications enter karke uski **Mileage (MPG)** check kar sakte hain.")

st.divider()

# 2. User Inputs (Columns ke hisab se)
col1, col2 = st.columns(2)

with col1:
    cylinders = st.selectbox('Cylinders', [3, 4, 5, 6, 8], index=1)
    displacement = st.number_input('Displacement (cu. in.)', min_value=50.0, max_value=500.0, value=150.0)
    horsepower = st.number_input('Horsepower', min_value=40.0, max_value=300.0, value=100.0)
    weight = st.number_input('Weight (lbs)', min_value=1500.0, max_value=6000.0, value=3000.0)

with col2:
    acceleration = st.number_input('Acceleration', min_value=5.0, max_value=25.0, value=15.0)
    model_year = st.slider('Model Year (1970 - 1982)', 70, 82, 76)
    origin = st.radio('Origin', ['America', 'Europe', 'Asia'])

# 3. Preprocessing (Categorical Data)
# Note: Agar aapke model ne One-Hot Encoding use ki thi to ye part change hoga.
# Filhal hum simple numerical mapping use kar rahe hain: America=1, Europe=2, Asia=3
origin_mapping = {'America': 1, 'Europe': 2, 'Asia': 3}
origin_val = origin_mapping[origin]

# 4. Prediction Button
# 3. Preprocessing (One-Hot Encoding handling)
# Model 9 features expect kar raha hai:
# [cylinders, displacement, horsepower, weight, acceleration, model_year, origin_america, origin_europe, origin_asia]

origin_america = 0
origin_europe = 0
origin_asia = 0

if origin == 'America':
    origin_america = 1
elif origin == 'Europe':
    origin_europe = 1
else:
    origin_asia = 1

# 4. Prediction Button
# 3. Preprocessing (One-Hot Encoding handling)
# Model 9 features expect kar raha hai:
# [cylinders, displacement, horsepower, weight, acceleration, model_year, origin_america, origin_europe, origin_asia]

origin_america = 0
origin_europe = 0
origin_asia = 0

if origin == 'America':
    origin_america = 1
elif origin == 'Europe':
    origin_europe = 1
else:
    origin_asia = 1

# 4. Prediction Button
if st.button('Predict Mileage'):
    # Ab hum 9 features bhej rahe hain model ko
    input_data = np.array([[
        cylinders, 
        displacement, 
        horsepower, 
        weight, 
        acceleration, 
        model_year, 
        origin_america, 
        origin_europe, 
        origin_asia
    ]])
    
    try:
        prediction = model.predict(input_data)
        st.success(f"### Predicted Mileage: **{round(prediction[0], 2)} MPG**")
    except Exception as e:
        st.error(f"Error: {e}")