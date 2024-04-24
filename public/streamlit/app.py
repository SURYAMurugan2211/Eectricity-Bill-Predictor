import streamlit as st
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

# Load and preprocess the dataset
df = pd.read_csv("C:\Frontend_and_Backend\Backend_Mlops\Django\streamlit\electricity_bill_dataset1.csv")  # Update the path to your dataset
# Assuming you have 'MonthlyHours' and 'electricitybill' columns in your dataset
X = df.iloc[:,[0,1,3,9]]  # Feature: MonthlyHours
y = df.iloc[:,-1]  # Target: electricitybill

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=1)

# Initialize the Linear Regression model
model = LinearRegression()

# Train the Linear Regression model
model.fit(X_train, y_train)

# Define prediction function
def predict(Fan,Refrigerator,Television,MonthlyHours):
    prediction = model.predict([[Fan,Refrigerator,Television,MonthlyHours]])
    return prediction[0]

# Streamlit UI
st.title("Electricity Bill Prediction")
st.write("Predicts electricity bill on this features:")

# Input components
Fan = st.number_input("Fan")
Refrigerator = st.number_input("Refrigerator")
Television = st.number_input("Television")
MonthlyHours = st.number_input("MonthlyHours")
# Prediction button
if st.button("Predict"):
    prediction = predict(Fan,Refrigerator,Television,MonthlyHours)
    st.write(f"Predicted Electricity Bill: {prediction}")
