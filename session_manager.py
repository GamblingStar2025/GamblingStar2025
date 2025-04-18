
import streamlit as st

def check_login():
    if not st.session_state.get("is_logged_in"):
        st.warning("🔒 Du bist nicht eingeloggt. Weiterleitung zum Login...")
        st.switch_page("pages/login.py")
        st.stop()
