
import streamlit as st

st.set_page_config(page_title="EuroGenius Start", layout="centered")
st.title("✨ Willkommen bei EuroGenius")

st.markdown("Bereit für intelligente EuroMillions-Vorhersagen?")

if st.button("🔍 Jetzt starten"):
    st.switch_page("pages/upload_and_analyse.py")
