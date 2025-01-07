import matplotlib.pyplot as plt
import pandas as pd
import streamlit as st

def generate_lead_time_analysis(df):
    order_id_column_key = 'order_id_column_select'
    lead_time_column_key = 'lead_time_column_select'

    order_id_column = st.selectbox('Select Order ID column', df.columns, key=order_id_column_key)
    lead_time_column = st.selectbox('Select Lead Time column', df.columns, key=lead_time_column_key)

    # Convert the data to numeric format
    df[lead_time_column] = pd.to_numeric(df[lead_time_column], errors='coerce')

    # Calculate average lead time
    average_lead_time = df[lead_time_column].mean()

    # Plotting
    fig, ax = plt.subplots(figsize=(10, 6))

    # Bar plot for Lead Times
    ax.bar(df[order_id_column], df[lead_time_column], color='skyblue')

    # Line for Average Lead Time
    ax.axhline(y=average_lead_time, color='red', linestyle='--', linewidth=2, label=f'Average Lead Time: {average_lead_time:.2f} days')

    # Adding text for labels, title, and custom x-axis tick labels
    ax.set_xlabel('Order ID')
    ax.set_ylabel('Lead Time (days)')
    ax.set_title('Lead Time Analysis')
    ax.set_xticklabels(df[order_id_column], rotation=45)
    ax.legend()

    # Display the plot in Streamlit
    if st.button('Create Lead Time Analysis'):
        st.pyplot(fig)
