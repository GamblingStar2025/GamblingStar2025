
import streamlit as st
from custom_style import eurogenius_css

st.set_page_config(page_title="🎯 EuroGenius Dashboard", layout="wide")
st.markdown(eurogenius_css(), unsafe_allow_html=True)
st.title("🎯 EuroGenius – Live Dashboard")

# Dashboard-Metrics
st.subheader("📊 Ziehungsübersicht")
col1, col2, col3 = st.columns(3)
col1.metric("Letzte Ziehung", "5 - 12 - 24 - 31 - 46")
col2.metric("Sterne", "3 - 7")
col3.metric("Jackpot", "CHF 68 Mio")

# Strategiepanel
st.subheader("🧠 Strategiewahl")
with st.expander("🔥 Heiße Zahlen"):
    st.slider("Anteil heiße Zahlen (%)", 0, 100, 60)
    st.button("💾 Speichern", key="hot_save_demo")

with st.expander("❄️ Kalte Zahlen"):
    st.slider("Anteil kalte Zahlen (%)", 0, 100, 40)
    st.button("💾 Speichern", key="cold_save_demo")

# Schritt-für-Schritt Mobile-Ansicht
st.subheader("📱 Tippstrategie erstellen (mobilfreundlich)")
st.markdown("### Schritt 1: Strategie wählen")
st.selectbox("Strategietyp", ["Heiße Zahlen", "KI", "Zufall"])

st.markdown("### Schritt 2: Parameter einstellen")
st.slider("Zahlenspan", 1, 50, 25)

st.markdown("### Schritt 3: Strategie speichern")
st.button("📦 Strategie speichern")
