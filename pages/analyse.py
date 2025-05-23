
import streamlit as st

st.set_page_config(page_title="Analysezentrale", layout="centered")
st.title("🧠 Analysezentrale")

st.markdown("Hier kannst du deine Ziehungen analysieren und Vorhersagen erstellen.")

if st.button("📤 CSV hochladen"):
    st.switch_page("pages/csv_upload.py")
