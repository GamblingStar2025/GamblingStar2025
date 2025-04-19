import streamlit as st

def check_login():
    if "user" not in st.session_state:
        st.session_state["user"] = "demo_user@example.com"
    st.sidebar.success(f"Angemeldet als: {st.session_state['user']}")