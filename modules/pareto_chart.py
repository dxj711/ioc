# pareto_chart.py
import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

def generate_pareto_chart(df):
    category_column_key = 'category_column_select'
    value_column1_key = 'value_column1_select'
    value_column2_key = 'value_column2_select'

    category_column = st.selectbox('Select category column', df.columns, key=category_column_key)
    value_column1 = st.selectbox('Select value column 1 (SKU)', df.columns, key=value_column1_key)
    value_column2 = st.selectbox('Select value column 2 (Quantity)', df.columns, key=value_column2_key)

    # Convert the data to numeric format
    df[value_column2] = pd.to_numeric(df[value_column2], errors='coerce')

    data = df.groupby(category_column)[value_column2].sum().sort_values(ascending=False)
    
    # Check if data length is zero to avoid division by zero
    if len(data) == 0:
        #st.error("No data available for Pareto chart generation.")
        return
    
    # Calculate percentage of SKU
    percentage_sku = (data / data.sum()) * 100
    
    # Calculate cumulative percentage of quantity
    cumulative_percentage = data.cumsum() / data.sum() * 100
    
    # Normalize category values to range between 0 and 1000
    normalized_categories = pd.Series(range(len(data)), index=data.index) * (1000 / len(data))
    
    fig, ax = plt.subplots()

    # Create bar plot for percentage of SKU
    ax.bar(normalized_categories, percentage_sku, color='C0', width=5, label='Percentage of SKU')

    # Create line plot for cumulative percentage of quantity
    ax2 = ax.twinx()
    ax2.plot(normalized_categories, cumulative_percentage, color='C1', marker='o', label='Cumulative Percentage of Quantity')

    # Set axis labels and title
    ax.set_xlabel(category_column)
    ax.set_ylabel('Percentage of SKU')
    ax2.set_ylabel('Cumulative Percentage of Quantity')
    plt.title('Pareto Chart')

    # Show legend
    ax.legend(loc='upper left')
    ax2.legend(loc='upper right')

    # Show plot
    if st.button('Create Pareto Chart'):
        st.pyplot(fig)
