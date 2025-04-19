import streamlit as st

def show_nav():
    st.sidebar.title("EuroGenius Navigation")
    st.sidebar.page_link("pages/dashboard.py", label="📊 Dashboard")
    st.sidebar.page_link("pages/tipp_generator.py", label="🔮 Tipp Generator")
    st.sidebar.page_link("pages/strategien.py", label="♟️ Strategien")
    st.sidebar.page_link("pages/login.py", label="🔐 Login")
