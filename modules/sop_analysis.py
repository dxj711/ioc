import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

def generate_sop_analysis(df):
    # Streamlit app title
    #st.title('Sales and Operations Planning (S&OP) Analysis')

    # Display the data for reference
    st.write("Uploaded Data:", df)
    
    # Select columns for the different datasets
    columns = df.columns.tolist()
    month_column = st.selectbox("Select the column for months", columns)
    forecasted_sales_column = st.selectbox("Select the column for forecasted sales", columns)
    actual_sales_column = st.selectbox("Select the column for actual sales", columns)
    production_column = st.selectbox("Select the column for production", columns)
    
    # Extract the selected columns
    months = df[month_column]
    forecasted_sales = df[forecasted_sales_column]
    actual_sales = df[actual_sales_column]
    production = df[production_column]
    
    # Plotting the data
    fig, ax1 = plt.subplots()
    
    # Bar chart for production levels
    ax1.bar(months, production, color='gray', alpha=0.6, label='Production')
    ax1.set_xlabel('Month')
    ax1.set_ylabel('Production Units')
    ax1.set_title('Sales and Operations Planning (S&OP) Analysis')
    
    # Set x-axis ticks and labels
    ax1.set_xticks(months)  # Set the ticks
    ax1.set_xticklabels(months, rotation=90)  # Set the labels with rotation
    
    # Create a second y-axis for the sales numbers
    ax2 = ax1.twinx()
    ax2.plot(months, forecasted_sales, color='blue', marker='o', label='Forecasted Sales')
    ax2.plot(months, actual_sales, color='red', marker='o', label='Actual Sales')
    ax2.set_ylabel('Sales Units')
    
    # Adding legend
    fig.legend(loc='upper left', bbox_to_anchor=(0.1, 0.9))
    
    # Display the plot
    st.pyplot(fig)
