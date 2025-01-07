# modules/transportation_mode_analysis.py

import matplotlib.pyplot as plt
import numpy as np
import streamlit as st
import pandas as pd  # Ensure pandas is imported

def generate_transportation_mode_analysis(modes, cost, speed, environmental_impact):
    # Create a DataFrame from the inputs
    data = pd.DataFrame({
        'Mode': modes,
        'Cost': cost,
        'Speed': speed,
        'Environmental Impact': environmental_impact
    })

    # Group by mode and calculate the mean of the metrics
    grouped_data = data.groupby('Mode').mean().reset_index()

    modes = grouped_data['Mode']
    cost = grouped_data['Cost']
    speed = grouped_data['Speed']
    environmental_impact = grouped_data['Environmental Impact']

    x = np.arange(len(modes))  # the label locations

    # Plotting
    fig, ax1 = plt.subplots(figsize=(10, 6))

    # Bar chart for costs
    ax1.set_xlabel('Mode of Transportation')
    ax1.set_ylabel('Cost', color='tab:red')
    ax1.bar(x - 0.2, cost, width=0.2, color='tab:red', align='center', label='Cost')
    ax1.tick_params(axis='y', labelcolor='tab:red')

    # Create a second y-axis for speed
    ax2 = ax1.twinx()
    ax2.set_ylabel('Speed', color='tab:blue')
    ax2.bar(x, speed, width=0.2, color='tab:blue', align='center', label='Speed')
    ax2.tick_params(axis='y', labelcolor='tab:blue')

    # Create a third y-axis for environmental impact
    ax3 = ax1.twinx()
    ax3.spines['right'].set_position(('outward', 60))  # Offset the right spine
    ax3.set_ylabel('Environmental Impact', color='tab:green')
    ax3.bar(x + 0.2, environmental_impact, width=0.2, color='tab:green', align='center', label='Environmental Impact')
    ax3.tick_params(axis='y', labelcolor='tab:green')

    # Title and custom x-axis tick labels
    ax1.set_title('Transportation Mode Analysis')
    ax1.set_xticks(x)
    ax1.set_xticklabels(modes)

    fig.tight_layout()  # Adjust layout to fit
    fig.legend(loc='upper left', bbox_to_anchor=(0.1, 0.9))  # Place the legend

    # Display the plot
    st.pyplot(fig)
