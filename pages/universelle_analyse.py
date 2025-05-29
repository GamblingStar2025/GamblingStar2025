
import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(page_title="♾️ Universelle Muster & Quantenanalyse", layout="wide")
uploaded_file = st.session_state.get('csv_data', None)
st.title("♾️ Universelle Muster & Quanten-Logik")

# CSV wird global aus Sidebar geladen\nuploaded_file = st.session_state.get('csv_data', None)"📄 Ziehungsdaten (CSV)", type="csv")

fibonacci_set = set([0, 1])
a, b = 0, 1
while b <= 100:
    a, b = b, a + b
    fibonacci_set.add(b)

def ist_spiegelzahl(n):
    return str(n) == str(n)[::-1]

if uploaded_file is not None:
    df = uploaded_file
    zahlen = df.iloc[:, 1:6].values.flatten()

    st.subheader("♻️ Spiegelzahlen")
    spiegel = [z for z in zahlen if ist_spiegelzahl(z)]
    st.write(f"Gespiegelte Zahlen: {sorted(set(spiegel))} (Anzahl: {len(spiegel)})")

    st.subheader("🌀 Fibonacci-Zahlen in Ziehungen")
    fiboz = [z for z in zahlen if z in fibonacci_set]
    st.write(f"Zahlen aus Fibonacci-Reihe: {sorted(set(fiboz))} (Anzahl: {len(fiboz)})")

    st.subheader("🔀 Goldener Schnitt – Abstand der Zahlen")
    ratios = []
    for i in range(len(zahlen) - 1):
        if zahlen[i+1] != 0:
            r = zahlen[i] / zahlen[i+1]
            if 1.5 < r < 1.7:
                ratios.append((zahlen[i], zahlen[i+1], round(r, 3)))
    st.write(f"Goldener Schnitt Paare (ungefähr ~1.618):")
    st.dataframe(ratios)

    st.subheader("♾️ Quantenmuster: Symmetrien & Selbstähnlichkeit")
    modulo_sym = [z for z in zahlen if z % 11 == 0 or z in [22, 33, 44]]
    st.write(f"Symmetrische Zahlen (mod 11): {sorted(set(modulo_sym))}")

    st.success("✅ Universelle Analyse abgeschlossen.")
else:
    st.info("📥 Bitte eine CSV-Datei hochladen.")
