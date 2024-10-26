# Multiple_Price_Prediction_Project

Welcome to the Price Prediction Project, an end-to-end solution for predicting prices across multiple categories. This project is divided into two main categories: Electronics Price Prediction and Vehicle Price Prediction, each with individual models tailored to specific types of products.

# Project Overview

>This project leverages various datasets from Kaggle and uses Machine Learning models to provide accurate price predictions based on user inputs. The interactive interface, built with Streamlit, allows users to select specifications and predict prices in real-time.

# Categories and Projects
>The project consists of two main categories, each containing multiple sub-projects:

1.Electronics Price Prediction

>Laptop Price Prediction (Model: Linear Regression)

>Mobile Price Prediction (Model: Linear Regression)

>Television Price Prediction (Model: Linear Regression)

>Camera Price Prediction (Model: Linear Regression)

2.Vehicle Price Prediction

>Car Price Prediction (Model: Linear Regression)

>Bike Price Prediction (Model: Random Forest Regression)

# Demo
>You can explore the live demo of this project here:

🔗 Check out the live demo here: [Price Prediction Project on Render](https://price-prediction-project.onrender.com/)


# Installation

>To run this project locally, please follow the steps below.

1.Clone the repository:

git clone https://github.com/msafridi1999/Multiple_Price_Prediction_Project.git
cd Multiple_Price_Prediction_Project

2.Install dependencies:
It is recommended to create a virtual environment and activate it before installing the dependencies.
pip install -r requirements.txt

3.Run the Streamlit app:
streamlit run app.py
The app should now be running on http://localhost:8501.

# Project Structure

.
├── Electronics
│   ├── Laptop_Price_Prediction
│   ├── Mobile_Price_Prediction
│   ├── Television_Price_Prediction
│   └── Camera_Price_Prediction
│
├── Vehicles
│   ├── Car_Price_Prediction
│   └── Bike_Price_Prediction
│
├── app.py              # Main application file for Streamlit
├── requirements.txt    # Python dependencies for the project
└── README.md           # Project documentation

# Usage
1.After running the app, a sidebar allows you to select between Electronics and Vehicles categories.

2.Select a project within the chosen category.

3.Input the specifications in the provided fields.

4.Click Predict Price to get an estimated price for the configuration.

# Example

1.Select "Electronics Price Prediction" in the sidebar.

2.Choose Laptop Price Prediction.

3.Enter specifications like RAM, screen size, CPU, etc.

4.Click Predict Price to see the estimated laptop price.

# Models Used
>Each project uses a specific model for price prediction:

1.Linear Regression: Used for Laptop, Mobile, Television, and Camera predictions.

2.Random Forest Regression: Used for Bike price prediction.

# Datasets

>The datasets used in this project are sourced from Kaggle and were preprocessed to create features suitable for price prediction. The datasets include relevant fields such as specifications and attributes that significantly impact the product prices.

# Technologies Used

1.Streamlit: For creating an interactive user interface.

2.Machine Learning: Models trained using scikit-learn for each sub-project.

3.Python: The primary programming language for the project.

4.Render: For deployment and hosting.

# Future Improvements

>Expanding product categories to include other electronics and vehicle types.

>Experimenting with more complex models for improved prediction accuracy.

>Adding feature importance analysis to understand the key price-driving features.

# Acknowledgments

>Special thanks to CampusX and Nitish Singh Sir for their support and guidance throughout my learning journey. Their teachings have been instrumental in building my knowledge in data science and machine learning.

# Contributing

If you’d like to contribute to this project, please fork the repository and make a pull request with your proposed changes. We welcome improvements and suggestions!
