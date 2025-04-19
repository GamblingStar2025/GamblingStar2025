
import streamlit as st
import pandas as pd

st.title("📊 Strategien Übersicht")

strategien = {
    "🔥 Heiße Zahlen": "Die am häufigsten gezogenen Zahlen.",
    "❄️ Kalte Zahlen": "Die am seltensten gezogenen Zahlen.",
    "🎡 Rad-Prinzip": "Gleichmäßige Verteilung über Zahlenbereiche.",
    "🧠 KI-Vorhersage": "Künstliche Intelligenz-basierte Analyse.",
    "🎰 Monaco Casino Simulation": "Monte-Carlo-Simulation für Wahrscheinlichkeiten.",
    "🔀 Kombinations-Mischer": "Mische Strategien für viele Variationen."
}

uploaded_file = st.session_state.get("csv_file", None)
if not uploaded_file:
    st.warning("Bitte zuerst eine CSV-Datei hochladen.")
else:
    df = pd.read_csv(uploaded_file)
    for name, beschreibung in strategien.items():
        with st.expander(name):
            st.markdown(f"**Beschreibung:** {beschreibung}")
            st.write("Einstellungen & Analyse folgen...")
