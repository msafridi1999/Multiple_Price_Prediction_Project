import streamlit as st
import pickle
import numpy as np
import pandas as pd

# Load the pre-trained model and data encoders
model = pickle.load(open('LinearRegressionModel.pkl', 'rb'))
df = pickle.load(open('camera.pkl', 'rb'))

# Set the title of the Streamlit app
st.title('Camera Price Prediction App')

# Collect user input for each feature required for prediction
def get_user_input():
    model = st.selectbox('Camera Model', df['Model'].unique())
    release_date = st.selectbox('Release Date', df['Release date'].unique())
    max_resolution = st.selectbox('Max Resolution', df['Max resolution'].unique())
    low_resolution = st.selectbox('Low Resolution', df['Low resolution'].unique())
    effective_pixels = st.selectbox('Effective Pixels (in MP)', df['Effective pixels'].unique())
    zoom_wide = st.selectbox('Zoom Wide (W)', df['Zoom wide (W)'].unique())
    zoom_tele = st.selectbox('Zoom Tele (T)', df['Zoom tele (T)'].unique())
    normal_focus_range = st.selectbox('Normal Focus Range', df['Normal focus range'].unique())
    macro_focus_range = st.selectbox('Macro Focus Range', df['Macro focus range'].unique())
    storage_included = st.selectbox('Storage Included (in MB)', df['Storage included'].unique())
    weight_inc_batteries = st.selectbox('Weight (including batteries) in grams', df['Weight (inc. batteries)'].unique())
    dimensions = st.selectbox('Dimensions (in mm)', df['Dimensions'].unique())

    # Store inputs into a dictionary
    user_data = {
        'Model': model,
        'Release date': release_date,
        'Max resolution': max_resolution,
        'Low resolution': low_resolution,
        'Effective pixels': effective_pixels,
        'Zoom wide (W)': zoom_wide,
        'Zoom tele (T)': zoom_tele,
        'Normal focus range': normal_focus_range,
        'Macro focus range': macro_focus_range,
        'Storage included': storage_included,
        'Weight (inc. batteries)': weight_inc_batteries,
        'Dimensions': dimensions
    }

    # Convert the user input to a DataFrame
    features = pd.DataFrame(user_data, index=[0])
    
    return features

# Get user input
user_input_df = get_user_input()

# Predict the price
if st.button('Predict Price'):
    prediction = model.predict(user_input_df)

    # Display the price in Indian Rupees (assuming the predicted price is in rupees already)
    st.subheader(f'Estimated Camera Price: ₹{prediction[0]:,.2f}')
