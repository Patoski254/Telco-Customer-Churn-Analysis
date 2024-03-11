Telco Customer Churn Analysis

Overview

This project aims to analyze and explore customer churn behavior in a Telco company using data analytics techniques. Customer churn, or attrition, is the phenomenon where customers stop doing business with a company. Understanding the factors contributing to churn and predicting which customers are likely to churn can help companies take proactive measures to retain customers and improve business performance.

The project consists of the following components:

1. Data Collection: Data was collected from the Telco company's database, containing information about customers, their services, and churn status.

2. Exploratory Data Analysis (EDA): The dataset was analyzed to understand the distribution of variables, identify patterns, and explore relationships between features and churn status.

3. Predictive Modeling: Machine learning models were built to predict customer churn based on historical data. Various classification algorithms such as Decision Trees, Logistic Regression, and Random Forest were employed.

4. Dashboard Application: A Streamlit dashboard was developed to provide interactive visualizations and insights from the analysis. Users can explore data, view key performance indicators (KPIs), and make predictions using the deployed models.

Requirements
Python 3.x
Streamlit
Pandas
Seaborn
Matplotlib
Plotly
PyODBC


Installation
1. Clone the repository:

git clone https://github.com/Patoski254/Telco-Customer-Churn-Analysis.git

2. Navigate to the project directory:

cd Embedding-Machine-Learning-Models

3. Install the required dependencies:
pip install -r requirements.txt

4. Usage
Ensure their is access to the Telco company's database 

5. Run the Streamlit application:

streamlit run main.py

Access the application in web browser using the provided URL.

Folder Structure

1. data: Contains the dataset files used for analysis.
2. models: Stores trained machine learning models.
3. history_data: Stores historical predictions and analysis results.
4. src: Contains source code files for data processing, modeling, and dashboard development.
5. config.ini: Configuration file for database connection details.
6. main.py: Main Streamlit application file.



License
This project is licensed under the MIT License. See the LICENSE file for details.