
import streamlit as st

# Statusleiste direkt in die Datei eingebaut
def show_login_status():
    st.markdown("## 🚦 Statusleiste")

    if st.session_state.get("is_logged_in"):
        st.success(f"✅ Eingeloggt als: {st.session_state.get('user_email', 'Unbekannt')}")
        if st.button("➡️ Weiter zur App"):
            st.switch_page("pages/main_app.py")
    else:
        st.warning("🚫 Du bist nicht eingeloggt.")
        if st.button("🔐 Zur Anmeldung"):
            st.switch_page("pages/login.py")

# App-Seite
st.set_page_config(page_title="EuroGenius", layout="centered")

st.image("https://upload.wikimedia.org/wikipedia/commons/5/53/Lottery_icon.png", width=100)
st.markdown("## 🎯 Willkommen bei EuroGenius")
st.markdown("**Dein KI-gestützter Lotto-Assistent für EuroMillions**")

# Zeige Login-Status
show_login_status()

if st.button("🎲 Jetzt starten"):
    st.switch_page("pages/login.py")
