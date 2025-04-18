
import streamlit as st

st.set_page_config(page_title="Home", layout="centered")
st.title("🏠 Willkommen bei EuroGenius")

if not st.session_state.get("is_logged_in"):
    st.warning("🔒 Du bist nicht eingeloggt. Bitte zuerst anmelden.")
    if st.button("➡️ Zur Anmeldung"):
        st.switch_page("pages/login.py")
    st.stop()

st.success(f"✅ Eingeloggt als: {st.session_state.get('user_email', '')}")

if st.button("🎲 Weiter zum Tippgenerator"):
    st.switch_page("pages/main_app.py")
