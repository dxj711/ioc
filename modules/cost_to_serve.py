# cost_serve_analysis.py
import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

def generate_cost_serve_analysis(df):
    segment_column_key = 'segment_column_select'
    cost_column_key = 'cost_column_select'
    revenue_column_key = 'revenue_column_select'

    segment_column = st.selectbox('Select segment column', df.columns, index=0, key=segment_column_key)
    cost_column = st.selectbox('Select cost column', df.columns, index=2, key=cost_column_key)
    revenue_column = st.selectbox('Select revenue column', df.columns, index=3, key=revenue_column_key)

    # Convert the data to numeric format
    df[cost_column] = pd.to_numeric(df[cost_column], errors='coerce')
    df[revenue_column] = pd.to_numeric(df[revenue_column], errors='coerce')

    # Group by the segment column and sum the cost and revenue
    data = df.groupby(segment_column).agg({cost_column: 'sum', revenue_column: 'sum'}).reset_index()
    
    # Check if data length is zero to avoid generating empty plot
    if len(data) == 0:
        st.error("No data available for Cost to Serve Analysis.")
        return

    # Plotting
    fig, ax = plt.subplots(figsize=(10, 6))

    # Bar plot for Costs
    cost_bars = ax.bar(data[segment_column], data[cost_column], width=0.4, label='Cost', color='red', alpha=0.7)

    # Bar plot for Revenues
    revenue_bars = ax.bar(data[segment_column], data[revenue_column], width=0.4, label='Revenue', color='green', alpha=0.7, bottom=data[cost_column])

    # Adding text for labels, title and custom x-axis tick labels, etc.
    ax.set_xlabel('Customer Segment')
    ax.set_ylabel('Amount ($)')
    ax.set_title('Cost to Serve Analysis')
    ax.legend()

    # Label with the values on the bars
    def add_labels(bars):
        for bar in bars:
            height = bar.get_height()
            ax.annotate('{}'.format(height),
                        xy=(bar.get_x() + bar.get_width() / 2, height),
                        xytext=(0, 3),  # 3 points vertical offset
                        textcoords="offset points",
                        ha='center', va='bottom')

    add_labels(cost_bars)
    add_labels(revenue_bars)

    # Show the plot
    if st.button('Create Cost to Serve Analysis Chart'):
        st.pyplot(fig)
