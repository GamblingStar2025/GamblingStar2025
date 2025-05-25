
import streamlit as st
import random

st.set_page_config(page_title="Vorhersage", layout="centered")
st.title("🎯 Vorhersage")

if "df" not in st.session_state:
    st.warning("⚠️ Bitte lade zuerst eine CSV-Datei hoch.")
    st.stop()

df = st.session_state.df
zahlen = df.iloc[:, :5].values.flatten()
sterne = df.iloc[:, 5:7].values.flatten()

def generate_tip():
    z_pool = list(set(zahlen))
    if len(z_pool) < 5:
        z_pool = list(range(1, 51))
    s_pool = list(set(sterne))
    if len(s_pool) < 2:
        s_pool = list(range(1, 13))
    return sorted(random.sample(z_pool, 5)), sorted(random.sample(s_pool, 2))

if st.button("🎯 Tipp generieren"):
    z, s = generate_tip()
    st.success(f"Tipp: Zahlen: {z} | Sterne: {s}")
