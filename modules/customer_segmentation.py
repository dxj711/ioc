# customer_segmentation.py
import matplotlib.pyplot as plt
import streamlit as st
import pandas as pd
import numpy as np

def generate_customer_segmentation(df):
    spending_column_key = 'spending_column_select'
    frequency_column_key = 'frequency_column_select'
    segment_column_key = 'segment_column_select'
    
    spending_column = st.selectbox('Select Annual Spending column', df.columns, key=spending_column_key)
    frequency_column = st.selectbox('Select Visit Frequency column', df.columns, key=frequency_column_key)
    segment_column = st.selectbox('Select Customer Segment column', df.columns, key=segment_column_key)
    
    if spending_column and frequency_column and segment_column:
        fig, ax = plt.subplots()
        
        segments = df[segment_column].unique()
        colors = plt.cm.rainbow(np.linspace(0, 1, len(segments)))
        
        for segment, color in zip(segments, colors):
            segment_data = df[df[segment_column] == segment]
            ax.scatter(segment_data[spending_column], segment_data[frequency_column], color=color, alpha=0.5, label=segment)
        
        # Labeling the axes and the plot
        ax.set_xlabel('Annual Spending (thousands)')
        ax.set_ylabel('Visit Frequency (visits per year)')
        ax.set_title('Customer Segmentation Analysis')
        ax.legend()
        
        # Show the plot
        if st.button('Create Customer Segmentation Chart'):
            st.pyplot(fig)
