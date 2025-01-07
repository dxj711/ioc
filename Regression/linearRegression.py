import streamlit as st
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import matplotlib.pyplot as plt
import numpy as np


def generate_linear_regression(df):
    
    st.write("DataFrame:")
    st.write(df)

    # Select features and target
    st.write("Select the feature columns (X) and the target column (y)")

    all_columns = df.columns.tolist()

    features = st.multiselect("Select feature columns (X)", all_columns)
    target = st.selectbox("Select target column (y)", all_columns)

    if st.button("Perform Linear Regression"):
        if features and target:
            X = df[features]
            y = df[target]

            # Split the data into training and testing sets
            X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

            # Feature scaling
            scaler = StandardScaler()
            X_train_scaled = scaler.fit_transform(X_train)
            X_test_scaled = scaler.transform(X_test)

            # Perform linear regression
            model = LinearRegression()
            model.fit(X_train_scaled, y_train)

            st.write("Intercept:", model.intercept_)
            st.write("Coefficients:", model.coef_)

            # Predicting the target
            y_pred_train = model.predict(X_train_scaled)
            y_pred_test = model.predict(X_test_scaled)

            # Evaluating the model
            st.write("Training Set Performance:")
            st.write("Mean Absolute Error (MAE):", mean_absolute_error(y_train, y_pred_train))
            st.write("Mean Squared Error (MSE):", mean_squared_error(y_train, y_pred_train))
            st.write("R-squared:", r2_score(y_train, y_pred_train))

            st.write("Testing Set Performance:")
            st.write("Mean Absolute Error (MAE):", mean_absolute_error(y_test, y_pred_test))
            st.write("Mean Squared Error (MSE):", mean_squared_error(y_test, y_pred_test))
            st.write("R-squared:", r2_score(y_test, y_pred_test))

            # Plotting the results
            fig, ax = plt.subplots()
            ax.scatter(range(len(y_test)), y_test, color='blue', label='Actual')
            ax.plot(range(len(y_test)), y_pred_test, color='red', linewidth=2, label='Predicted')
            ax.legend()
            ax.set_xlabel("Index")
            ax.set_ylabel(target)
            ax.set_title("Linear Regression: Actual vs Predicted")
            
            st.pyplot(fig)

        else:
            st.write("Please select the feature columns (X) and the target column (y).")
