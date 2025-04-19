
import streamlit as st
import itertools
import random

st.title("🔀 Kombinationsmischer")

st.markdown("""
Diese Strategie erstellt zufällige Kombinationen von Zahlen – bis zu 1 Million mögliche Varianten!
Nur eine Stichprobe wird angezeigt.
""")

alle_zahlen = list(range(1, 51))
alle_sterne = list(range(1, 13))

anzahl_kombis = st.slider("Anzahl Kombinationen", 1, 10, 5)

kombis = [sorted(random.sample(alle_zahlen, 5)) + ["+"] + sorted(random.sample(alle_sterne, 2)) for _ in range(anzahl_kombis)]

for i, komb in enumerate(kombis, 1):
    st.write(f"🎲 Kombination {i}: {komb}")
