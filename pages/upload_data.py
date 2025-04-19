
import streamlit as st
import pandas as pd

st.title("📤 Ziehungsdaten hochladen")

uploaded_file = st.file_uploader("Wähle eine CSV-Datei mit Lottoziehungen aus", type=["csv"])

if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.session_state["lotto_daten"] = df  # <- Hier wird gespeichert
    st.success("✅ Datei erfolgreich geladen und gespeichert!")
    st.dataframe(df)
else:
    st.info("Noch keine Datei hochgeladen.")
