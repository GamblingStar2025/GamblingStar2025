import streamlit as st
import pandas as pd
import random

st.set_page_config(page_title="🎰 Tipp Generator", layout="centered")
st.title("🎰 Tipp Generator")

uploaded_file = st.session_state.get("csv_data", None)

@st.cache_data
def lade_haeufigkeit(datei):
    df = pd.read_csv(datei)
    zahlen = df.iloc[:, :6].values.flatten()
    haeufigkeit = pd.Series(zahlen).value_counts().sort_index()
    return haeufigkeit

if uploaded_file is not None:
    gewichtung = lade_haeufigkeit(uploaded_file)
    st.bar_chart(gewichtung)

    st.subheader("🎯 Zufallstipps basierend auf Gewichtung")

    top_zahlen = gewichtung.nlargest(20).index.tolist()
    anzahl_tipps = st.slider("Wie viele Tipps möchtest du generieren?", 1, 10, 5)

    for i in range(anzahl_tipps):
        tipp = sorted(random.sample(top_zahlen, 5))
        sterne = sorted(random.sample(range(1, 13), 2))
        with st.container():
            st.markdown(f"### 🧾 Tipp {i+1}")
            st.success(f"Zahlen: {tipp}")
            st.info(f"⭐ Sterne: {sterne}")

    if st.button("🧠 Tipps als Strategie speichern"):
        email = st.session_state.get("user_email", "gast@demo.com")
        from supabase_connector import supabase
        supabase.table("strategien").insert({
            "email": email,
            "name": "Tipp Generator",
            "parameter": {"tipps": anzahl_tipps, "quelle": "gewichtung"}
        }).execute()
        st.success("✅ Strategie gespeichert!")
else:
    st.info("📥 Bitte lade eine CSV-Datei mit Ziehungszahlen hoch.")
