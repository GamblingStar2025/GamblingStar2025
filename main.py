
import streamlit as st

st.set_page_config(
    page_title="EuroGenius Start",
    layout="centered",
    initial_sidebar_state="collapsed"
)

st.title("🎯 Willkommen bei EuroGenius")
st.markdown("Starte jetzt deine individuelle Analyse und Vorhersage für EuroMillions.")

if st.button("🚀 Jetzt starten"):
    st.switch_page("pages/analyse.py")
