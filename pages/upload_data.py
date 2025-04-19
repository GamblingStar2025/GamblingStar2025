
import streamlit as st
import pandas as pd

st.title("📤 Ziehungsdaten hochladen")

uploaded_file = st.file_uploader("Wähle eine CSV-Datei mit Lottoziehungen aus", type=["csv"])

if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.success("✅ Datei erfolgreich geladen!")
    st.dataframe(df)
else:
    st.info("Noch keine Datei hochgeladen.")
