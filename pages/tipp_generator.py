
import streamlit as st
import pandas as pd
import random

st.set_page_config(page_title="EuroGenius KI Tipp Generator")

st.title("🧠 KI-Tipp Generator für EuroMillions")

uploaded_file = st.file_uploader("📂 Lade die Ziehungsdaten (CSV)", type="csv")

if uploaded_file:
    df = pd.read_csv(uploaded_file, parse_dates=["Datum"])
    df["Zahlen"] = df[["Zahl_1", "Zahl_2", "Zahl_3", "Zahl_4", "Zahl_5"]].values.tolist()
    df["Sterne"] = df[["Stern_1", "Stern_2"]].values.tolist()
    
    # Frequenzanalyse für heiße Zahlen
    zahlen = sum(df["Zahlen"].tolist(), [])
    zahlen_haeufigkeit = pd.Series(zahlen).value_counts().sort_values(ascending=False)
    hot_numbers = zahlen_haeufigkeit.head(10).index.tolist()

    # Kalte Zahlen
    cold_numbers = zahlen_haeufigkeit.tail(10).index.tolist()

    # Tippgenerator mit Strategien
    num_tips = st.slider("🔢 Wie viele Tipps möchtest du generieren?", 1, 1000, 10)
    selected_strategies = st.multiselect("⚙️ Wähle Strategien", ["Hot", "Cold", "Random"], default=["Hot", "Random"])

    def generate_tip():
        tip_numbers = []
        tip_stars = []
        pool = []

        if "Hot" in selected_strategies:
            pool += hot_numbers
        if "Cold" in selected_strategies:
            pool += cold_numbers
        if "Random" in selected_strategies or not pool:
            pool += list(range(1, 51))
        pool = list(set(pool))

        while len(tip_numbers) < 5:
            number = random.choice(pool)
            if number not in tip_numbers:
                tip_numbers.append(number)

        while len(tip_stars) < 2:
            star = random.randint(1, 12)
            if star not in tip_stars:
                tip_stars.append(star)

        return sorted(tip_numbers), sorted(tip_stars)

    tips = [generate_tip() for _ in range(num_tips)]

    df_tips = pd.DataFrame(tips, columns=["Zahlen", "Sterne"])
    st.dataframe(df_tips)

    csv = df_tips.to_csv(index=False).encode("utf-8")
    st.download_button("📥 Exportiere Tipps als CSV", csv, "eurogenius_tips.csv", "text/csv")
