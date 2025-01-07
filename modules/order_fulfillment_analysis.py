import matplotlib.pyplot as plt
import pandas as pd
import streamlit as st

def generate_order_analysis(df):
    order_id_column_key = 'order_id_column_fulfillment_select'
    fulfillment_time_column_key = 'fulfillment_time_column_select'

    order_id_column = st.selectbox('Select Order ID column', df.columns, key=order_id_column_key)
    fulfillment_time_column = st.selectbox('Select Fulfillment Time column', df.columns, key=fulfillment_time_column_key)

    # Convert the data to numeric format
    df[fulfillment_time_column] = pd.to_numeric(df[fulfillment_time_column], errors='coerce')

    # Set a benchmark for expected fulfillment time
    benchmark_fulfillment_time = st.number_input('Set benchmark fulfillment time (days)', value=3)

    # Convert the value to string
    benchmark_fulfillment_time_str = str(benchmark_fulfillment_time)

    # Plotting
    fig, ax = plt.subplots(figsize=(10, 6))

    # Bar plot for Fulfillment Times
    bars = ax.bar(df[order_id_column], df[fulfillment_time_column], color='lightblue')

    # Highlight bars that exceed the benchmark time
    for bar in bars:
        if bar.get_height() > benchmark_fulfillment_time:
            bar.set_color('salmon')

    # Line for Benchmark Fulfillment Time
    ax.axhline(y=benchmark_fulfillment_time, color='green', linestyle='--', linewidth=2, label=f'Benchmark Time: {benchmark_fulfillment_time_str} days')

    # Adding text for labels, title, and custom x-axis tick labels
    ax.set_xlabel('Order ID')
    ax.set_ylabel('Fulfillment Time (days)')
    ax.set_title('Order Fulfillment Analysis')
    ax.set_xticklabels(df[order_id_column], rotation=45)
    ax.legend()

    # Display the plot in Streamlit
    if st.button('Create Order Fulfillment Analysis'):
        st.pyplot(fig)
