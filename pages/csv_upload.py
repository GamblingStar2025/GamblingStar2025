
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from collections import Counter
import numpy as np
import random

st.set_page_config(page_title="EuroGenius Analyse", layout="centered")
st.title("📊 Analyse deiner EuroMillions Ziehungen")

file = st.file_uploader("CSV hochladen (Zahl1-5, Stern1-2)", type="csv")

if file:
    try:
        df = pd.read_csv(file)
        zahlen_cols = ["Zahl1", "Zahl2", "Zahl3", "Zahl4", "Zahl5"]
        sterne_cols = ["Stern1", "Stern2"]

        zahlen = df[zahlen_cols].values.flatten()
        sterne = df[sterne_cols].values.flatten()

        # Hot/Cold
        zahlen_counter = Counter(zahlen)
        hot_zahlen = zahlen_counter.most_common(10)
        cold_zahlen = zahlen_counter.most_common()[-10:]

        st.subheader("🔥 Hot-Zahlen")
        st.write(pd.DataFrame(hot_zahlen, columns=["Zahl", "Häufigkeit"]))
        st.subheader("❄️ Cold-Zahlen")
        st.write(pd.DataFrame(cold_zahlen, columns=["Zahl", "Häufigkeit"]))

        # Cluster-Analyse
        st.subheader("🧩 Cluster-Verteilung")
        cluster_ranges = [(1,10), (11,20), (21,30), (31,40), (41,50)]
        cluster_counts = {f"{start}-{end}": 0 for start, end in cluster_ranges}
        for num in zahlen:
            for start, end in cluster_ranges:
                if start <= num <= end:
                    cluster_counts[f"{start}-{end}"] += 1

        st.write(pd.DataFrame(list(cluster_counts.items()), columns=["Cluster", "Anzahl"]))

        # Rad-Prinzip: Hoch/Niedrig und Gerade/Ungerade
        st.subheader("♻️ Rad-Prinzip")
        hoch = sum(1 for n in zahlen if n > 25)
        niedrig = sum(1 for n in zahlen if n <= 25)
        gerade = sum(1 for n in zahlen if n % 2 == 0)
        ungerade = sum(1 for n in zahlen if n % 2 != 0)

        st.write(pd.DataFrame([
            ["Hoch (26–50)", hoch],
            ["Niedrig (1–25)", niedrig],
            ["Gerade", gerade],
            ["Ungerade", ungerade]
        ], columns=["Kategorie", "Anzahl"]))

        # Monte Carlo Simulation: häufigste Sets aus 100.000 Zufallsziehungen
        st.subheader("🎲 Monte Carlo (100.000 Ziehungen)")
        simulated = []
        for _ in range(100000):
            simulated.append(tuple(sorted(random.sample(range(1, 51), 5))))
        sim_counter = Counter(simulated)
        top_sets = sim_counter.most_common(5)
        st.write("Top 5 häufigste Kombinationen:")
        st.write(pd.DataFrame([{"Kombination": list(k), "Häufigkeit": v} for k, v in top_sets]))

    except Exception as e:
        st.error(f"Fehler beim Einlesen: {e}")

if st.button("⬅️ Zurück zur Startseite"):
    st.session_state.page = 'start'
    st.experimental_rerun()
