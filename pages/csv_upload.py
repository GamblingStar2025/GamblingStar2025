# CSV Upload Page
import streamlit as st
import pandas as pd

def show():
    st.title("CSV Upload")
    uploaded_file = st.file_uploader("Wähle eine CSV Datei", type=["csv"])
    if uploaded_file:
        df = pd.read_csv(uploaded_file)
        st.session_state['csv_data'] = df
        st.write("CSV Vorschau:", df.head())