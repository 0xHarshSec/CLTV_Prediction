# Import libraries
import streamlit as st
import pandas as pd
import numpy as np
import pickle

# Load the model from the pickle file
pickle_in = open("model.pkl", "rb")
model = pickle.load(pickle_in)

# Display the app title and description
st.title("CLTV Prediction App")
st.write("This app predicts the customer lifetime value (CLTV) of three months based on the past sales data. You can enter the values of the features for a new customer and get the predicted CLTV.")

# Display the input form for a new customer
st.subheader("Predict CLTV for a New Customer")
# Create input fields for each feature
sales_avg_M_2 = st.number_input("Average Sales in Month 2", 0.0, format="%.2f")
sales_avg_M_3 = st.number_input("Average Sales in Month 3", 0.0, format="%.2f")
sales_avg_M_4 = st.number_input("Average Sales in Month 4", 0.0, format="%.2f")
sales_avg_M_5 = st.number_input("Average Sales in Month 5", 0.0, format="%.2f")
sales_count_M_2 = st.number_input("Sales Count in Month 2", 0)
sales_count_M_3 = st.number_input("Sales Count in Month 3", 0)
sales_count_M_4 = st.number_input("Sales Count in Month 4", 0)
sales_count_M_5 = st.number_input("Sales Count in Month 5", 0)
sales_sum_M_2 = st.number_input("Sales Sum in Month 2", 0.0, format="%.2f")
sales_sum_M_3 = st.number_input("Sales Sum in Month 3", 0.0, format="%.2f")
sales_sum_M_4 = st.number_input("Sales Sum in Month 4", 0.0, format="%.2f")
sales_sum_M_5 = st.number_input("Sales Sum in Month 5", 0.0, format="%.2f")

# Create a button to make prediction
if st.button("Predict"):
    # Create a numpy array of the input values
    input_values = np.array([sales_avg_M_2, sales_avg_M_3, sales_avg_M_4, sales_avg_M_5,
                             sales_count_M_2, sales_count_M_3, sales_count_M_4, sales_count_M_5,
                             sales_sum_M_2, sales_sum_M_3, sales_sum_M_4, sales_sum_M_5]).reshape(1,-1)
    # Use the model to make prediction
    prediction = model.predict(input_values)[0]
    # Display the prediction result
    st.success(f"The predicted CLTV for the new customer is {prediction:.2f}")
