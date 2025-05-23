
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from collections import Counter
import random

st.set_page_config(page_title="Analyse Ergebnisse", layout="centered")
st.title("🔎 Analyse-Ergebnisse & Vorhersagen")

if "df" not in st.session_state:
    st.warning("⚠️ Keine Daten gefunden. Bitte lade zuerst eine CSV hoch.")
    st.stop()

df = st.session_state.df
cols = df.columns.tolist()

# Nutzer wählt Spalten
zahlenspalten = st.multiselect("Wähle 5 Spalten für Zahlen", cols, max_selections=5)
sternspalten = st.multiselect("Wähle 2 Spalten für Sterne", cols, max_selections=2)

if len(zahlenspalten) == 5 and len(sternspalten) == 2:
    zahlen = df[zahlenspalten].values.flatten()
    sterne = df[sternspalten].values.flatten()

    # Hot/Cold
    zahlen_counter = Counter(zahlen)
    hot_zahlen = zahlen_counter.most_common(10)
    cold_zahlen = zahlen_counter.most_common()[-10:]

    st.subheader("🔥 Hot-Zahlen")
    st.write(pd.DataFrame(hot_zahlen, columns=["Zahl", "Häufigkeit"]))

    st.subheader("❄️ Cold-Zahlen")
    st.write(pd.DataFrame(cold_zahlen, columns=["Zahl", "Häufigkeit"]))

    # Cluster
    st.subheader("🧩 Cluster")
    cluster_ranges = [(1,10), (11,20), (21,30), (31,40), (41,50)]
    cluster_counts = {f"{start}-{end}": 0 for start, end in cluster_ranges}
    for num in zahlen:
        for start, end in cluster_ranges:
            if start <= num <= end:
                cluster_counts[f"{start}-{end}"] += 1
    st.write(pd.DataFrame(list(cluster_counts.items()), columns=["Cluster", "Anzahl"]))

    # Rad-Prinzip
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

    # Monte Carlo
    st.subheader("🎲 Monte Carlo (100.000 Ziehungen)")
    simulated = []
    for _ in range(100000):
        simulated.append(tuple(sorted(random.sample(range(1, 51), 5))))
    sim_counter = Counter(simulated)
    top_sets = sim_counter.most_common(5)
    st.write("Top 5 Kombinationen:")
    st.write(pd.DataFrame([{"Kombination": list(k), "Häufigkeit": v} for k, v in top_sets]))

else:
    st.info("Bitte wähle genau 5 Zahlen- und 2 Sternspalten.")

if st.button("⬅️ Zurück zur Analysezentrale"):
    st.switch_page("pages/analyse.py")
