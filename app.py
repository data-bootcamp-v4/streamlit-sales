# app.py
import streamlit as st
from backend import load_data, get_summary, plot_sales_over_time

def main():
    st.title('Supermarket Sales Dashboard')

    data = load_data()
    summary = get_summary(data)
    
    # Display summary stats
    st.write("### Summary Statistics")
    st.table(summary)
    
    # Display raw data
    st.write("### Raw Data")
    st.dataframe(data)

    # Plotting
    st.write("### Sales Over Time")
    plt = plot_sales_over_time(data)
    st.pyplot(plt)
    


if __name__ == '__main__':
    main()
