# modules/supplier_performance.py

import matplotlib.pyplot as plt
import pandas as pd
import streamlit as st

def generate_supplier_performance(df):
    st.write("Please select the columns for the supplier performance analysis.")
    
    supplier_column = st.selectbox("Select the column for suppliers", df.columns)
    metrics_columns = st.multiselect("Select the performance metrics columns", df.columns)
    
    if not supplier_column or not metrics_columns:
        st.error("Please select the supplier column and at least one performance metrics column.")
        return
    
    if len(metrics_columns) < 4:
        st.error("Please select at least four performance metrics columns.")
        return
    
    # Plotting
    fig, axs = plt.subplots(2, 2, figsize=(14, 10))  # Create a grid of subplots
    fig.suptitle('Supplier Performance Analysis', fontsize=16)

    # Plot for the first metric
    axs[0, 0].bar(df[supplier_column], df[metrics_columns[0]], color='skyblue')
    axs[0, 0].set_title(metrics_columns[0])
    axs[0, 0].set_xlabel('Supplier')
    axs[0, 0].set_ylabel('Value')

    # Plot for the second metric
    axs[0, 1].bar(df[supplier_column], df[metrics_columns[1]], color='lightgreen')
    axs[0, 1].set_title(metrics_columns[1])
    axs[0, 1].set_xlabel('Supplier')
    axs[0, 1].set_ylabel('Value')

    # Plot for the third metric
    axs[1, 0].bar(df[supplier_column], df[metrics_columns[2]], color='lightcoral')
    axs[1, 0].set_title(metrics_columns[2])
    axs[1, 0].set_xlabel('Supplier')
    axs[1, 0].set_ylabel('Value')

    # Plot for the fourth metric
    axs[1, 1].bar(df[supplier_column], df[metrics_columns[3]], color='gold')
    axs[1, 1].set_title(metrics_columns[3])
    axs[1, 1].set_xlabel('Supplier')
    axs[1, 1].set_ylabel('Value')

    # Automatically adjust layout to prevent overlap
    plt.tight_layout(rect=[0, 0.03, 1, 0.95])

    # Display the plot
    st.pyplot(fig)
