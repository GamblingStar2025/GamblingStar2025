
import streamlit as st
import pandas as pd
import random
from collections import Counter

st.set_page_config(page_title="EuroGenius", layout="centered")

st.title("🎯 EuroGenius Vorhersage")

if "df" not in st.session_state:
    st.warning("Bitte lade zuerst eine CSV-Datei hoch.")
    st.stop()

df = st.session_state.df
zahlen = df.iloc[:, :5].values.flatten()
sterne = df.iloc[:, 5:7].values.flatten()

def generate_tip():
    zahlen_pool = list(set(zahlen))
    if len(zahlen_pool) < 5:
        zahlen_pool = list(range(1, 51))
    tip_zahlen = sorted(random.sample(zahlen_pool, 5))

    sterne_pool = list(set(sterne))
    if len(sterne_pool) < 2:
        sterne_pool = list(range(1, 13))
    tip_sterne = sorted(random.sample(sterne_pool, 2))

    return tip_zahlen, tip_sterne

if st.button("🎯 Tipp generieren"):
    z, s = generate_tip()
    st.success(f"Tipp: {z} | Sterne: {s}")
