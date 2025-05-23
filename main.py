
import streamlit as st

st.set_page_config(page_title="EuroGenius Start", layout="centered")
st.title("🎯 Willkommen bei EuroGenius")

st.markdown("Starte jetzt deine individuelle Analyse und Vorhersage für EuroMillions.")

if st.button("🚀 Jetzt starten"):
    st.switch_page("pages/analyse.py")
