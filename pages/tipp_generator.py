
import streamlit as st
import pandas as pd
import random
from supabase_connector import supabase

st.set_page_config(page_title="🎯 Tipp Generator", layout="centered")
st.title("🎯 Tipp-Generator")

email = st.session_state.get("user_email", "gast@demo.com")

@st.cache_data
def lade_haeufigkeit(datei):
    df = pd.read_csv(datei)
    zahlen = df.iloc[:, 1:6].values.flatten()
    haeufigkeit = pd.Series(zahlen).value_counts().sort_index()
    return haeufigkeit

uploaded_file = st.file_uploader("📄 Ziehungsdaten (CSV) hochladen", type="csv")
if uploaded_file is not None:
    gewichtung = lade_haeufigkeit(uploaded_file)
    st.bar_chart(gewichtung)

    st.subheader("🔢 Zufallstipp basierend auf Gewichtung")
    top_zahlen = gewichtung.nlargest(10).index.tolist()

    if len(top_zahlen) >= 5:
        tipp = random.sample(top_zahlen, 5)
        st.success(f"Dein Tipp: {sorted(tipp)}")

        if st.button("💾 Tipp als Strategie speichern"):
            try:
                supabase.table("strategien").insert({
                    "email": email,
                    "strategy_name": "Tipp-Generator",
                    "parameters": {"tipp": tipp}
                }).execute()
                st.success("✅ Tipp gespeichert!")
            except Exception as e:
                st.error(f"❌ Fehler beim Speichern: {e}")
    else:
        st.error("⚠️ Nicht genügend häufige Zahlen für 5 Zufallswerte gefunden.")
else:
    st.info("📥 Bitte eine CSV-Datei mit Ziehungszahlen hochladen.")
