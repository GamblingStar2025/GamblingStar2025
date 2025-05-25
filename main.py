
import streamlit as st

st.set_page_config(page_title="EuroGenius", layout="centered")

st.title("🎯 Willkommen bei EuroGenius")

if st.button("➡️ CSV hochladen"):
    st.switch_page("csv upload")
