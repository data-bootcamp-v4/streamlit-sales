# app.py

# Add necessary imports at the beginning of your script
import streamlit as st
from backend import load_data, get_summary, plot_sales_over_time

def main():
    st.title('Supermarket Sales Dashboard - Real-time Hypothesis Testing')

    # Load data and display initial state
    data = load_data()
    summary = get_summary(data)
    st.write("### Summary Statistics")
    st.table(summary)
    
    # Interactive widgets for hypothesis testing
    st.sidebar.header('Hypothesis Testing Controls')
    discount_rate = st.sidebar.slider('Discount Rate', min_value=0.0, max_value=1.0, value=0.1, step=0.01)
    min_rating = st.sidebar.slider('Minimum Rating', min_value=0, max_value=10, value=5, step=1)

    # Apply the discount and filter by rating
    data['Discounted_Total'] = data['Total'] * (1 - discount_rate)
    filtered_data = data[data['Rating'] >= min_rating]

    # Update summary statistics and plots
    updated_summary = get_summary(filtered_data)
    st.write("### Updated Summary Statistics")
    st.table(updated_summary)
    
    st.write("### Sales Over Time")
    plot_sales_over_time(filtered_data)

if __name__ == '__main__':
    main()
