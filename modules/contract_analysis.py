# contract_management_analysis.py
import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

def generate_contract_analysis(df):
    client_column_key = 'client_column_select'
    contract_value_column_key = 'contract_value_column_select'
    contract_duration_column_key = 'contract_duration_column_select'
    performance_column_key = 'performance_column_select'

    client_column = st.selectbox('Select client column', df.columns, key=client_column_key)
    contract_value_column = st.selectbox('Select contract value column', df.columns, key=contract_value_column_key)
    contract_duration_column = st.selectbox('Select contract duration column', df.columns, key=contract_duration_column_key)
    performance_column = st.selectbox('Select performance column', df.columns, key=performance_column_key)

    clients = df[client_column].astype(str)
    contract_values = pd.to_numeric(df[contract_value_column], errors='coerce')
    contract_durations = pd.to_numeric(df[contract_duration_column], errors='coerce')
    performance = pd.to_numeric(df[performance_column], errors='coerce')

    fig, ax1 = plt.subplots()

    # Bar chart for contract values
    ax1.bar(clients, contract_values, color='blue', alpha=0.6, label='Contract Value ($000)')
    ax1.set_xlabel('Client')
    ax1.set_ylabel('Contract Value ($000)', color='blue')
    ax1.tick_params(axis='y', labelcolor='blue')
    ax1.set_title('Contract Management Analysis')

    # Rotate x-axis labels
    plt.xticks(rotation=90)

    # Create a second y-axis for contract duration
    ax2 = ax1.twinx()
    ax2.bar(clients, contract_durations, color='green', alpha=0.6, width=0.4, label='Contract Duration (months)')
    ax2.set_ylabel('Contract Duration (months)', color='green')
    ax2.tick_params(axis='y', labelcolor='green')

    # Create a third y-axis for performance
    ax3 = ax1.twinx()
    ax3.spines['right'].set_position(('outward', 60))
    ax3.plot(clients, performance, color='red', marker='o', label='Performance (%)')
    ax3.set_ylabel('Performance (%)', color='red')
    ax3.tick_params(axis='y', labelcolor='red')

    # Adding legend
    fig.legend(loc='upper left', bbox_to_anchor=(0.1, 0.9))

    # Show the plot
    if st.button('Create Contract Management Analysis Chart'):
        st.pyplot(fig)
