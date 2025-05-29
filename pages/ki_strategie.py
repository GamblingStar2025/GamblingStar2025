import streamlit as st
import random

uploaded_file = st.session_state.get("csv_data", None)

st.title("🤖 KI-Strategie")

if uploaded_file is not None:
    df = uploaded_file
    häufige = df.iloc[:, 1:].stack().value_counts().head(10).index.tolist()
    tipp = random.sample(häufige, 5)
    st.write("🧠 KI-generierter Tipp:", tipp)
else:
    st.warning("Bitte lade zuerst eine CSV-Datei hoch.")
