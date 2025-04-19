
import streamlit as st

def save_strategy(name, anteil):
    st.success(f"Strategie '{name}' mit Anteil {anteil}% gespeichert.")

st.title("🎯 EuroGenius Strategien")

strategien = {
    "🔥 Heiße Zahlen": "hot",
    "❄️ Kalte Zahlen": "cold",
    "🔢 Cluster-Analyse": "cluster",
    "🎰 Monaco Casino Style": "monaco",
    "🌀 Rad-Prinzip": "rad",
    "🧠 KI-Prognose & Kombinatorik": "ki_combo"
}

for title, key in strategien.items():
    with st.expander(title):
        val = st.slider(f"Anteil für {title} (%)", 0, 100, 50, key=key)
        if st.button(f"💾 Strategie speichern ({title})", key=f"save_{key}"):
            save_strategy(title, val)
