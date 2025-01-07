import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

def perform_abc_analysis(df):
    category_column = st.selectbox('Select category column', df.columns)
    value_column = st.selectbox('Select value column', df.columns)

    if category_column not in df.columns or value_column not in df.columns:
        st.error("Selected columns not found in the DataFrame.")
        return

    df[value_column] = pd.to_numeric(df[value_column], errors='coerce')
    df = df.dropna(subset=[value_column])

    df = df.sort_values(by=value_column, ascending=False)
    df['Cumulative'] = df[value_column].cumsum()
    df['Percentage'] = (df['Cumulative'] / df[value_column].sum()) * 100

    def categorize(row, breaks=[80, 95]):
        if row['Percentage'] <= breaks[0]:
            return 'A'
        elif row['Percentage'] <= breaks[1]:
            return 'B'
        else:
            return 'C'

    df['Category'] = df.apply(categorize, axis=1)

    return df

def plot_abc_analysis(df):
    if df.empty:
        #st.error("No data available for plotting.")
        return

    fig, ax = plt.subplots(figsize=(10, 6))
    colors = {'A': 'red', 'B': 'blue', 'C': 'green'}
    grouped = df.groupby('Category')['Value'].sum()
    categories = ['A', 'B', 'C']  # Ensure all categories are accounted for
    grouped = grouped.reindex(categories, fill_value=0)  # Fill missing categories with 0
    if not grouped.empty:
        grouped.plot(kind='bar', color=grouped.index.map(colors), alpha=0.7)
        for i, value in enumerate(grouped):
            ax.text(i, value, f'{value:.0f}', ha='center', va='bottom')
    ax.set_title('ABC Analysis of Items')
    ax.set_xlabel('Category')
    ax.set_ylabel('Total Value')
    ax.set_xticklabels(['Class A', 'Class B', 'Class C'])
    ax.grid(True)
    st.pyplot(fig)


def abc_analysis_app(df):
    abc_df = perform_abc_analysis(df)
    if abc_df is not None:
        st.write(abc_df.head())

        if st.button('Plot ABC Analysis'):
            plot_abc_analysis(abc_df)

# Example usage
if __name__ == "__main__":
    df = pd.read_csv("your_data.csv")  # Load your CSV data
    abc_analysis_app(df)
