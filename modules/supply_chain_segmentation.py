import matplotlib.pyplot as plt
import streamlit as st
import pandas as pd

def generate_supply_chain_segmentation(df):
    st.write("Please select the columns for the segmentation analysis.")
    
    segments_column = st.selectbox("Select the column for segments", df.columns)
    value_columns = st.multiselect("Select the value columns", df.columns)
    
    if not segments_column or not value_columns:
        st.error("Please select both the segment column and at least one value column.")
        return
    
    max_segments = st.slider("Select the maximum number of segments to display", min_value=5, max_value=20, value=10)
    
    try:
        # Group by segments and calculate the sum of the selected value columns
        grouped_data = df.groupby(segments_column)[value_columns].sum().reset_index()

        for value_column in value_columns:
            segments = grouped_data[segments_column]
            sales_percentage = grouped_data[value_column] / grouped_data[value_column].sum() * 100

            # Sort the data by sales percentage
            sorted_data = grouped_data.assign(sales_percentage=sales_percentage).sort_values(by='sales_percentage', ascending=False)

            # Aggregate smaller segments into 'Other' category if necessary
            if len(sorted_data) > max_segments:
                top_data = sorted_data[:max_segments - 1]
                other_data = sorted_data[max_segments - 1:]
                other_total = other_data[value_column].sum()
                other_row = pd.DataFrame({segments_column: ['Other'], value_column: [other_total]})
                top_data = pd.concat([top_data, other_row])

                segments = top_data[segments_column]
                sales_percentage = top_data[value_column] / top_data[value_column].sum() * 100

            # Creating the pie chart
            fig, ax = plt.subplots()
            ax.pie(sales_percentage, labels=segments, autopct='%1.1f%%', startangle=90, colors=plt.cm.tab20.colors)
            ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

            # Adding a title
            ax.set_title(f'Supply Chain Segmentation Analysis ({value_column})')

            # Display the plot
            st.pyplot(fig)

    except KeyError as e:
        st.error(f"Error: {e}. Please check if the column contains the appropriate datatype.")

    except Exception as e:
        st.error(f"An error occurred: {e}")

