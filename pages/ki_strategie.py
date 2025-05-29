import streamlit as st
import pandas as pd
import random

st.set_page_config(page_title="🧠 KI-Strategie Plus", layout="centered")
st.title("🧠 Erweiterte KI-Strategie")

uploaded_file = st.session_state.get("csv_data", None)

@st.cache_data
def analysiere_daten(df):
    zahlen = df.iloc[:, :6].values.flatten()
    haeufigkeit = pd.Series(zahlen).value_counts().sort_values(ascending=False)
    letzte_ziehung = df.iloc[-1, :6].tolist()
    return haeufigkeit, letzte_ziehung

if uploaded_file is not None:
    df = uploaded_file
    gewichtung, letzte = analysiere_daten(df)

    top_zahlen = gewichtung.index.tolist()[:25]
    st.subheader("🎯 KI-Tipps: Basierend auf Häufigkeit + Letzte Ziehung")

    anzahl_tipps = st.slider("Wie viele KI-Tipps generieren?", 1, 5, 3)
    bereits_verwendete = set()

    for i in range(anzahl_tipps):
        vorschlag = []
        while len(vorschlag) < 5:
            kandidat = random.choice(top_zahlen)
            if kandidat not in vorschlag:
                vorschlag.append(kandidat)

        vorschlag.sort()
        bereits_verwendete.update(vorschlag)

        sterne = sorted(random.sample(range(1, 13), 2))
        schnittstelle = set(vorschlag).intersection(set(letzte))
        bewertung = f"✅ Übereinstimmung mit letzter Ziehung: {len(schnittstelle)} Zahlen"

        with st.container():
            st.markdown(f"### 💡 KI-Tipp {i+1}")
            st.success(f"Zahlen: {vorschlag}")
            st.info(f"⭐ Sterne: {sterne}")
            st.caption(bewertung)
else:
    st.warning("📥 Bitte lade eine CSV-Datei mit Ziehungsdaten hoch.")
