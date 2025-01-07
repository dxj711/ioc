import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

def generate_production_planning(df):
    #st.title('Production Planning and Scheduling Analysis')
    
    # Dropdown menus to select columns for Task, Start, and Finish
    task_column = st.selectbox('Select the Task column', df.columns)
    start_column = st.selectbox('Select the Start date column', df.columns)
    finish_column = st.selectbox('Select the Finish date column', df.columns)
    
    if task_column and start_column and finish_column:
        # Convert selected columns to appropriate data types
        df['Start'] = pd.to_datetime(df[start_column], errors='coerce')
        df['Finish'] = pd.to_datetime(df[finish_column], errors='coerce')
        
        # Drop rows with NaT values in 'Start' or 'Finish' columns
        df.dropna(subset=['Start', 'Finish'], inplace=True)
        
        # Check if the DataFrame is empty after dropping rows with NaT values
        if df.empty:
            #st.warning("No valid data available. Please ensure the selected columns contain valid dates.")
            return
        
        df['Duration'] = df['Finish'] - df['Start']
        df['Task'] = df[task_column]
    
        # Select 15 equally spaced dates for display
        date_range = pd.date_range(df['Start'].min(), df['Finish'].max(), periods=15)
    
        # Creating the plot
        fig, ax = plt.subplots(figsize=(10, 5))
    
        # Generate bars for each task
        for i, task in df.iterrows():
            ax.barh(task['Task'], task['Duration'].days, left=task['Start'], color='skyblue')
    
        # Set the selected dates as major ticks on the x-axis
        ax.set_xticks(date_range)
    
        # Set the format of the date labels
        ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
    
        # Adding labels and a title
        ax.set_xlabel('Date')
        ax.set_ylabel('Task')
        ax.set_title('Production Planning and Scheduling Analysis')
        plt.xticks(rotation=45, ha='right')  # Rotate x-axis labels for better readability
        plt.grid(True)
    
        # Use Streamlit to display the plot
        st.pyplot(fig)

# Example usage
# df = pd.read_csv('your_data.csv')
# generate_production_planning(df)
