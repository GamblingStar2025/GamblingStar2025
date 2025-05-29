
import streamlit as st
import pandas as pd
import random

st.set_page_config(page_title="🧠 Meta-Strategie", layout="wide")
st.title("🧠 Meta-Strategie – Kombination aller Taktiken")

# CSV wird global aus Sidebar geladen\nuploaded_file = st.session_state.get('csv_data', None)"📄 Ziehungsdaten (CSV)", type="csv")

if uploaded_file:
    df = uploaded_file
    zahlen = df.iloc[:, 1:6].values.flatten()

    selected_strategies = []
    if st.checkbox("🔢 Häufigkeitsbasierte Strategie"):
        haeufigkeit = pd.Series(zahlen).value_counts().nlargest(15).index.tolist()
        if len(haeufigkeit) >= 5:
            selected_strategies.append(random.sample(haeufigkeit, 5))

    if st.checkbox("🧠 KI-Gewichtung: Top-Werte"):
        top_zahlen = pd.Series(zahlen).value_counts().nlargest(10).index.tolist()
        if len(top_zahlen) >= 5:
            selected_strategies.append(random.sample(top_zahlen, 5))

    if st.checkbox("🌀 Fibonacci-Zahlen"):
        fibo = [0, 1]
        while fibo[-1] < 100:
            fibo.append(fibo[-1] + fibo[-2])
        fibo_zahlen = [z for z in zahlen if z in fibo]
        if len(fibo_zahlen) >= 5:
            selected_strategies.append(random.sample(fibo_zahlen, 5))

    if st.checkbox("♾️ Symmetrische Zahlen"):
        sym = [z for z in zahlen if str(z) == str(z)[::-1] or z % 11 == 0]
        if len(sym) >= 5:
            selected_strategies.append(random.sample(sym, 5))

    if selected_strategies:
        st.subheader("✨ Generierte Meta-Tipps")
        for i, tipp in enumerate(selected_strategies, start=1):
            st.success(f"Tipp {i}: {sorted(tipp)}")
    else:
        st.warning("⚠️ Bitte mindestens eine Strategie aktivieren.")
else:
    st.info("📥 Bitte eine CSV-Datei hochladen.")
