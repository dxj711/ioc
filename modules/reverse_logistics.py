import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

def generate_reverse_logistics(df):
    category_column_key = 'category_column_select'
    value_column1_key = 'value_column1_select'
    value_column2_key = 'value_column2_select'

    category_column = st.selectbox('Select category column', df.columns, key=category_column_key)
    value_column1 = st.selectbox('Select value column 1', df.columns, key=value_column1_key)
    value_column2 = st.selectbox('Select value column 2', df.columns, key=value_column2_key)

    # Sample data for reverse logistics metrics
    categories = df[category_column]
    values1 = df[value_column1]
    values2 = df[value_column2]

    # Check if the selected columns are numeric
    if not pd.api.types.is_numeric_dtype(values1):
        st.error(f'The selected column {value_column1} contains non-numeric data. Please select a numeric column.')
        return

    if not pd.api.types.is_numeric_dtype(values2):
        st.error(f'The selected column {value_column2} contains non-numeric data. Please select a numeric column.')
        return

    # Create a figure and a set of subplots
    fig, axs = plt.subplots(3, 1, figsize=(10, 15), sharex=True)

    # Plotting Value Column 1
    axs[0].bar(categories, values1, color='skyblue')
    axs[0].set_title(f'Monthly {value_column1}')
    axs[0].set_ylabel('Units')

    # Plotting Value Column 2
    axs[1].bar(categories, values2, color='salmon')
    axs[1].set_title(f'Monthly {value_column2}')
    axs[1].set_ylabel('Cost ($1000s)')

    # Example: Plotting a Calculated Metric
    calculated_metric = values1 / values2  # Example calculation
    axs[2].bar(categories, calculated_metric, color='lightgreen')
    axs[2].set_title('Calculated Metric')
    axs[2].set_ylabel('Value')

    # Add labels and title to the plot
    for ax in axs:
        ax.set_xlabel(category_column)
        ax.set_xticks(categories)  # Set the ticks
        ax.set_xticklabels(categories, rotation=45)  # Set the labels with rotation
        ax.grid(True)

    plt.tight_layout()
    st.pyplot(fig)

def main():
    st.title('Reverse Logistics Dashboard')
    uploaded_file = st.file_uploader("Upload CSV", type=["csv"])
    if uploaded_file:
        df = pd.read_csv(uploaded_file)
        generate_reverse_logistics(df)

if __name__ == "__main__":
    main()
