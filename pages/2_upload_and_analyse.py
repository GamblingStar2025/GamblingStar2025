
import streamlit as st
import pandas as pd

st.set_page_config(page_title="CSV & Analyse", layout="centered")
st.title("📤 CSV hochladen & analysieren")

file = st.file_uploader("Wähle deine EuroMillions CSV", type="csv")

if file:
    try:
        df = pd.read_csv(file)
        st.session_state.df = df
        st.success("CSV erfolgreich geladen & gespeichert.")
        st.dataframe(df.tail())

        if st.button("➡️ Weiter zur Vorhersage"):
            st.switch_page("3_weighted_prediction")
    except Exception as e:
        st.error(f"Fehler beim Einlesen: {e}")
else:
    st.info("Bitte lade eine gültige CSV-Datei hoch.")
