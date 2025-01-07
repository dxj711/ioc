# modules/risk_analysis.py

import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

def generate_risk_analysis(df):
    # Get the columns from the DataFrame
    category_column_key = 'category_column_select'
    value_column1_key = 'value_column1_select'
    value_column2_key = 'value_column2_select'

    category_column = st.selectbox('Select category column', df.columns, key=category_column_key)
    value_column1 = st.selectbox('Select value column 1 (Likelihood)', df.columns, key=value_column1_key)
    value_column2 = st.selectbox('Select value column 2 (Impact)', df.columns, key=value_column2_key)

    # Convert the data to numeric format
    df[value_column1] = pd.to_numeric(df[value_column1], errors='coerce')
    df[value_column2] = pd.to_numeric(df[value_column2], errors='coerce')

    # Drop rows with NaN values in the selected columns
    df = df.dropna(subset=[value_column1, value_column2, category_column])

    # Check if there is data after cleaning
    if df.empty:
        #st.error("No data available for the selected columns after cleaning. Please check your data.")
        return

    # Display the cleaned data for debugging
    st.write("Cleaned Data for Risk Analysis:")
    st.dataframe(df[[category_column, value_column1, value_column2]])

    # Create a scatter plot
    fig, ax = plt.subplots(figsize=(8, 6))
    scatter = ax.scatter(df[value_column1], df[value_column2], c=df[value_column2] * df[value_column1], cmap='Reds', s=100, edgecolor='black')

    # Adding annotations for risk labels
    for i, label in enumerate(df[category_column]):
        ax.annotate(label, (df[value_column1].iloc[i], df[value_column2].iloc[i]), textcoords="offset points", xytext=(0,10), ha='center')

    # Set up the color bar
    cbar = plt.colorbar(scatter)
    cbar.set_label('Risk Score (Impact * Likelihood)')

    # Set axes limits
    ax.set_xlim(0, 6)
    ax.set_ylim(0, 6)

    # Adding labels, title, and grid
    ax.set_xlabel('Likelihood')
    ax.set_ylabel('Impact')
    ax.set_title('Risk Assessment and Mitigation Analysis')
    ax.set_xticks([1, 2, 3, 4, 5])
    ax.set_yticks([1, 2, 3, 4, 5])
    ax.grid(True)

    # Show the plot
    if st.button('Generate Risk Analysis'):
        st.pyplot(fig)
