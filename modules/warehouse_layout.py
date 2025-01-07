import streamlit as st
import matplotlib.pyplot as plt
import matplotlib.patches as patches

def generate_warehouse_layout():
    # Streamlit app title
    st.title('Warehouse Layout Optimization')

    # Number of sections input
    num_sections = st.number_input('Enter the number of sections', min_value=1, max_value=10, value=4)

    # Initialize lists for storing section details
    section_names = []
    section_width = []
    section_height = []
    section_colors = []

    # Input fields for each section
    for i in range(num_sections):
        st.subheader(f'Section {i + 1}')
        section_names.append(st.text_input(f'Enter name for section {i + 1}', f'Section {i + 1}'))
        section_width.append(st.slider(f'Width for section {i + 1}', 0.1, 1.0, 0.2))
        section_height.append(st.slider(f'Height for section {i + 1}', 0.1, 1.0, 0.4))
        section_colors.append(st.color_picker(f'Pick a color for section {i + 1}', '#0000FF'))

    # Calculate total area of sections
    total_area = sum([w * h for w, h in zip(section_width, section_height)])

    # Check if total area exceeds available space
    if total_area > 1.0:
        st.error("The total area of sections exceeds the available space. Please adjust the section dimensions.")

        # Exit the function to prevent further execution
        return

    # Create a figure and a grid of subplots
    fig, ax = plt.subplots(figsize=(10, 7))

    # Initialize variables for positioning sections
    x_pos = 0
    y_pos = 0
    max_height = 0  # Track the maximum height in the current row
    gap = 0.05  # Gap between sections

    # Add rectangles for each section
    for i, (name, width, height, color) in enumerate(zip(section_names, section_width, section_height, section_colors)):
        # Check if adding the current section with gap exceeds the width of the plot
        if x_pos + width + gap > 1:
            x_pos = 0  # Reset x position to start a new row
            y_pos += max_height + gap  # Move to the next row
            max_height = 0  # Reset the maximum height for the new row
        
        # Add the rectangle for the current section with gap
        rect = patches.Rectangle((x_pos, y_pos), width, height, linewidth=2, edgecolor='black', facecolor=color)
        ax.add_patch(rect)
        # Update the maximum height in the current row
        if height > max_height:
            max_height = height
        
        # Increment x position for the next section with gap
        x_pos += width + gap

        # Add text label in the center of each section
        ax.text(x_pos - (width + gap) / 2, y_pos + height / 2, name,
                horizontalalignment='center', verticalalignment='center', fontsize=12, color='black', weight='bold')

    # Set limits and labels
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_aspect('equal')  # Set the aspect of the plot to be equal
    #ax.set_title('Warehouse Layout Optimization')

    # Show the plot in Streamlit
    st.pyplot(fig)


