import matplotlib.pyplot as plt
import pandas as pd
import streamlit as st

def generate_inventory_optimization(df):
    st.write("Please select the columns for the inventory optimization analysis.")
    
    day_column = st.selectbox("Select the column for days", df.columns)
    inventory_column = st.selectbox("Select the column for inventory levels", df.columns)
    reorder_point = st.number_input("Set the reorder point", min_value=0)
    safety_stock = st.number_input("Set the safety stock level", min_value=0)
    
    # Ensure the necessary columns are available
    if not all(col in df.columns for col in [day_column, inventory_column]):
        st.error(f"DataFrame must contain the following columns: {day_column}, {inventory_column}")
        return

    # Sort the DataFrame by the day column
    df = df.sort_values(by=day_column)
    
    df['Reorder Point'] = reorder_point
    df['Safety Stock'] = safety_stock

    # Plotting
    fig, ax = plt.subplots(figsize=(10, 6))

    # Line plot for Inventory Level
    ax.plot(df[day_column], df[inventory_column], label='Inventory Level', marker='o', color='blue')

    # Horizontal line for Reorder Point
    ax.axhline(y=reorder_point, color='red', linestyle='--', linewidth=2, label='Reorder Point')

    # Horizontal line for Safety Stock
    ax.axhline(y=safety_stock, color='green', linestyle='--', linewidth=2, label='Safety Stock')
    days=df[day_column]
    # Adding text for labels, title, and custom x-axis tick labels
    ax.set_xlabel('Day of the Month')
    ax.set_ylabel('Inventory Units')
    ax.set_title('Inventory Optimization Analysis')
    ax.set_xticks(days)
    ax.legend()

    ax.set_xticklabels(days, rotation=90)

    # Display the plot
    st.pyplot(fig)
