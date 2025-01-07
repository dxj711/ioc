import matplotlib.pyplot as plt
import pandas as pd
import streamlit as st


def generate_demand_forecasting_chart(df):
    # User selects columns for month, historical sales, and forecasted sales
    month_column = st.selectbox('Select month column', df.columns)
    historical_sales_column = st.selectbox('Select historical sales column', df.columns)
    forecasted_sales_column = st.selectbox('Select forecasted sales column', df.columns)

    # Convert the necessary columns to appropriate types if not already
    df[historical_sales_column] = pd.to_numeric(df[historical_sales_column], errors='coerce')
    df[forecasted_sales_column] = pd.to_numeric(df[forecasted_sales_column], errors='coerce')

    # Plotting
    fig, ax = plt.subplots(figsize=(10, 6))

    # Line plot for Historical Sales
    ax.plot(df[month_column], df[historical_sales_column], label='Historical Sales', marker='o', color='blue')

    # Line plot for Forecasted Sales
    ax.plot(df[month_column], df[forecasted_sales_column], label='Forecasted Sales', marker='o', linestyle='--', color='green')

    # Adding text for labels, title, and custom x-axis tick labels
    ax.set_xlabel('Month')
    ax.set_ylabel('Sales Units')
    ax.set_title('Demand Forecasting Analysis')
    ax.set_xticks(df[month_column])
    ax.set_xticklabels(df[month_column], rotation=45)
    ax.legend()

    # Show the plot
    if st.button('Create Demand Forecasting Chart'):
        st.pyplot(fig)
