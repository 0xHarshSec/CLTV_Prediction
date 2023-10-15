import streamlit as st
import pandas as pd
import pickle

# Load the model from the pickle file
pickle_in = open("model.pkl", "rb")
model = pickle.load(pickle_in)

# Define custom CSS for the gradient background
custom_css = f"""
<style>
    .custom-text-color {{
        color: #0B1B2D;
        }}
    .stApp {{
        background: linear-gradient(to bottom right, #F79256, #246EB9);
        color: #848FA5;
    }}
    .st-bc {{
        background-color: #BBE1C3;
        color: #272727;
    }}
    .st-cc {{
        color: #848FA5;
    }}
    .st-dh {{
        background-color: #272727;
    }}
    .st-cq {{
        background-color: #BBE1C3;
        color: #272727;
    }}
</style>
"""

# Set page title and icon
st.set_page_config(
    page_title="CLTV Prediction App",
    page_icon="💰",
)

# Inject custom CSS
st.markdown(custom_css, unsafe_allow_html=True)

# Display the app title and description
st.title("Customer Lifetime Value (CLTV) Prediction App")
st.write("This app predicts the customer lifetime value (CLTV) of three months based on past sales data. Upload a CSV or XLSX file containing the required features to make predictions for each row.")

# Upload a CSV or XLSX file
uploaded_file = st.file_uploader("Upload a CSV or XLSX file", type=["csv", "xlsx"])

if uploaded_file is not None:
    # Read the uploaded file into a DataFrame
    df = pd.read_csv(uploaded_file) if uploaded_file.name.endswith('csv') else pd.read_excel(uploaded_file)

    # Check if the required features exist in the uploaded file
    required_features = [
        'sales_avg_M_2', 'sales_avg_M_3', 'sales_avg_M_4', 'sales_avg_M_5',
        'sales_count_M_2', 'sales_count_M_3', 'sales_count_M_4', 'sales_count_M_5',
        'sales_sum_M_2', 'sales_sum_M_3', 'sales_sum_M_4', 'sales_sum_M_5'
    ]

    if all(feature in df.columns for feature in required_features):
        # Create an empty list to store predictions
        predictions = []

        # Iterate through the rows and make predictions
        for index, row in df.iterrows():
            features = row[required_features]
            prediction = model.predict([features])[0]
            predictions.append(prediction)

        # Add the predictions to the DataFrame
        df['CLTV_Predicted'] = predictions

        # Display the DataFrame with predictions
        st.subheader("Predicted CLTV for Each Row in the Uploaded Data")
        st.dataframe(df.style.set_properties(subset=["CLTV_Predicted"], **{'background-color': '#0B1B2D'}))

    else:
        st.error("Some required features are missing in the uploaded file. Please make sure the file contains all the required features.")
