
import streamlit as st
from st_supabase_connection import SupabaseConnection
from custom_style import eurogenius_css

st.set_page_config(page_title="Login / Registrierung", layout="centered")
st.markdown(eurogenius_css(), unsafe_allow_html=True)
st.title("🔐 EuroGenius – Login & Registrierung")

conn = st.connection("supabase", type=SupabaseConnection)
supabase = conn.client

mode = st.radio("🔄 Modus wählen", ["🔓 Login", "📝 Registrieren"])

email = st.text_input("📧 E-Mail")
pw = st.text_input("🔑 Passwort", type="password")

if mode == "🔓 Login":
    if st.button("➡️ Login"):
        try:
            auth_response = supabase.auth.sign_in_with_password({"email": email, "password": pw})
            user = auth_response.user

            if user:
                # Nutze direkt eingegebene E-Mail zur Sicherheit
                st.session_state["is_logged_in"] = True
                st.session_state["user_email"] = email
                st.success(f"✅ Eingeloggt als {email}")
                st.rerun()
        except Exception as e:
            st.error(f"❌ Login fehlgeschlagen: {e}")

else:
    if st.button("📝 Registrieren"):
        try:
            supabase.auth.sign_up({"email": email, "password": pw})
            st.success("✅ Registrierung erfolgreich. Bitte einloggen.")
        except Exception as e:
            st.error(f"❌ Registrierung fehlgeschlagen: {e}")
