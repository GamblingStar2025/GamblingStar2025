
import streamlit as st
import random
import pandas as pd
from datetime import date

st.set_page_config(page_title="EuroGenius Tipps", layout="centered")

st.title("🎯 EuroGenius – Dein KI-Tippassistent")

# Spielmodus und Land
modus = st.radio("Modus", ["👤 Einzelspieler", "👥 Gemeinschaft"])
land = st.selectbox("Land", ["🇨🇭 Schweiz", "🇩🇪 Deutschland", "🇫🇷 Frankreich", "🇦🇹 Österreich"])
waehrung = "CHF" if "Schweiz" in land else "€"
preis = 3.5 if "Schweiz" in land else 2.5

# Parametersteuerung
anzahl = st.slider("Anzahl Tipps", 1, 50 if modus == "👤 Einzelspieler" else 500)
ki = st.slider("KI-Gewichtung", 0, 200, 100)
sim = st.slider("Simulationen", 1000, 1000000, 100000)

# Methodenwahl
st.markdown("### 🧠 Analyse-Strategien")
use_hot = st.checkbox("🔥 Hot/Cold", value=True)
use_cluster = st.checkbox("🧩 Cluster", value=True)
use_rad = st.checkbox("♻️ Rad-Prinzip", value=False)
use_monte = st.checkbox("🎲 Monte Carlo", value=True)

kosten = anzahl * preis
st.markdown(f"💰 **Gesamtkosten:** `{kosten:.2f} {waehrung}`")

# Tipp-Generator
def generate_euromillions_tip(hot_mode=False):
    numbers = list(range(1, 51))
    stars = list(range(1, 13))
    hot_numbers = [20, 23, 27, 17, 44]
    hot_stars = [2, 9]

    if hot_mode:
        main = random.sample(hot_numbers + random.sample(numbers, 10), 5)
        star = random.sample(hot_stars + random.sample(stars, 4), 2)
    else:
        main = random.sample(numbers, 5)
        star = random.sample(stars, 2)

    return sorted(main), sorted(star)

# Tipps generieren
st.markdown("### 🎟️ Generierte Tipps")
tips = []
for _ in range(anzahl):
    nums, stars = generate_euromillions_tip(use_hot)
    tips.append({"Zahlen": ', '.join(map(str, nums)), "Sterne": ', '.join(map(str, stars))})

if tips:
    df = pd.DataFrame(tips)
    st.dataframe(df)

    csv = df.to_csv(index=False).encode("utf-8")
    st.download_button(
        label="📥 Tipps als CSV herunterladen",
        data=csv,
        file_name="eurogenius_tipps.csv",
        mime="text/csv"
    )
else:
    st.warning("Keine Tipps generiert. Bitte überprüfen Sie die Einstellungen.")
