# Session handling for uploaded CSV
import streamlit as st

def init_session():
    if 'csv_data' not in st.session_state:
        st.session_state['csv_data'] = None
