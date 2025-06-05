
import streamlit as st
import pandas as pd
from supabase_connector import supabase

st.set_page_config(page_title="📊 Dashboard", layout="wide")
uploaded_file = st.session_state.get('csv_data', None)
st.title("📊 EuroGenius Dashboard")

email = st.session_state.get("user_email", "gast@demo.com")

# CSV wird global aus der Sidebar geladen

if uploaded_file is not None:
    df = uploaded_file
    st.subheader("📅 Letzte 5 Ziehungen")
    st.dataframe(df.tail(5))

    zahlen = df.iloc[:, 1:6].values.flatten()
    haeufigkeit = pd.Series(zahlen).value_counts().sort_values(ascending=False)
    st.subheader("🔢 Häufigste Zahlen")
    st.bar_chart(haeufigkeit.head(10))

st.divider()

st.subheader("🧠 Letzte KI-Tipps")
try:
    eintraege = supabase.table("strategien").select("*").eq("email", email).order("created_at", desc=True).limit(5).execute()
    daten = eintraege.data
    if daten:
        for eintrag in daten:
            st.markdown(f"- **{eintrag['strategy_name']}** → {eintrag['parameters'].get('tipp', [])}")
    else:
        st.info("Noch keine gespeicherten Strategien.")
except Exception as e:
    st.error(f"Fehler beim Laden der Strategien: {e}")
