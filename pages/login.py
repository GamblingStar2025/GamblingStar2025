
import streamlit as st

st.title("🔐 Login")
email = st.text_input("Email Adresse")
if st.button("Login"):
    st.success(f"Eingeloggt als {email}")
