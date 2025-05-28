
import streamlit as st
from custom_style import eurogenius_css

st.set_page_config(page_title="🧱 Layouts Demo", layout="wide")
st.markdown(eurogenius_css(), unsafe_allow_html=True)
st.title("🎨 EuroGenius Layout-Demo")

tab1, tab2, tab3 = st.tabs(["📊 Dashboard", "🧠 Expander", "📱 Schrittweise"])

with tab1:
    st.subheader("📊 Karten & Kennzahlen (Dashboard-Stil)")
    col1, col2, col3 = st.columns(3)
    col1.metric("Letzte Ziehung", "12 - 18 - 29 - 34 - 45")
    col2.metric("Sterne", "3 - 8")
    col3.metric("Jackpot", "CHF 94 Mio")

with tab2:
    st.subheader("🧠 Strategiepanel mit Expandern")
    with st.expander("🔥 Heiße Zahlen"):
        st.slider("Anteil", 0, 100, 60)
        st.button("💾 Speichern", key="hot")

    with st.expander("🤖 KI Strategie"):
        st.slider("Anpassung", 0, 200, 100)
        st.button("💾 Speichern", key="ki")

with tab3:
    st.subheader("📱 Schritt-für-Schritt")
    st.markdown("### Schritt 1: Strategie wählen")
    st.selectbox("Typ", ["Heiße Zahlen", "Zufall", "KI"])

    st.markdown("### Schritt 2: Parameter festlegen")
    st.slider("Zahlenspan", 1, 50, 25)

    st.markdown("### Schritt 3: Speichern")
    st.button("💾 Speichern", key="step")
