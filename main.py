
import streamlit as st

st.set_page_config(page_title="EuroGenius Start", layout="centered")
st.title("✨ Willkommen bei EuroGenius")

if 'page' not in st.session_state:
    st.session_state.page = 'start'

if st.button("📊 Analysen anzeigen"):
    st.session_state.page = 'upload'
    st.experimental_rerun()

if st.session_state.page == 'upload':
    st.switch_page("pages/csv_upload.py")
