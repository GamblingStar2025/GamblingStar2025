
import streamlit as st
import pandas as pd

with st.sidebar:
    st.markdown("## 📁 Datenbasis")
    uploaded_file = st.file_uploader("Lade Ziehungsdaten (CSV)", type="csv")

    if uploaded_file:
        try:
            df = pd.read_csv(uploaded_file)
            st.session_state["csv_data"] = df
            st.success("✅ Datei geladen!")
        except Exception as e:
            st.error(f"❌ Fehler beim Laden: {e}")
