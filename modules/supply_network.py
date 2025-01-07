
# supply_chain_analysis.py
import matplotlib.pyplot as plt
import networkx as nx
import streamlit as st

def generate_supply_network(df):
    st.write("Supply Chain Network Analysis")

    # Select columns for different nodes
    supplier_column = st.selectbox('Select Supplier Column', df.columns)
    factory_column = st.selectbox('Select Factory Column', df.columns)
    warehouse_column = st.selectbox('Select Warehouse Column', df.columns)
    retailer_column = st.selectbox('Select Retailer Column', df.columns)

    # Create a directed graph
    G = nx.DiGraph()

    # Add nodes with the node type as a node attribute
    nodes = {
        "Supplier": df[supplier_column].unique(),
        "Factory": df[factory_column].unique(),
        "Warehouse": df[warehouse_column].unique(),
        "Retailer": df[retailer_column].unique()
    }
    for node_type, node_list in nodes.items():
        G.add_nodes_from(node_list, type=node_type)

    # Add edges based on the data in the DataFrame
    for _, row in df.iterrows():
        G.add_edge(row[supplier_column], row[factory_column])
        G.add_edge(row[factory_column], row[warehouse_column])
        G.add_edge(row[warehouse_column], row[retailer_column])

    # Define positions for visualization
    pos = nx.spring_layout(G)

    # Draw the network
    plt.figure(figsize=(12, 8))
    nx.draw(G, pos, with_labels=True, node_color='skyblue', edge_color='k', node_size=2500, font_size=10, font_color='darkred', arrowstyle='-|>', arrowsize=10)
    plt.title('Supply Chain Network')
    
    st.pyplot(plt)