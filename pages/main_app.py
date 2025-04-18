from session_manager import check_login
check_login()

import streamlit as st
import random
from custom_style import eurogenius_css

st.set_page_config(page_title="Tippgenerator", layout="centered")
st.markdown(eurogenius_css(), unsafe_allow_html=True)
st.title("🎰 EuroGenius Tippgenerator")

# 🛡 Debug: Session anzeigen
st.subheader("🛠 Debug – Session State")
st.json(st.session_state)

# Login prüfen
if not st.session_state.get("is_logged_in"):
    st.warning("🚫 Du bist nicht eingeloggt. Bitte zuerst anmelden.")
    if st.button("🔐 Zur Anmeldung"):
        st.switch_page("pages/login.py")
    st.stop()

rolle = st.session_state.get("rolle", None)

if rolle == "gast":
    st.info("🔓 Als Gast erhältst du 3 kostenlose Tipps!")
    anzahl = 3
elif rolle == "premium":
    anzahl = st.slider("Wie viele Tipps?", 1, 10, 3)
else:
    st.warning("⚠️ Deine Rolle ist nicht erkannt. Bitte erneut einloggen.")
    if st.button("🔐 Zur Anmeldung"):
        st.switch_page("pages/login.py")
    st.stop()

# Tipp-Generierung
tipps = []
for _ in range(anzahl):
    zahlen = sorted(random.sample(range(1, 51), 5))
    sterne = sorted(random.sample(range(1, 13), 2))
    tipps.append((zahlen, sterne))

if st.button("💾 Tipp speichern"):
    st.success("✅ Tipps gespeichert!")

for idx, (z, s) in enumerate(tipps, 1):
    st.markdown(f"**Tipp {idx}:** {z} ⭐ {s}")
