import streamlit as st

def check_login():
    if "email" not in st.session_state:
        st.error("Bitte zuerst einloggen.")
        st.stop()
    return True
