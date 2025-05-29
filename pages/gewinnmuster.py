
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="📈 Gewinnmuster & Trends", layout="wide")
uploaded_file = st.session_state.get('csv_data', None)
st.title("📈 Gewinnmuster & Statistische Trends")

# CSV wird global aus Sidebar geladen\nuploaded_file = st.session_state.get('csv_data', None)"📄 Ziehungsdaten (CSV)", type="csv")

if uploaded_file is not None:
    df = uploaded_file
    df_zahlen = df.iloc[:, 1:6]

    st.subheader("🧮 Durchschnittliche Ziehungssumme")
    summen = df_zahlen.sum(axis=1)
    st.line_chart(summen)

    st.subheader("🔁 Wiederholungen in Ziehungen")
    wiederholung_count = 0
    for i in range(1, len(df_zahlen)):
        set1 = set(df_zahlen.iloc[i-1])
        set2 = set(df_zahlen.iloc[i])
        if set1 & set2:
            wiederholung_count += 1
    st.info(f"In {wiederholung_count} von {len(df_zahlen)-1} Ziehungen gab es mindestens eine Wiederholung.")

    st.subheader("📉 Abstand bis Zahl erneut erscheint")
    flat = df_zahlen.values.flatten()
    series = pd.Series(flat)
    letzte_sicht = {}
    abstaende = []

    for i, z in enumerate(series):
        if z in letzte_sicht:
            abstaende.append(i - letzte_sicht[z])
        letzte_sicht[z] = i

    if abstaende:
        abstand_df = pd.Series(abstaende)
        st.bar_chart(abstand_df.value_counts().sort_index())

    st.success("✅ Gewinnmuster analysiert.")
else:
    st.info("📥 Bitte eine CSV-Datei hochladen.")
