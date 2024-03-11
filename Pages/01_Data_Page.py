# Import necessary libraries
import streamlit as st
import pandas as pd
import pyodbc

# Title of the page
st.title("Data Page")

# Define a function to establish a database connection and cache it
@st.cache_resource(show_spinner='Connecting to Database..')
def connect_to_database():
    connection = pyodbc.connect(
        "DRIVER={SQL Server};SERVER="
        + st.secrets['SERVER']
        + ";DATABASE="
        + st.secrets['DATABASE']
        + ";UID="
        + st.secrets['UID']
        + ";PWD="
        + st.secrets['PWD']
    )

    return connection


# Define a function to execute SQL query and return results as DataFrame
@st.cache_data()
def query_database(query):
    conn = connect_to_database()
    with conn.cursor() as cur:
        cur.execute(query)
        rows = cur.fetchall()

        df = pd.DataFrame.from_records(data=rows, columns=[column[0] for column in cur.description])

    return df

# Define the SQL query
query = "SELECT * FROM LP2_Telco_churn_first_3000"

# Create selection option
column1, column2 = st.columns(2)
with column2:
    option = st.selectbox('Choose columns to be viewed',
                          ('All Columns', 'Numeric Columns', 'Categorical Columns'))

# Execute the SQL query and fetch data
df = query_database(query)

# Display based on selection
if option == 'Numeric Columns':
    st.subheader('Numeric Columns')
    st.write(df.select_dtypes(include='number'))
    
    # Additional information about numerical features
    st.subheader('Numerical Features Information')
    st.write("3 numerical features:")
    st.write("- Tenure: Number of months the customer has stayed with the company")
    st.write("- MonthlyCharges: The amount charged to the customer monthly")
    st.write("- TotalCharges: The total amount charged to the customer")
    
elif option == 'Categorical Columns':
    st.subheader('Categorical Columns')
    st.write(df.select_dtypes(include='object'))
    
    # Additional information about categorical features
    st.subheader('Categorical Features Information')
    st.write("17 categorical features:")
    st.write("- CustomerID: Unique identifier for each customer")
    st.write("- gender: Whether the customer is a male or a female")
    st.write(" - SeniorCitizen: Whether the customer is a senior citizen or not (1, 0)")
    st.write(" - Partner: Whether the customer has a partner or not (Yes, No)")
    st.write(" - Dependent: Whether the customer has dependents or not (Yes, No)")
    st.write(" - PhoneService: Whether the customer has a phone service or not (Yes, No)")
    st.write(" - MultipeLines: Whether the customer has multiple lines (Yes, No, No phone service)")
    st.write(" - InternetService: Customer’s internet service provider (DSL, Fiber optic, No)")
    st.write("- OnlineSecurity: Whether the customer has online security (Yes, No, No internet service)")
    st.write("- OnlineBackup: Whether the customer has an online backup (Yes, No, No internet service)")
    st.write("- DeviceProtection: Whether the customer has device protection (Yes, No, No internet service)")
    st.write(" - TechSupport: Whether the customer has tech support (Yes, No, No internet service)")
    st.write(" - StreamingTV: Whether the customer streams TV (Yes, No, No internet service)")
    st.write("- StreamingMovies: Whether the customer streams movies (Yes, No, No internet service)")
    st.write("- Contract: The contract term of the customer (Month-to-month, One year, Two years)")
    st.write(" - PaperlessBilling: Whether the customer does paperless Billing or not (True, False)")
    st.write("- PaymentMethod: The customer’s payment method (Electronic check, Mailed check, Bank transfer (automatic), Credit card (automatic))")

else:
    st.subheader('Entire Dataset')
    st.write(df)
