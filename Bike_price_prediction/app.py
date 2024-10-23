import streamlit as st
import pickle
import pandas as pd
import numpy as np

# Load the model and the dataset
model = pickle.load(open('RandomForestRegressionModel.pkl', 'rb'))
bike = pickle.load(open('bike.pkl', 'rb'))

# Clean column names by stripping extra spaces or tabs
bike.columns = bike.columns.str.strip()

# Streamlit app title
st.title("Bike Price Predictor")

# Input parameters on the main page (similar to the television predictor UI)
company = st.selectbox('Company', bike['company'].unique())

Engine_warranty = st.selectbox('Engine Warranty', bike['Engine_warranty'].unique())

Engine_type = st.selectbox('Engine Type', bike['Engine_type'].unique())

Fuel_type = st.selectbox('Fuel Type', bike['Fuel_type'].unique())

Cubic_capacity = st.selectbox('Cubic Capacity (in cc)', bike['Cubic_capacity'].unique())

Fuel_capacity = st.selectbox('Fuel Capacity (in liters)', bike['Fuel_Capacity'].unique())

# Button for making the prediction
if st.button('Predict Price'):
    # Predict the price using the trained model
    query = np.array([company, Engine_warranty, Engine_type, Fuel_type, Cubic_capacity, Fuel_capacity])
    query = query.reshape(1, 6)
    
    prediction = model.predict(pd.DataFrame(columns=['company', 'Engine_warranty', 'Engine_type', 'Fuel_type', 'Cubic_capacity', 'Fuel_Capacity'], data=query))
    
    # Show the prediction result
    st.title(f"The predicted price of the bike is ₹{np.round(prediction[0], 2)}")
