
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from dotenv import load_dotenv



from modules.plot_types import PLOT_TYPES
from modules.abc_analysis import perform_abc_analysis, plot_abc_analysis
from modules.pareto_chart import generate_pareto_chart
from modules.capacity_analysis import perform_capacity_analysis
from modules.contract_analysis import generate_contract_analysis
from modules.demand_forecast import generate_demand_forecasting_chart
from modules.risk_analysis import generate_risk_analysis
from modules.cost_to_serve import generate_cost_serve_analysis
from modules.warehouse_layout import generate_warehouse_layout
from modules.lead_time_analysis import generate_lead_time_analysis
from modules.order_fulfillment_analysis import generate_order_analysis
from modules.product_lifecycle_analysis import generate_product_lifecycle
from modules.quality_control_analysis import generate_quality_analysis
from modules.service_level_analysis import generate_service_level_analysis
from modules.sku_rationalization import generate_sku_rationalization
from modules.supplier_consolidation import generate_supplier_consolidation
from modules.inventory_optimization import generate_inventory_optimization
from modules.sop_analysis import generate_sop_analysis
from modules.customer_segmentation import generate_customer_segmentation
from modules.reverse_logistics import generate_reverse_logistics
from modules.supplier_performance import generate_supplier_performance
from modules.supply_chain_segmentation import generate_supply_chain_segmentation
from modules.supply_network import generate_supply_network
from modules.production_planning import generate_production_planning

from Regression.regression_types import regression_types
from Regression.linearRegression import generate_linear_regression
from Regression.logisticRegression import generate_logistic_regression
from Regression.randomForest import generate_random_forest
from Regression.gradientRegression import generate_gradient_regression
load_dotenv()
api_key = "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"
#os.getenv('OPENAI_API_KEY')
#st.set_page_config(layout="wide")

def main():
    st.header("Visualization")
    

    csv_file = st.file_uploader("Upload your CSV", type='csv')
    if csv_file is not None:
        df = pd.read_csv(csv_file)
        st.write("Data preview:")
        st.dataframe(df)
        

      
        
        st.header("Generate Plots")
        plot_option = st.selectbox("Select a plot type", PLOT_TYPES)
        
        if plot_option == "Histogram":
            selected_column = st.selectbox("Select a column for the histogram", df.columns)
            fig, ax = plt.subplots()
            sns.histplot(df[selected_column], bins=20, kde=True, ax=ax)
            st.pyplot(fig)

        elif plot_option == "Line Plot":
            x_column = st.selectbox("Select the x-axis column", df.columns)
            y_column = st.selectbox("Select the y-axis column", df.columns)
            fig, ax = plt.subplots()
            sns.lineplot(x=df[x_column], y=df[y_column], ax=ax)
            st.pyplot(fig)

        elif plot_option == "Scatter Plot":
            x_column = st.selectbox("Select the x-axis column", df.columns)
            y_column = st.selectbox("Select the y-axis column", df.columns)
            fig, ax = plt.subplots()
            sns.scatterplot(x=df[x_column], y=df[y_column], ax=ax)
            st.pyplot(fig)

        elif plot_option == "ABC Analysis":
            df_abc = perform_abc_analysis(df)
            plot_abc_analysis(df_abc)

        elif plot_option == "Pareto Chart":
            generate_pareto_chart(df)
            
        elif plot_option == "Capacity Planning Analysis":
            perform_capacity_analysis(df)

        elif plot_option == "Contract Management Analysis":
            generate_contract_analysis(df)
        
        elif plot_option == "Demand Forecasting Analysis":
            generate_demand_forecasting_chart(df)
        
        elif plot_option == "Risk Assessment and Mitigation":
            generate_risk_analysis(df)

        elif plot_option == "Cost to Serve Analysis":
            generate_cost_serve_analysis(df)

        elif plot_option == "Warehouse Layout":
            generate_warehouse_layout()

        elif plot_option == "Lead Time Analysis":
            generate_lead_time_analysis(df)

        elif plot_option == "Order Fulfillment Analysis":
            generate_order_analysis(df)
        
        elif plot_option == "Product Lifecyle Analysis":
            generate_product_lifecycle(df)

        elif plot_option == "Quality Control and Inspection Analysis":
            generate_contract_analysis(df)

        elif plot_option == "Service Level Analysis":
            generate_service_level_analysis(df)

        elif plot_option == "SKU Rationalization":
            generate_sku_rationalization(df)

        elif plot_option == "Supplier Consolidation Analysis":
            generate_supplier_consolidation(df)
        

        elif plot_option == "Risk Analysis":
            generate_risk_analysis(df)

        elif plot_option == "SOP Analysis":
            generate_sop_analysis(df)

        elif plot_option == "Customer Segmentation Analysis":
            generate_customer_segmentation(df)

        elif plot_option == "Reverse Logistics Analysis":
            generate_reverse_logistics(df)

        elif plot_option == "Supplier Performance Analysis":
            generate_supplier_performance(df)

        elif plot_option == "Supply Chain Segmentation Analysis":
            generate_supply_chain_segmentation(df)

        elif plot_option == "Supply Chain network Optimization":
            generate_supply_network(df)

        elif plot_option == "Iventory Optimization":
            generate_inventory_optimization(df)
        
        elif plot_option == "Production Planning and Scheduling Analysis":
            generate_production_planning(df)


        st.header("Generate Predictions")
        plot_option1 = st.selectbox("Select a prediciton type", regression_types)
        
        if plot_option1 == "Linear Regression":
            generate_linear_regression(df)

        elif plot_option1 == "Logistic Regression":
            generate_logistic_regression(df)

        elif plot_option1 == "Random Forest":
            generate_random_forest(df)
        
        elif plot_option1 == "Gradient Boost Regression":
            generate_gradient_regression(df)

if __name__ == '__main__':
    main()
