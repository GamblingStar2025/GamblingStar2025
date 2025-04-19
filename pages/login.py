import streamlit as st
email = st.text_input("E-Mail")
if st.button("Login"):
    st.session_state["email"] = email
    st.success("Eingeloggt als " + email)
