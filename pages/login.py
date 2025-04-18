
import streamlit as st
from st_supabase_connection import SupabaseConnection

st.set_page_config(page_title="Login", layout="centered")
st.title("🔐 EuroGenius Login")

conn = st.connection("supabase", type=SupabaseConnection)
supabase = conn.client

email = st.text_input("📧 E-Mail")
pw = st.text_input("🔑 Passwort", type="password")

if st.button("➡️ Login"):
    try:
        auth_response = supabase.auth.sign_in_with_password({"email": email, "password": pw})
        user = auth_response.user

        if user:
            st.session_state["is_logged_in"] = True
            st.session_state["user_email"] = email
            st.session_state["rolle"] = "gast"  # Standardrolle, ggf. aus DB laden
            st.success("✅ Eingeloggt!")
            st.switch_page("pages/home.py")
        else:
            st.error("❌ Anmeldung fehlgeschlagen.")
    except Exception as e:
        st.error(f"❌ Fehler: {e}")
