import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

def generate_product_lifecycle(df):
    # Define the keys for Streamlit widgets
    month_column_key = 'month_column_select'
    sales_column_key = 'sales_column_select'
    stages_column_key = 'stages_column_select'
    
    # User selection for time periods (months) and sales figures
    month_column = st.selectbox('Select month column', df.columns, key=month_column_key)
    sales_column = st.selectbox('Select sales column', df.columns, key=sales_column_key)
    stages_column = st.selectbox('Select stages column', df.columns, key=stages_column_key)
    
    # Convert necessary columns to numeric
    df[month_column] = pd.to_numeric(df[month_column], errors='coerce')
    df[sales_column] = pd.to_numeric(df[sales_column], errors='coerce')
    
    # Extracting the data
    months = df[month_column].values
    sales = df[sales_column].values
    stages = df[stages_column].values
    
    # Create the figure and plot
    fig, ax = plt.subplots(figsize=(10, 6))
    
    # Line plot for sales
    ax.plot(months, sales, marker='o')
    
    # Color areas for different lifecycle stages
    unique_stages = df[stages_column].unique()
    colors = ['lightblue', 'lightgreen', 'yellow', 'salmon']
    for stage, color in zip(unique_stages, colors):
        ax.fill_between(months, sales, 0, where=(stages == stage), color=color, alpha=0.3, label=stage)
    
    # Adding labels and a title
    ax.set_xlabel('Month')
    ax.set_ylabel('Sales')
    ax.set_title('Product Lifecycle Analysis')
    ax.legend()
    
    # Show the plot
    if st.button('Create Product Lifecycle Analysis Chart'):
        st.pyplot(fig)
