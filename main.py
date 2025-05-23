
import streamlit as st

st.set_page_config(page_title="EuroGenius Start", layout="centered")
st.title("✨ Willkommen bei EuroGenius")

if st.button("📊 Zur Analysezentrale"):
    st.switch_page("pages/analyse.py")
