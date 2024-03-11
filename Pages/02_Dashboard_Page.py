import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px

st.set_page_config(
    page_title='Dashboard',
    page_icon='',
    layout='wide'
)

# Dataset for Visualization
combined_data = pd.read_csv('./data/combined_data.csv')

# Function to display EDA dashboard
def eda_dashboard():
  
    st.title('EDA Dashboard')
    

    # EDA visualizations
    st.subheader('Histogram of Tenure')
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.histplot(combined_data['tenure'], bins=30, kde=True, ax=ax)
    plt.title('Distribution of Tenure')
    st.pyplot(fig)

    st.subheader('Histogram of Monthly Charges')
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.histplot(combined_data['MonthlyCharges'], kde=True, ax=ax)
    plt.title('Distribution of Monthly Charges')
    st.pyplot(fig)

    st.subheader('Scatter Plot: Tenure vs. Monthly Charges')
    fig = px.scatter(combined_data, x='tenure', y='MonthlyCharges', title='Tenure vs. Monthly Charges')
    st.plotly_chart(fig)

# Function to display Analytics dashboard
def analytics_dashboard():
    st.title('Analytics Dashboard')
    st.write('Here you can find key performance indicators (KPIs).')

    # KPIs
    st.subheader('Key Performance Indicators (KPIs)')
    st.write('Average Tenure:', str(combined_data['tenure'].mean()))
    st.write('Average Monthly Charges:', str(combined_data['MonthlyCharges'].mean()))

    # Convert string representations to boolean values for 'Churn' column
    combined_data['Churn'] = pd.to_numeric(combined_data['Churn'], errors='coerce').astype(bool)

    # Convert boolean values to integers for 'Churn' column
    combined_data['Churn'] = combined_data['Churn'].astype(int)

    # Compute Churn Rate
    churn_rate = combined_data['Churn'].mean()
    st.write('Churn Rate:', int(churn_rate))

    # Create a bar chart
    kpis = ['Average Tenure', 'Average Monthly Charges', 'Churn Rate']
    values = [combined_data['tenure'].mean(), combined_data['MonthlyCharges'].mean(), churn_rate]
    fig = px.bar(x=kpis, y=values, labels={'x': 'KPI', 'y': 'Value'}, title='Analytics KPIs')
    st.plotly_chart(fig)

# Main function
def main():
    # Create layout
    columns = st.columns([2, 1])

    # Display selection box for choosing dashboard
    with columns[1]:
        dashboard_choice = st.selectbox("Choose Dashboard", ("EDA Dashboard", "Analytics Dashboard"))

    # Display dashboards in column 0
    with columns[0]:
        if dashboard_choice == "EDA Dashboard":
            eda_dashboard()
        elif dashboard_choice == "Analytics Dashboard":
            analytics_dashboard()

if __name__ == '__main__':
    main()
