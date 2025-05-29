import streamlit as st
import random

uploaded_file = st.session_state.get("csv_data", None)

st.title("🎰 Tipp Generator")

if uploaded_file is not None:
    zahlen = list(range(1, 51))
    sterne = list(range(1, 13))

    tipp = random.sample(zahlen, 5) + random.sample(sterne, 2)
    st.write("💡 Dein Tipp:", tipp)
else:
    st.warning("Bitte lade zuerst eine CSV-Datei in der Seitenleiste hoch.")
