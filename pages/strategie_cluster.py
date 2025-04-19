
import streamlit as st
import pandas as pd
from collections import Counter, defaultdict

st.title("🧩 Cluster-Strategie")

if "lotto_daten" not in st.session_state:
    st.warning("Bitte lade zuerst eine CSV-Datei auf der Seite 'Ziehungsdaten hochladen'.")
    st.stop()

df = st.session_state["lotto_daten"]

try:
    cluster_counts = defaultdict(int)

    for col in df.columns:
        for value in df[col]:
            try:
                zahl = int(value)
                if 1 <= zahl <= 50:
                    cluster = (zahl - 1) // 10 + 1  # Cluster 1 = 1–10, 2 = 11–20, ...
                    cluster_counts[cluster] += 1
            except:
                continue

    st.subheader("Cluster-Auswertung")
    for cluster in sorted(cluster_counts.keys()):
        st.write(f"Cluster {cluster*10-9}–{cluster*10}: {cluster_counts[cluster]} Zahlen")
except Exception as e:
    st.error(f"Fehler bei der Analyse: {e}")
