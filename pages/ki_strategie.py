
import streamlit as st
import pandas as pd
import random
from supabase_connector import supabase

st.set_page_config(page_title="🤖 KI-Strategie", layout="centered")
uploaded_file = st.session_state.get('csv_data', None)
st.title("🤖 KI-Strategie – Intelligente Tipp-Generierung")

email = st.session_state.get("user_email", "gast@demo.com")

@st.cache_data
def lade_haeufigkeit(datei):
    df = pd.read_csv(datei)
    zahlen = df.iloc[:, 1:6].values.flatten()
    haeufigkeit = pd.Series(zahlen).value_counts().sort_index()
    return haeufigkeit

uploaded_file = st.markdown('ℹ️ **Lade eine Datei im Format wie `EuroMillion_Ziehungen.csv` hoch.**')
    st.file_uploader("📄 Ziehungsdaten (CSV)", type="csv", help='Datei mit 5 Lottozahlen pro Ziehung im CSV-Format (z. B. Spalten: Datum, Zahl1-Zahl5)')

if uploaded_file is not None:
    gewichtung = lade_haeufigkeit(uploaded_file)
    st.write("📊 Häufigkeit", gewichtung)

    intensitaet = st.slider("🤖 Intelligenzfaktor", 0, 200, 100)

    if intensitaet < 100:
        basis = gewichtung.nsmallest(15)
    elif intensitaet > 100:
        basis = gewichtung.nlargest(15)
    else:
        basis = gewichtung

    basis_zahlen = basis.index.tolist()

    if len(basis_zahlen) >= 5:
        tipp = random.sample(basis_zahlen, 5)
        st.success('✅ Generierter Tipp: ' + str("🔢 KI-Tipp: {sorted(tipp)}")

        if st.button("💾 Strategie speichern"):
            try:
                # Versuche zu speichern in Supabase
            supabase.table("strategien").insert({
                    "email": email,
                    "strategy_name": "KI-Strategie",
                    "parameters": {
                        "intelligenz": intensitaet,
                        "tipp": tipp
                    }
                }).execute()
                st.success("✅ KI-Strategie gespeichert.")
            except Exception as e:
                st.error(f"❌ Fehler beim Speichern: {e}")
    else:
        st.error("⚠️ Nicht genügend gültige Zahlen für Tipp-Auswahl.")
else:
    st.info("📥 Bitte eine CSV-Datei hochladen.")
