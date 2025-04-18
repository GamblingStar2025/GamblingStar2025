
import streamlit as st
import sys
import os

# Importpfad korrigieren
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from custom_style import eurogenius_css
from statusbar import show_login_status

st.set_page_config(page_title="EuroGenius", layout="centered")
st.markdown(eurogenius_css(), unsafe_allow_html=True)

st.image("https://upload.wikimedia.org/wikipedia/commons/5/53/Lottery_icon.png", width=100)
st.markdown("## 🎯 Willkommen bei EuroGenius")
st.markdown("**Dein KI-gestützter Lotto-Assistent für EuroMillions**")

# Login-Status anzeigen
show_login_status()

if st.button("🎲 Jetzt starten"):
    st.switch_page("pages/login.py")
