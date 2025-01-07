import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

def perform_capacity_analysis(df):
    # Allow the user to select the columns for the analysis
    time_period_column_key = 'time_period_column_select'
    current_capacity_column_key = 'current_capacity_column_select'
    projected_demand_column_key = 'projected_demand_column_select'
    planned_capacity_column_key = 'planned_capacity_column_select'

    time_period_column = st.selectbox('Select time period column', df.columns, key=time_period_column_key)
    current_capacity_column = st.selectbox('Select current capacity column', df.columns, key=current_capacity_column_key)
    projected_demand_column = st.selectbox('Select projected demand column', df.columns, key=projected_demand_column_key)
    planned_capacity_column = st.selectbox('Select planned capacity column', df.columns, key=planned_capacity_column_key)

    # Convert the capacity and demand data to numeric format
    df[current_capacity_column] = pd.to_numeric(df[current_capacity_column], errors='coerce')
    df[projected_demand_column] = pd.to_numeric(df[projected_demand_column], errors='coerce')
    df[planned_capacity_column] = pd.to_numeric(df[planned_capacity_column], errors='coerce')

    # Group by the selected time period and sum the capacities and demands
    current_capacity_data = df.groupby(time_period_column)[current_capacity_column].sum().sort_index()
    projected_demand_data = df.groupby(time_period_column)[projected_demand_column].sum().sort_index()
    planned_capacity_data = df.groupby(time_period_column)[planned_capacity_column].sum().sort_index()

    # Check if capacity and demand data length is zero to avoid errors
    if len(current_capacity_data) == 0 or len(projected_demand_data) == 0 or len(planned_capacity_data) == 0:
        #st.error("No data available for Capacity Analysis.")
        return

    # Plotting the Capacity and Demand Analysis
    fig, ax = plt.subplots()
    ax.plot(current_capacity_data.index, current_capacity_data.values, marker='o', linestyle='-', color='b', label='Current Capacity')
    ax.plot(projected_demand_data.index, projected_demand_data.values, marker='x', linestyle='--', color='r', label='Projected Demand')
    ax.plot(planned_capacity_data.index, planned_capacity_data.values, marker='s', linestyle='-', color='g', label='Planned Capacity')

    # Set axis labels and title
    ax.set_xlabel(time_period_column)
    ax.set_ylabel('Values')
    plt.title('Capacity and Demand Analysis Over Time')

    # Show legend
    ax.legend()

    # Show plot
    if st.button('Create Capacity and Demand Analysis Plot'):
        st.pyplot(fig)
