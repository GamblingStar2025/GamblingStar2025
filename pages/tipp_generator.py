
import streamlit as st
import random
import pandas as pd
from collections import Counter
from datetime import datetime, timedelta

st.set_page_config(page_title="🎯 Tipp Generator", layout="centered")

st.title("🎯 EuroMillions Tipp Generator")
st.markdown("Basierend auf häufig gezogenen Zahlen und überfälligen Zahlen")

# Nutzer-Parameter
num_tips = st.slider("Wie viele Tipps möchtest du generieren?", 1, 10, 3)
hot_weight = st.slider("Hot-Zahlen-Faktor", 1.0, 3.0, 1.5)
overdue_days = st.slider("Tage seit letztem Vorkommen (Überfällig)", 30, 180, 90)
overdue_boost = st.slider("Boost-Faktor für überfällige Zahlen", 1.0, 3.0, 1.5)

uploaded_file = st.file_uploader("Ziehungsdaten hochladen (CSV)", type=["csv"])
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    if 'Datum' in df.columns:
        df['Datum'] = pd.to_datetime(df['Datum'])
        df = df.sort_values('Datum')
    else:
        st.error("CSV muss eine 'Datum'-Spalte enthalten.")
        st.stop()

    all_numbers = df[['Zahl1', 'Zahl2', 'Zahl3', 'Zahl4', 'Zahl5']].values.flatten()
    all_stars = df[['Stern1', 'Stern2']].values.flatten()

    freq_nums = Counter(all_numbers)
    freq_stars = Counter(all_stars)

    last_date = df['Datum'].max()
    days_since = {}
    for col in ['Zahl1', 'Zahl2', 'Zahl3', 'Zahl4', 'Zahl5']:
        for idx, row in df.iterrows():
            for val in row[[col]]:
                days = (last_date - row['Datum']).days
                if val not in days_since or days < days_since[val]:
                    days_since[val] = days

    def generate_weighted_pool(freq, days_since, total_range):
        pool = []
        for i in range(1, total_range+1):
            weight = 1 + freq.get(i, 0) * hot_weight
            if days_since.get(i, 9999) >= overdue_days:
                weight *= overdue_boost
            pool += [i] * int(weight)
        return pool

    number_pool = generate_weighted_pool(freq_nums, days_since, 50)
    star_pool = generate_weighted_pool(freq_stars, {}, 12)

    def generate_tip():
        return sorted(random.sample(number_pool, 5)), sorted(random.sample(star_pool, 2))

    tips = [generate_tip() for _ in range(num_tips)]

    st.subheader("💡 Generierte Tipps")
    for i, (nums, stars) in enumerate(tips):
        st.markdown(f"**Tipp {i+1}:** Zahlen: {nums} | Sterne: {stars}")
else:
    st.info("Bitte lade zuerst eine CSV-Datei mit den EuroMillions-Ziehungen hoch.")
