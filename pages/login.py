import streamlit as st
from supabase import create_client

url = st.secrets["SUPABASE_URL"]
key = st.secrets["SUPABASE_KEY"]
supabase = create_client(url, key)

st.title("🔐 Login")

email = st.text_input("E-Mail")
password = st.text_input("Passwort", type="password")

if st.button("Einloggen"):
    try:
        user = supabase.auth.sign_in_with_password({"email": email, "password": password})
        st.success("✅ Erfolgreich eingeloggt!")
    except Exception as e:
        st.error(f"❌ Fehler beim Login: {e}")
