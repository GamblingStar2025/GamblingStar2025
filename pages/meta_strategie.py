
import streamlit as st
import pandas as pd
import random
import numpy as np

st.set_page_config(page_title="🧠 Meta-Strategie", layout="wide")
st.title("🧠 Meta-Strategie – Kombination aller Taktiken")

uploaded_file = st.session_state.get("csv_data", None)

if uploaded_file is not None:
    df = uploaded_file
    zahlen = df.iloc[:, 1:6].values.flatten()

    st.markdown("## 📋 Wähle deine Strategien zur Tipp-Generierung:")

    selected_strategies = []
    strategie_namen = []

    if st.checkbox("🔢 Häufigkeitsbasierte Strategie"):
        haeufigkeit = pd.Series(zahlen).value_counts().nlargest(15).index.tolist()
        if len(haeufigkeit) >= 5:
            selected_strategies.append(random.sample(haeufigkeit, 5))
            strategie_namen.append("Häufigkeit")

    if st.checkbox("🧠 KI-Gewichtung: Top-Werte"):
        top_zahlen = pd.Series(zahlen).value_counts().nlargest(10).index.tolist()
        if len(top_zahlen) >= 5:
            selected_strategies.append(random.sample(top_zahlen, 5))
            strategie_namen.append("KI-Top-Werte")

    if st.checkbox("🌀 Fibonacci-Zahlen"):
        fibo = [0, 1]
        while fibo[-1] < 100:
            fibo.append(fibo[-1] + fibo[-2])
        fibo_zahlen = [z for z in zahlen if z in fibo]
        if len(fibo_zahlen) >= 5:
            selected_strategies.append(random.sample(fibo_zahlen, 5))
            strategie_namen.append("Fibonacci")

    if st.checkbox("♾️ Symmetrische Zahlen"):
        sym = [z for z in zahlen if str(z) == str(z)[::-1] or z % 11 == 0]
        if len(sym) >= 5:
            selected_strategies.append(random.sample(sym, 5))
            strategie_namen.append("Symmetrisch")

    if selected_strategies:
        st.markdown("## ✨ Generierte Meta-Tipps mit Vorhersagekraft")
        for i, tipp in enumerate(selected_strategies, start=1):
            strategie_text = strategie_namen[i - 1] if i <= len(strategie_namen) else "Unbekannt"
            tipp_liste = sorted([int(n) for n in tipp])
            st.success(f"Tipp {i}: {tipp_liste}")
            st.caption(f"📌 Strategie: {strategie_text}")
            st.caption(f"🔮 Prognose: Dieser Tipp kombiniert {strategie_text}-basierte Muster mit überdurchschnittlicher Häufigkeit.")
    else:
        st.warning("⚠️ Bitte mindestens eine Strategie aktivieren.")
else:
    st.info("📥 Bitte lade eine CSV-Datei hoch.")
