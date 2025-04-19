# Tipp Generator Page
import streamlit as st
import pandas as pd

def show():
    st.title("Tipp Generator")
    df = st.session_state.get('csv_data')
    if df is not None:
        st.write("Generiere Tipps basierend auf der CSV")
    else:
        st.warning("Bitte zuerst eine CSV hochladen.")