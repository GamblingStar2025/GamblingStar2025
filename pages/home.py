
import streamlit as st

def show_home():
    st.markdown("<h1 style='text-align:center;'>Willkommen bei EuroGenius</h1>", unsafe_allow_html=True)
    st.write("Analyse. Strategie. Gewinnchance.")
    if st.button("🎯 Jetzt starten"):
        st.switch_page("pages/login.py")
