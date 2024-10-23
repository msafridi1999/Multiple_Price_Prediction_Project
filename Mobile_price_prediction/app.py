import streamlit as st
import pickle
import pandas as pd
import numpy as np

# Load the saved Linear Regression model and other required components
lr_model = pickle.load(open('lr_model.pkl', 'rb'))
ohe = pickle.load(open('ohe.pkl', 'rb'))  # Load the OneHotEncoder used during training
data = pickle.load(open('data.pkl', 'rb'))

# Streamlit UI
st.title("Mobile Price Prediction App")
st.header("Enter mobile specifications to predict the price")

# Brand selection based on unique brand values used in the original dataset
brand_options = list(data['Brand me'].unique())
brand = st.selectbox("Brand", options=brand_options)

# User inputs for mobile features
ratings = st.number_input("Ratings (0-5)", min_value=0.0, max_value=5.0, value=4.0, step=0.1)
ram = st.number_input("RAM (GB)", min_value=0, max_value=64, value=6)
rom = st.number_input("ROM (GB)", min_value=0, max_value=512, value=64)
mobile_size = st.number_input("Mobile Size (inches)", min_value=4.0, max_value=7.0, value=6.5)
primary_cam = st.number_input("Primary Camera (MP)", min_value=2, max_value=108, value=48)
selfi_cam = st.number_input("Selfie Camera (MP)", min_value=0, max_value=64, value=13)
battery_power = st.number_input("Battery Power (mAh)", min_value=100, max_value=10000, value=4000)

# Prepare the input data as a DataFrame
input_data = pd.DataFrame({
    'Ratings': [ratings],
    'RAM': [ram],
    'ROM': [rom],
    'Mobile_Size': [mobile_size],
    'Primary_Cam': [primary_cam],
    'Selfi_Cam': [selfi_cam],
    'Battery_Power': [battery_power],
    'Brand me': [brand]
})

# Transform the 'Brand me' column using the trained OneHotEncoder
encoded_brand = ohe.transform(input_data[['Brand me']])

# Drop the 'Brand me' column and concatenate the encoded brand with other input features
input_data = input_data.drop('Brand me', axis=1)
input_data_encoded = pd.concat([input_data.reset_index(drop=True), 
                                pd.DataFrame(encoded_brand, columns=ohe.get_feature_names_out())], axis=1)

# Predict the price when the button is clicked
if st.button("Predict Price"):
    predicted_price = lr_model.predict(input_data_encoded)  # Predict using the linear regression model
    st.success(f"The predicted price is ₹{predicted_price[0]:,.2f}")
