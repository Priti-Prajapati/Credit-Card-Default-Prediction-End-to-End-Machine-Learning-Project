import pickle

import streamlit as st
import pandas as pd
import numpy as np

with open('Models/model.pkl', 'rb') as file: 
        model = pickle.load(file)


x = pd.read_csv('Data/cleandata/clean.csv')


st.title("Credit Risk Prediction App")
st.markdown("Predict default risk based on customer financial and demographic data.")

# User Input
st.header("Enter Customer Details")

LIMIT_BAL = st.number_input("Limit Balance (Amount of credit given)", x['LIMIT_BAL'].min(), x['LIMIT_BAL'].max())
SEX = st.selectbox("Sex (1 = male; 2 = female)", [1, 2])
EDUCATION = st.selectbox("Education (1 = graduate school; 2 = university; 3 = high school; 4 = others;5=unkown;6=unkown)", [1, 2, 3, 4,5,6])
MARRIAGE = st.selectbox("Marriage Status (1 = married; 2 = single; 3 = others)", [1, 2, 3])
AGE = st.slider("Age",18, 100, 30)

#('age',x['Age'].min),x['Age'].max(),30)

st.subheader("Recent Repayment Status (Last 6 months)")
PAY_0 = st.number_input("Repayment in September (PAY_0)", min_value=-2, max_value=8)
PAY_2 = st.number_input("Repayment in August (PAY_2)", min_value=-2, max_value=8)
PAY_3 = st.number_input("Repayment in July (PAY_3)", min_value=-2, max_value=8)
PAY_4 = st.number_input("Repayment in June (PAY_4)", min_value=-2, max_value=8)
PAY_5 = st.number_input("Repayment in May (PAY_5)", min_value=-2, max_value=8)
PAY_6 = st.number_input("Repayment in April (PAY_6)", min_value=-2, max_value=8)

st.subheader("Bill Amount for Last 6 Months")
BILL_AMT1 = st.number_input("Bill Amount in September", value=0.0)
BILL_AMT2 = st.number_input("Bill Amount in August", value=0.0)
BILL_AMT3 = st.number_input("Bill Amount in July", value=0.0)
BILL_AMT4 = st.number_input("Bill Amount in June", value=0.0)
BILL_AMT5 = st.number_input("Bill Amount in May", value=0.0)
BILL_AMT6 = st.number_input("Bill Amount in April", value=0.0)

st.subheader("Payment Amount for Last 6 Months")
PAY_AMT1 = st.number_input("Payment in September", value=0.0)
PAY_AMT2 = st.number_input("Payment in August", value=0.0)
PAY_AMT3 = st.number_input("Payment in July", value=0.0)
PAY_AMT4 = st.number_input("Payment in June", value=0.0)
PAY_AMT5 = st.number_input("Payment in May", value=0.0)
PAY_AMT6 = st.number_input("Payment in April", value=0.0)

# Prepare input for model
input_data = np.array([[LIMIT_BAL, SEX, EDUCATION, MARRIAGE, AGE,
                        PAY_0, PAY_2, PAY_3, PAY_4, PAY_5, PAY_6,
                        BILL_AMT1, BILL_AMT2, BILL_AMT3, BILL_AMT4, BILL_AMT5, BILL_AMT6,
                        PAY_AMT1, PAY_AMT2, PAY_AMT3, PAY_AMT4, PAY_AMT5, PAY_AMT6]])

if st.button("Predict Default Risk"):
    prediction = model.predict(input_data)
    if prediction[0] == 1:
        st.error("⚠ High risk of default!")
    else:
        st.success("✅ Low risk of default.")

