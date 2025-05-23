
import streamlit as st
import pandas as pd
import random
from collections import Counter

st.set_page_config(page_title="Vorhersage", layout="centered")
st.title("🎯 EuroMillions Vorhersage")

if "df" not in st.session_state:
    st.warning("Bitte lade zuerst eine CSV-Datei hoch.")
    st.stop()

df = st.session_state.df
columns = df.columns.tolist()
zahlenspalten = [c for c in columns if any(str(n) in c.lower() for n in ["1", "2", "3", "4", "5"]) and not "stern" in c.lower()]
sternspalten = [c for c in columns if "stern" in c.lower() or "star" in c.lower()]

# Slider zur Gewichtung
st.subheader("⚙️ Gewichtung der Strategien")
hot_weight = st.slider("🔥 Hot/Cold", 0, 200, 100)
cluster_weight = st.slider("🧩 Cluster", 0, 200, 100)
rad_weight = st.slider("♻️ Rad-Prinzip", 0, 200, 100)
monte_weight = st.slider("🎲 Monte Carlo", 0, 200, 100)
ai_weight = st.slider("🧠 KI-Faktor (Test)", 0, 200, 100)

if len(zahlenspalten) >= 5 and len(sternspalten) >= 2:
    zahlen = df[zahlenspalten[:5]].values.flatten()
    sterne = df[sternspalten[:2]].values.flatten()
    zahlen_counter = Counter(zahlen)

    def weighted_tip():
        main_pool = list(range(1, 51))
        star_pool = list(range(1, 13))
        hot = [num for num, _ in zahlen_counter.most_common(15)]
        hot_weighted = hot * (hot_weight // 20)
        clusters = []
        for num in zahlen:
            if num <= 10:
                clusters.append(1)
            elif num <= 20:
                clusters.append(2)
            elif num <= 30:
                clusters.append(3)
            elif num <= 40:
                clusters.append(4)
            else:
                clusters.append(5)
        cluster_freq = Counter(clusters)
        cluster_nums = []
        for c, _ in cluster_freq.most_common(3):
            cluster_range = list(range((c-1)*10+1, c*10+1))
            cluster_nums += cluster_range
        cluster_weighted = cluster_nums * (cluster_weight // 20)
        rad_nums = [n for n in zahlen if n % 2 == 0] + [n for n in zahlen if n <= 25]
        rad_weighted = rad_nums * (rad_weight // 20)
        monte_nums = []
        for _ in range(2000):
            combo = random.sample(main_pool, 5)
            monte_nums += combo
        monte_weighted = monte_nums * (monte_weight // 100)
        mix_pool = main_pool + hot_weighted + cluster_weighted + rad_weighted + monte_weighted
        tip_zahlen = sorted(random.sample(mix_pool, 5))
        tip_sterne = sorted(random.sample(star_pool, 2))
        return tip_zahlen, tip_sterne

    if st.button("🎟️ Vorhersage generieren"):
        tipp = weighted_tip()
        st.success(f"🎫 Dein Tipp: Zahlen: {tipp[0]}  ⭐ Sterne: {tipp[1]}")
else:
    st.warning("Mindestens 5 Zahlen- und 2 Sternspalten erforderlich.")

if st.button("⬅️ Zurück zur Analyse"):
    st.switch_page("pages/upload_and_analyse.py")
