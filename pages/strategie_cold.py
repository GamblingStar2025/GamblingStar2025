
import streamlit as st
import pandas as pd
from collections import Counter

st.title("❄️ Kalte Zahlen Strategie")

if "lotto_daten" not in st.session_state:
    st.warning("Bitte lade zuerst eine CSV-Datei auf der Seite 'Ziehungsdaten hochladen'.")
    st.stop()

df = st.session_state["lotto_daten"]

try:
    zahlen = []
    for col in df.columns:
        for value in df[col]:
            try:
                zahl = int(value)
                if 1 <= zahl <= 50:
                    zahlen.append(zahl)
            except:
                continue

    haeufigkeit = Counter(zahlen)
    alle_zahlen = list(range(1, 51))
    kalte_zahlen = sorted(alle_zahlen, key=lambda x: haeufigkeit.get(x, 0))[:10]

    st.subheader("Top 10 seltenste (kalte) Zahlen")
    st.write(kalte_zahlen)
except Exception as e:
    st.error(f"Fehler bei der Analyse: {e}")
