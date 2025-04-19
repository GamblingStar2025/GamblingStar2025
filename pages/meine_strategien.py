
import streamlit as st
import pandas as pd

st.title("🧠 Meine Strategien")

data = {
    "Strategie": [
        "Heiße Zahlen", "Kalte Zahlen", "Cluster-Analyse",
        "Monaco Casino Style", "Rad-Prinzip", "KI-Prognose & Kombinatorik"
    ],
    "Anteil (%)": [60, 40, 55, 45, 50, 70]
}
df = pd.DataFrame(data)
st.table(df)
