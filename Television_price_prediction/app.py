import streamlit as st
import pandas as pd
import numpy as np
import pickle

# Set the title of the app
st.title("📺 Television Price Prediction")

# Add a brief description
st.write(""" ### Enter the details of the television to predict its price. """)

# Load the model
pipe = pickle.load(open('pipe_model.pkl', 'rb'))
df = pickle.load(open('df_tv.pkl', 'rb'))

# Brand
brand = st.selectbox('Brand', df['Brand'].unique())

# Resolution
resolution = st.selectbox('Resolution', df['Resolution'].unique())

# Screen Size
size = st.selectbox('Size (in inches)', df['Size'].unique())

# Operating System
operating_system = st.selectbox('Operating System', df['Operating System'].unique())

# Rating
rating = st.selectbox('Rating', df['Rating'].unique())

# Predict button
if st.button('Predict Price'):
    # Create a query array
    query = np.array([brand, resolution, size, operating_system, rating])
    query = query.reshape(1, 5)
    
    # Predict the price
    predicted_price = pipe.predict(query)[0]
    
    # Display the predicted price
    st.title(f"The predicted price of this configuration is ₹{int(predicted_price)}")