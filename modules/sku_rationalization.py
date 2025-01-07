import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd

def generate_sku_rationalization(df):
    try:
        # Define the keys for Streamlit widgets
        sales_volume_column_key = 'sales_volume_column_select'
        profit_margin_column_key = 'profit_margin_column_select'
        sku_id_column_key = 'sku_id_column_select'

        # User selection for sales volume, profit margin, and SKU ID
        sales_volume_column = st.selectbox('Select Sales Volume column', df.columns, key=sales_volume_column_key)
        profit_margin_column = st.selectbox('Select Profit Margin column', df.columns, key=profit_margin_column_key)
        sku_id_column = st.selectbox('Select SKU ID column', df.columns, key=sku_id_column_key)

        # Convert necessary columns to numeric
        df[sales_volume_column] = pd.to_numeric(df[sales_volume_column], errors='coerce')
        df[profit_margin_column] = pd.to_numeric(df[profit_margin_column], errors='coerce')

        # Create a scatter plot
        fig, ax = plt.subplots(figsize=(10, 6))
        scatter = ax.scatter(df[sales_volume_column], df[profit_margin_column], c=df[profit_margin_column], cmap='viridis', s=100, alpha=0.6)

        # Color bar indicating Profit Margin
        cbar = plt.colorbar(scatter)
        cbar.set_label('Profit Margin (%)')

        # Adding annotations for SKU IDs
        for i in range(len(df)):
            ax.annotate(df[sku_id_column][i], (df[sales_volume_column][i], df[profit_margin_column][i]), textcoords="offset points", xytext=(0,10), ha='center')

        # Adding labels and title
        ax.set_xlabel('Sales Volume')
        ax.set_ylabel('Profit Margin (%)')
        ax.set_title('SKU Rationalization Analysis')
        ax.grid(True)

        # Show the plot
        if st.button('Create SKU Rationalization Chart'):
            st.pyplot(fig)
    except:
        pass  # Hide the error message


