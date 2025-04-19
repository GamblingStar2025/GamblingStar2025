
import streamlit as st
import pandas as pd

st.title("🤖 KI-basierte Strategie")

st.markdown("""
Diese Strategie nutzt einfache statistische Analyse (Häufigkeit der Zahlen) aus der CSV-Datei,
um „intelligente“ Vorhersagen zu treffen.
""")

uploaded_file = st.file_uploader("📤 Lade eine EuroMillions CSV-Datei hoch", type=["csv"])

if uploaded_file:
    df = pd.read_csv(uploaded_file)
    zahlen = df.iloc[:, 1:6].apply(pd.to_numeric, errors='coerce')  # Annahme: erste 5 sind Hauptzahlen
    sterne = df.iloc[:, 6:8].apply(pd.to_numeric, errors='coerce')  # Annahme: 6,7 sind Sterne
    
    haeufige_zahlen = zahlen.stack().value_counts().head(5).index.tolist()
    haeufige_sterne = sterne.stack().value_counts().head(2).index.tolist()

    st.success(f"🤖 KI-Tipp: {sorted(haeufige_zahlen)} + Sterne: {sorted(haeufige_sterne)}")
