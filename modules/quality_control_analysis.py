import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd

def generate_quality_analysis(df):
    # Define the keys for Streamlit widgets
    defect_column_key = 'defect_column_select'
    frequency_column_key = 'frequency_column_select'
    month_column_key = 'month_column_select'
    pass_rate_column_key = 'pass_rate_column_select'
    
    # User selection for defect types and their frequencies
    defect_column = st.selectbox('Select defect type column', df.columns, key=defect_column_key)
    frequency_column = st.selectbox('Select frequency column', df.columns, key=frequency_column_key)
    
    # User selection for monthly inspection pass rates
    month_column = st.selectbox('Select month column', df.columns, key=month_column_key)
    pass_rate_column = st.selectbox('Select pass rate column', df.columns, key=pass_rate_column_key)
    
    # Convert necessary columns to numeric
    df[frequency_column] = pd.to_numeric(df[frequency_column], errors='coerce')
    df[pass_rate_column] = pd.to_numeric(df[pass_rate_column], errors='coerce')
    
    # Data preparation for the bar chart
    defect_data = df.groupby(defect_column)[frequency_column].sum()
    
    # Data preparation for the line chart
    pass_rate_data = df.groupby(month_column)[pass_rate_column].mean()
    
    # Ensure the months are sorted correctly if they are strings like 'Jan', 'Feb', etc.
    pass_rate_data = pass_rate_data.reindex(sorted(pass_rate_data.index), fill_value=0)
    
    # Create the figure and subplots
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))
    
    # Bar chart for types of defects
    ax1.bar(defect_data.index, defect_data.values, color='salmon')
    ax1.set_title('Frequency of Defect Types')
    ax1.set_xlabel('Defect Type')
    ax1.set_ylabel('Frequency')
    ax1.set_ylim(0, defect_data.max() + 30)  # Set y-axis limits to make the chart cleaner
    
    # Line chart for inspection pass rates
    ax2.plot(pass_rate_data.index, pass_rate_data.values, marker='o', linestyle='-', color='green')
    ax2.set_title('Monthly Inspection Pass Rates')
    ax2.set_xlabel('Month')
    ax2.set_ylabel('Pass Rate (%)')
    ax2.set_ylim(90, 100)  # Limiting y-axis for better visibility of changes
    
    # Show the plot
    if st.button('Create Quality Control and Inspection Analysis Chart'):
        st.pyplot(fig)
