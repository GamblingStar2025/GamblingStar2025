
import streamlit as st
import pandas as pd
import random
from collections import Counter

st.set_page_config(page_title="EuroGenius Super-Vorhersage", layout="centered")
st.title("🚀 EuroGenius – Intelligente Vorhersage")

if "df" not in st.session_state:
    st.warning("Bitte lade zuerst eine CSV-Datei hoch.")
    st.stop()

df = st.session_state.df
columns = df.columns.tolist()
zahlenspalten = [c for c in columns if any(str(n) in c.lower() for n in ["1", "2", "3", "4", "5"]) and not "stern" in c.lower()]
sternspalten = [c for c in columns if "stern" in c.lower() or "star" in c.lower()]

# --- Benutzer-Einstellungen ---
st.subheader("⚙️ Konfiguration")
modus = st.radio("Modus", ["👤 Einzelspieler", "👥 Gruppe"])
land = st.selectbox("Land", ["🇨🇭 Schweiz", "🇩🇪 Deutschland", "🇫🇷 Frankreich", "🇦🇹 Österreich"])
waehrung = "CHF" if "Schweiz" in land else "€"
preis = 3.5 if "Schweiz" in land else 2.5
anzahl = st.slider("Anzahl Tipps", 1, 100, 5)
kosten = anzahl * preis
st.markdown(f"💰 **Gesamtkosten:** `{kosten:.2f} {waehrung}`")

st.subheader("🤖 Strategien & Gewichtung")
hot_weight = st.slider("🔥 Hot/Cold", 0, 200, 100)
cluster_weight = st.slider("🧩 Cluster", 0, 200, 100)
rad_weight = st.slider("♻️ Rad-Prinzip", 0, 200, 100)
monte_weight = st.slider("🎲 Monte Carlo", 0, 200, 100)
ai_weight = st.slider("🧠 KI-Faktor", 0, 200, 100)
sim = st.slider("Monte-Carlo Simulationen", 1000, 100000, 10000)

# --- Tipp-Erzeugung ---
zahlen = df[zahlenspalten[:5]].values.flatten()
sterne = df[sternspalten[:2]].values.flatten()
zahlen_counter = Counter(zahlen)

def generate_tip():
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
    for _ in range(sim // 100):
        combo = random.sample(main_pool, 5)
        monte_nums += combo
    monte_weighted = monte_nums * (monte_weight // 100)
    mix_pool = main_pool + hot_weighted + cluster_weighted + rad_weighted + monte_weighted
    tip_zahlen = sorted(random.sample(mix_pool, 5))
    tip_sterne = sorted(random.sample(star_pool, 2))
    return tip_zahlen, tip_sterne

if st.button("🎯 Vorhersagen generieren"):
    tipps = [generate_tip() for _ in range(anzahl)]
    st.success(f"{anzahl} Tipps generiert für {modus}")
    df_out = pd.DataFrame([{"Tipp": i+1, "Zahlen": t[0], "Sterne": t[1]} for i, t in enumerate(tipps)])
    st.dataframe(df_out)
    csv = df_out.to_csv(index=False).encode("utf-8")
    st.download_button("📥 Download als CSV", data=csv, file_name="eurogenius_tipps.csv", mime="text/csv")

if st.button("🔁 Zurück zum Upload"):
    st.switch_page("pages/csv_upload.py")
