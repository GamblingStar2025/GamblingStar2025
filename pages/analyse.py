
import streamlit as st

st.set_page_config(page_title="Analysezentrale", layout="centered")
st.title("🧠 Analysezentrale")

st.markdown("In dieser Zentrale lädst du deine CSV-Daten hoch und konfigurierst deine Analyse.")

if st.button("📤 CSV hochladen"):
    st.switch_page("csv_upload")
