import streamlit as st
import pandas as pd
import random

st.set_page_config(page_title="🎰 Tipp Generator", layout="centered")
st.title("🎰 Tipp Generator")

uploaded_file = st.session_state.get("csv_data", None)

def lade_haeufigkeit(file):
    try:
        df = pd.read_csv(file)
        zahlen = df.iloc[:, :6].values.flatten()
        haeufigkeit = pd.Series(zahlen).value_counts().sort_index()
        return haeufigkeit
    except Exception as e:
        st.error(f"❌ Fehler beim Verarbeiten der Datei: {e}")
        return pd.Series()

if uploaded_file is not None:
    gewichtung = lade_haeufigkeit(uploaded_file)
    if not gewichtung.empty:
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
