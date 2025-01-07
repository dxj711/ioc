import matplotlib.pyplot as plt
import pandas as pd
import streamlit as st

def generate_service_level_analysis(df):
    response_time_column_key = 'response_time_column_select'
    resolution_time_column_key = 'resolution_time_column_select'
    month_column_key = 'month_column_select'

    month_column = st.selectbox('Select Month column', df.columns, key=month_column_key)
    response_time_column = st.selectbox('Select Response Time column', df.columns, key=response_time_column_key)
    resolution_time_column = st.selectbox('Select Resolution Time column', df.columns, key=resolution_time_column_key)

    # Convert the data to numeric format
    df[response_time_column] = pd.to_numeric(df[response_time_column], errors='coerce')
    df[resolution_time_column] = pd.to_numeric(df[resolution_time_column], errors='coerce')

    fig, ax1 = plt.subplots(figsize=(10, 6))

    # Plotting Average Response Time
    color = 'tab:red'
    ax1.set_xlabel(month_column)
    ax1.set_ylabel('Average Response Time (hours)', color=color)
    ax1.plot(df[month_column], df[response_time_column], color=color, marker='o', label='Avg Response Time')
    ax1.tick_params(axis='y', labelcolor=color)

    # Create a second y-axis for the resolution time
    ax2 = ax1.twinx()
    color = 'tab:blue'
    ax2.set_ylabel('Average Resolution Time (hours)', color=color)
    ax2.plot(df[month_column], df[resolution_time_column], color=color, marker='o', label='Avg Resolution Time')
    ax2.tick_params(axis='y', labelcolor=color)

    # Adding a title and grid
    ax1.set_title('Service Level Analysis: Response and Resolution Times')
    ax1.grid(True)

    # Adding legend
    fig.legend(loc='upper right', bbox_to_anchor=(1,1), bbox_transform=ax1.transAxes)

    # Display the plot in Streamlit
    if st.button('Create Service Level Analysis'):
        st.pyplot(fig)
