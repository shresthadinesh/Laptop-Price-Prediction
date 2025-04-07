import streamlit as st
import pickle
import numpy as np

# Load the model and data
pipe = pickle.load(open('pipe.pkl', 'rb'))
df = pickle.load(open('df.pkl', 'rb'))

# App Title
st.set_page_config(page_title="Laptop Price Predictor", layout="centered")
st.title("💻 Laptop Price Predictor")
st.write("Get an instant estimate for your desired laptop configuration.")

# User Inputs
company = st.selectbox('Brand', df['Company'].unique())
typename = st.selectbox('Laptop Type', df['TypeName'].unique())
ram = st.selectbox('RAM (in GB)', [2, 4, 6, 8, 12, 16, 24, 32, 64])
weight = st.number_input('Weight of the Laptop (in kg)', min_value=0.5, max_value=5.0, value=2.0)
touchscreen = st.selectbox('Touchscreen', ['No', 'Yes'])
ips = st.selectbox('IPS Display', ['No', 'Yes'])
screen_size = st.slider('Screen Size (in inches)', 10.0, 18.0, 13.3)
resolution = st.selectbox('Screen Resolution', [
    '1920x1080', '1366x768', '1600x900', '3840x2160',
    '3200x1800', '2880x1800', '2560x1600', '2560x1440', '2304x1440'
])
cpu = st.selectbox('CPU Brand', df['Cpu Brand'].unique())
hdd = st.selectbox('HDD (in GB)', [0, 128, 256, 512, 1024, 2048])
ssd = st.selectbox('SSD (in GB)', [0, 8, 128, 256, 512, 1024])
gpu = st.selectbox('GPU Brand', df['Gpu Brand'].unique())
os = st.selectbox('Operating System', df['Operating System'].unique())

# Predict Button
import pandas as pd 

if st.button('🔍 Predict Laptop Price'):
    # Convert features
    touchscreen_val = 1 if touchscreen == 'Yes' else 0
    ips_val = 1 if ips == 'Yes' else 0

    # Calculate PPI
    X_res = int(resolution.split('x')[0])
    Y_res = int(resolution.split('x')[1])
    ppi = ((X_res**2) + (Y_res**2)) ** 0.5 / screen_size

    # Create input DataFrame with correct column names
    input_df = pd.DataFrame([[company, typename, ram, weight, touchscreen_val,
                               ips_val, ppi, cpu, hdd, ssd, gpu, os]],
                            columns=['Company', 'TypeName', 'Ram', 'Weight',
                                     'Touchscreen', 'IPS', 'PPI', 'Cpu Brand',
                                     'HDD', 'SSD', 'Gpu Brand', 'Operating System'])

    # Make prediction
    predicted_price = int(np.exp(pipe.predict(input_df)[0]))

    # Display result
    st.success(f"💰 Estimated Price:  {predicted_price:,}")
