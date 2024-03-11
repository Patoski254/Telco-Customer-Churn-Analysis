import streamlit as st
import pandas as pd
import os

st.set_page_config(
    page_title='History',
    page_icon='',
    layout='wide'
)

st.title('Predictions History')

def show_historic_predictions():
    csv_path = "./history_data/history.csv"
    if os.path.exists(csv_path):
        df = pd.read_csv(csv_path)
        return df
    else:
        return pd.DataFrame()

def clear_history():
    csv_path = "./history_data/history.csv"
    if os.path.exists(csv_path):
        os.remove(csv_path)
        st.success("History cleared successfully!")
    else:
        st.warning("No history found to clear!")

# Call the data function directly
if __name__ == '__main__':
    df = show_historic_predictions()
    st.dataframe(df)

    if st.button("Clear History"):
        clear_history()
