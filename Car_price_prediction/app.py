import streamlit as st
import pickle
import pandas as pd
import numpy as np

# Load the model and the dataset
model = pickle.load(open('LinearRegression.pkl', 'rb'))
car = pd.read_csv('Cleaned_Car_data.csv')

# Display car image (you can replace the URL with a local image path if needed)
#st.image("https://images.app.goo.gl/iGCCgjucbExkowgVA", width=300)  # You can replace the URL with an actual image URL or path

# Streamlit app title
st.title("Car Price Predictor")

# Input parameters on the main page (similar to the television predictor UI)
company = st.selectbox('Company', car['company'].unique())

car_model = st.selectbox('Car Model', car['name'].unique())

year = st.selectbox('Year', sorted(car['year'].unique(), reverse=True))

fuel_type = st.selectbox('Fuel Type', car['fuel_type'].unique())

kms_driven = st.number_input('Kilometers Driven', min_value=0)

# Button for making the prediction
if st.button('Predict Price'):
    # Predict the price using the trained model
    query = np.array([car_model, company, year, kms_driven, fuel_type])
    query = query.reshape(1, 5)
    
    prediction = model.predict(pd.DataFrame(columns=['name', 'company', 'year', 'kms_driven', 'fuel_type'], data=query))
    
    # Show the prediction result
    st.title(f"The predicted price of the car is ₹{np.round(prediction[0], 2)}")
