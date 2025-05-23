
import streamlit as st
import pandas as pd

st.set_page_config(page_title="CSV Upload", layout="centered")
st.title("📤 EuroMillions CSV hochladen")

file = st.file_uploader("Wähle deine CSV-Datei (5 Zahlen + 2 Sterne)", type="csv")

if file:
    try:
        df = pd.read_csv(file)
        st.session_state.df = df
        st.success("Datei erfolgreich geladen.")
        st.dataframe(df.tail())
        if st.button("🔍 Weiter zur Analyse"):
            st.switch_page("pages/results.py")
    except Exception as e:
        st.error(f"Fehler beim Einlesen: {e}")
else:
    st.info("Bitte lade eine gültige CSV-Datei hoch.")
