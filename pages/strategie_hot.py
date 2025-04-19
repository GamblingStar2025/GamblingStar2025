
import streamlit as st
import pandas as pd
from collections import Counter

st.title("🔥 Heiße Zahlen Strategie")

# CSV-Daten aus dem Session-State holen
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
    heiße_zahlen = [zahl for zahl, _ in haeufigkeit.most_common(10)]

    st.subheader("Top 10 häufigste (heiße) Zahlen")
    st.write(heiße_zahlen)
except Exception as e:
    st.error(f"Fehler bei der Analyse: {e}")
