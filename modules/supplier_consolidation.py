import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd

def generate_supplier_consolidation(df):
    # Define the keys for Streamlit widgets
    supplier_column_key = 'supplier_column_select'
    spending_before_column_key = 'spending_before_column_select'
    spending_after_column_key = 'spending_after_column_select'
    category_column_key = 'category_column_select'
    spending_percentage_column_key = 'spending_percentage_column_select'

    # User selection for supplier columns and spending data
    supplier_column = st.selectbox('Select Supplier column', df.columns, index=0, key=supplier_column_key)
    spending_before_column = st.selectbox('Select Spending Before Consolidation column', df.columns, index=1, key=spending_before_column_key)
    spending_after_column = st.selectbox('Select Spending After Consolidation column', df.columns, index=2, key=spending_after_column_key)
    category_column = st.selectbox('Select Category column', df.columns, index=3, key=category_column_key)
    spending_percentage_column = st.selectbox('Select Spending Percentage column', df.columns, index=4, key=spending_percentage_column_key)

    # Convert necessary columns to numeric
    df[spending_before_column] = pd.to_numeric(df[spending_before_column], errors='coerce')
    df[spending_after_column] = pd.to_numeric(df[spending_after_column], errors='coerce')
    df[spending_percentage_column] = pd.to_numeric(df[spending_percentage_column], errors='coerce')

    # Create the figure and subplots
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))

    # Bar chart for supplier spending
    ax1.bar(df[supplier_column], df[spending_before_column], width=0.4, label='Before Consolidation', color='blue', alpha=0.6)
    ax1.bar(df[supplier_column], df[spending_after_column], width=0.4, label='After Consolidation', color='green', alpha=0.6, bottom=df[spending_before_column])
    ax1.set_title('Supplier Spending Before and After Consolidation')
    ax1.set_ylabel('Spending ($000s)')
    ax1.legend()

    # Pie chart for spending by category
    ax2.pie(df[spending_percentage_column], labels=df[category_column], autopct='%1.1f%%', startangle=90, colors=['gold', 'lightblue', 'lightgreen', 'salmon'])
    ax2.set_title('Spending by Category After Consolidation')
    ax2.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

    # Show the plot
    if st.button('Create Supplier Consolidation Analysis Chart'):
        st.pyplot(fig)
