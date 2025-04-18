
import streamlit as st
from custom_style import eurogenius_css
from save_strategy import save_strategy

st.set_page_config(page_title="Strategie-Zentrale", layout="centered")
st.markdown(eurogenius_css(), unsafe_allow_html=True)
st.title("🧠 Strategie-Zentrale – Dein Lotto-Setup")

# 🛡 Debug: Session-Inhalt anzeigen
st.subheader("🛠 Debug – Session State")
st.json(st.session_state)

# Login & Email prüfen
if not st.session_state.get("is_logged_in"):
    st.error("⚠️ Du musst eingeloggt sein.")
    st.stop()

email = st.session_state.get("user_email")
if not email or email == "None":
    st.warning("⚠️ Keine gültige E-Mail in Session. Bitte zurück zum Login.")
    if st.button("🔁 Zurück zur Anmeldung"):
        st.switch_page("pages/login.py")
    st.stop()

# Strategie UI
with st.expander("🔥 Heiße Zahlen", expanded=False):
    hot = st.slider("Anteil heiße Zahlen (%)", 0, 100, 60, key="hot_slider")
    if st.button("💾 Strategie speichern", key="save_hot"):
        res = save_strategy(email, "Heiße Zahlen", {"anteil": hot})
        st.success("✅ Strategie gespeichert.")

with st.expander("❄️ Kalte Zahlen", expanded=False):
    cold = st.slider("Anteil kalte Zahlen (%)", 0, 100, 30, key="cold_slider")
    if st.button("💾 Strategie speichern", key="save_cold"):
        res = save_strategy(email, "Kalte Zahlen", {"anteil": cold})
        st.success("✅ Strategie gespeichert.")
