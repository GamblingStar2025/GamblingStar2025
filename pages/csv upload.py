
import streamlit as st
import pandas as pd
from datetime import datetime

st.set_page_config(page_title="CSV Upload", layout="centered")
st.title("📤 EuroMillions CSV hochladen")

file = st.file_uploader("Wähle deine CSV-Datei", type="csv")

if file:
    df = pd.read_csv(file)
    st.session_state.df = df
    st.session_state.csv_timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    st.success("✅ CSV erfolgreich geladen")
    st.dataframe(df.tail())
    if st.button("➡️ Zur Vorhersage"):
        st.switch_page("super_prediction")
