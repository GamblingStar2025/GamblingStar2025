
import streamlit as st
import random
import pandas as pd
from collections import Counter

st.set_page_config(page_title="Tipp-Konfigurator", layout="centered")
st.title("🛠️ EuroGenius – Dein KI-Tippassistent")

modus = st.radio("Modus", ["👤 Einzelspieler", "👥 Gemeinschaft"])
land = st.selectbox("Land", ["🇨🇭 Schweiz", "🇩🇪 Deutschland", "🇫🇷 Frankreich", "🇦🇹 Österreich"])
waehrung = "CHF" if "Schweiz" in land else "€"
preis = 3.5 if "Schweiz" in land else 2.5
anzahl = st.slider("Anzahl Tipps", 1, 50)
ki = st.slider("KI-Gewichtung", 0, 200, 100)
sim = st.slider("Simulationen", 1000, 1000000, 100000)

st.markdown("### 🧠 Analyse-Strategien")
use_hot = st.checkbox("🔥 Hot/Cold", value=True)
use_cluster = st.checkbox("🧩 Cluster", value=True)
use_rad = st.checkbox("♻️ Rad-Prinzip", value=True)
use_monte = st.checkbox("🎲 Monte Carlo", value=True)

kosten = anzahl * preis
st.markdown(f"💰 **Gesamtkosten:** `{kosten:.2f} {waehrung}`")

if "df" not in st.session_state:
    st.warning("⚠️ Bitte lade zuerst eine CSV-Datei hoch.")
    st.stop()

df = st.session_state.df
zahlenspalten = [c for c in df.columns if any(str(n) in c.lower() for n in ["1", "2", "3", "4", "5"]) and not "stern" in c.lower()]
sternspalten = [c for c in df.columns if "stern" in c.lower() or "star" in c.lower()]
zahlen = df[zahlenspalten[:5]].values.flatten()
zahlen_counter = Counter(zahlen)

def generate_tip():
    pool = list(range(1, 51))
    stars = list(range(1, 13))
    hot = [n for n, _ in zahlen_counter.most_common(15)] if use_hot else []
    cluster_nums = [n for n in zahlen if use_cluster and n <= 30]
    rad_nums = [n for n in zahlen if use_rad and (n % 2 == 0 or n <= 25)]
    monte_nums = []
    if use_monte:
        for _ in range(sim // 1000):
            monte_nums += random.sample(pool, 5)
    pool_mix = pool + hot + cluster_nums + rad_nums + monte_nums
    zahlen_tip = sorted(random.sample(pool_mix, 5))
    sterne_tip = sorted(random.sample(stars, 2))
    return zahlen_tip, sterne_tip

if st.button("📊 Tipps generieren"):
    tipps = [generate_tip() for _ in range(anzahl)]
    st.session_state.tipps = tipps
    st.switch_page("pages/results.py")
